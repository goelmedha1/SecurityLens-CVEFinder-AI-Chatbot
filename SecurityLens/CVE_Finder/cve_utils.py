# # cve_utils.py
# import requests

# def search_cve_database(cve_id):
#     url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
#     params = {
#         'resultsPerPage': 10,
#         'startIndex':0,
#         'cveId': cve_id,
        
#     }
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()  # Will raise an error for bad status codes
#         data = response.json()


#         if data.get('vulnerabilities'):
#             cve_item = data['vulnerabilities'][0]['cve']
#             cve_id = cve_item['id']
#             description = cve_item['descriptions'][0]['value']
#             cve_metric = cve_item.get('metrics', {})
#             return f"{cve_id}: {description} \n Metrics : {cve_metric}"
#         else:
#             return f"No details found for CVE ID: {cve_id}"
#     except requests.exceptions.RequestException as e:
#         return f"Error fetching CVE data: {e}"
    
# # cve_details = search_cve_database("CVE-2020-2020")
# # print(cve_details)
    

# def search_cve_by_product(keyword_search):

#     url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    
#     params = {

#         'keywordSearch': keyword_search,
#         'startIndex': 0,
#         'resultsPerPage': 10

#     }

#     try:
#         response = requests.get(url, params = params)
#         response.raise_for_status()
#         data = response.json()

#         cve_results =[]

#         # write code here
#         # Temporary placeholder return to confirm the function is being called
#         # return f"Function ⁠ search_cve_by_product ⁠ called with keyword: {keyword_search}"
        

#         # Loop through the vulnerabilities and collect relevant details
#         if data.get('vulnerabilities'):
#             cve_details = ""
#             for vulnerability in data['vulnerabilities']:
#                 cve_item = vulnerability.get('cve', {})
#                 cve_id = cve_item.get('id', 'N/A')
#                 description = cve_item.get('descriptions', [{'value': 'No description available'}])[0]['value']
#                 published_date = vulnerability.get('published', 'Unknown')
#                 cve_details += f"{cve_id}: {description} (Published: {published_date})\n\n"
#             return cve_details.strip()
#         else:
#             return f"No CVEs found for the keyword: {keyword_search}"
#     except requests.exceptions.RequestException as e:
#         return f"Error fetching CVE data: {e}"


#print(search_cve_by_product("netbios"))
# print(search_cve_database("CVE-2020-2020"))

#cve_utils.py

import requests
from langchain.tools import BaseTool

class FetchCVEData(BaseTool):
    name = "fetch_cve"
    description = "Fetch CVE data from NVD API using a CVE ID or a keyword."

    def _run(self, query: str):
        # Initialize parameters
        params = {
            'resultsPerPage': 10,  # Limit to 100 results per request
            'startIndex': 0,       # Start from the first result
        }
        if "CVE-" in query:
            # If the query contains a CVE ID, search by ID
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={query}"
        else:
            # Otherwise, treat it as a keyword search
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}"
        
        # url = f"https://services.nvd.nist.gov/rest/json/cves/2.0"  # Main URL for fetching data
        # if "CVE-" in query:
        #     # If the query contains a CVE ID, search by ID
        #     params['cveId'] = query
        # else:
        #     # Otherwise, treat it as a keyword search
        #     params['keywordSearch'] = query


        response = requests.get(url,params=params)
        data = response.json()
        
        # Extract and format the results
        if 'vulnerabilities' in data:
            results = []
            for item in data['vulnerabilities']:
                cve_item = data['vulnerabilities'][0]['cve']
                cve_id = cve_item['id']
                description = cve_item['descriptions'][0]['value']
                cve_metric = cve_item.get('metrics', {})
                results.append(f"{cve_id}: {description} \n Metrics : {cve_metric}")
            return "\n".join(results)
        else:
            return "No CVEs found."

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported")