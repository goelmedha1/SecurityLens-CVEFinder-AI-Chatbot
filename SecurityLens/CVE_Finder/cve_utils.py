# cve_utils.py
import requests

def search_cve_database(cve_id):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        'resultsPerPage': 10,
        'startIndex':0,
        'cveId': cve_id,
        
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an error for bad status codes
        data = response.json()


        if data.get('vulnerabilities'):
            cve_item = data['vulnerabilities'][0]['cve']
            cve_id = cve_item['id']
            description = cve_item['descriptions'][0]['value']
            cve_metric = cve_item.get('metrics', {})
            return f"{cve_id}: {description} \n Metrics : {cve_metric}"
        else:
            return f"No details found for CVE ID: {cve_id}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching CVE data: {e}"
    
# cve_details = search_cve_database("CVE-2020-2020")
# print(cve_details)
    

def search_cve_by_product(keyword_search):

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    
    params = {

        'keywordSearch': keyword_search,
        'startIndex': 0,
        'resultsPerPage': 10

    }

    try:
        response = requests.get(url, params = params)
        response.raise_for_status()
        data = response.json()

        cve_results = []

        # write code here



    except requests.exceptions.RequestException as e:
        return f"Error fetching CVE data: {e}"




