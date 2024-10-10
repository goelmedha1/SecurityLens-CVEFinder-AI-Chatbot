# nmap_tool.py

import nmap
import socket
from langchain.tools import BaseTool

class NmapScanTool(BaseTool):
    name = "nmap_scan"
    description = "Use Nmap to perform network scans on given IP addresses or hostnames."

    def _run(self, query: str):
        nm = nmap.PortScanner()
        try:
            if 'local' in query:
                local_ip = self.get_local_ip()  #Get loacal IP
                target = f"{local_ip.split('.', 1)[0]}.0/24"  #Adjust subnet mask to scan entire network
            else:
                target = query.split()[-1]  # Assuming the last word in the query is the IP or hostname

            # Use TCP connect scan (-sT) which doesn't require root privileges
            scan_result = nm.scan(hosts=target, arguments='-sT')
            
            result = []
            for host in nm.all_hosts():
                host_info = f"Host: {host} ({nm[host].hostname() or 'Unknown hostname'})"
                result.append(host_info)

                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        port_info = f"Port: {port}, State: {nm[host][proto][port]['state']}"
                        result.append(port_info)

            return "\n".join(result) if result else "No devices or open ports found on the network."
        
        except Exception as e:
            return f"Error performing Nmap scan: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("Async mode is not supported for Nmap scans.")
    
    def get_local_ip(self):
        """
        Get the local IP address of the machine by connecting to an external server.
        This avoids returning the loopback address (127.0.0.1).
        """

        try:
            #create a dummy connection to an external address
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  #Google's public DNS server (no actual data is sent)
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            return f"Error determining local IP: {e}"

        #return socket.gethostbyname(socket.gethostname())
