# cve_utils.py
import requests

def search_cve_database(cve_id):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        'cveId': cve_id
    }
    # params = {
    #     'keyword': query,
    #     'resultsPerPage': 1,
    #     'startIndex': 0
    # }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an error for bad status codes
        data = response.json()
        
        
        # Check if there are CVE items in the response
    #     if 'result' in data and data['result']['CVE_Items']:
    #         cve_item = data['result']['CVE_Items'][0]
    #         cve_id = cve_item['cve']['CVE_data_meta']['ID']
    #         description = cve_item['cve']['description']['description_data'][0]['value']
    #         return f"{cve_id}: {description}"
    #     else:
    #         return "No CVE found for the given query: {cve_id}"
    # except requests.exceptions.RequestException as e:
    #     return f"Error fetching CVE data: {e}"


        if data.get('vulnerabilities'):
            cve_item = data['vulnerabilities'][0]['cve']
            cve_id = cve_item['id']
            description = cve_item['descriptions'][0]['value']
            return f"{cve_id}: {description}"
        else:
            return f"No details found for CVE ID: {cve_id}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching CVE data: {e}"
    
cve_details = search_cve_database("CVE-2020-2022")
print(cve_details)