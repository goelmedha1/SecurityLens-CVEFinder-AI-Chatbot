# nmap_tool.py

import nmap
from langchain.tools import BaseTool

class NmapScanTool(BaseTool):
    name = "nmap_scan"
    description = "Use Nmap to perform network scans on given IP addresses or hostnames."

    def _run(self, query: str):
        nm = nmap.PortScanner()
        try:
            target = query.split()[-1]  # Assuming the last word in the query is the IP or hostname
            # Use TCP connect scan (-sT) which doesn't require root privileges
            scan_result = nm.scan(hosts=target, arguments='-sT')
            
            result = []
            for host in nm.all_hosts():
                result.append(f"Host: {host} ({nm[host].hostname()})")
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        result.append(f"Port: {port}, State: {nm[host][proto][port]['state']}")
            return "\n".join(result)
        
        except Exception as e:
            return f"Error performing Nmap scan: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("Async mode is not supported for Nmap scans.")
