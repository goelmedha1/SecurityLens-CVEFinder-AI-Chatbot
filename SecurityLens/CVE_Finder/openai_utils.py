from openai import OpenAI
from django.conf import settings
import requests

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def search_cve_database(query):
    url = "https://www.cve.org/" # !!!! Change this 
    params = {
        'keyword': query,
        'resultsPerPage': 1,
        'startIndex': 0
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get('result', {}).get('CVE_Items'):
            cve_item = data['result']['CVE_Items'][0]
            cve_id = cve_item['cve']['CVE_data_meta']['ID']
            description = cve_item['cve']['description']['description_data'][0]['value']
            return f"{cve_id}: {description}"
        else:
            return "No CVE found for the given query."
    except requests.exceptions.RequestException as e:
        return f"Error fetching CVE data: {e}"

def get_chatgpt_response(prompt):
    try:
        # Fetch CVE data based on user prompt
        cve_info = search_cve_database(prompt)
        
        # Create a chat completion with the given prompt
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": cve_info}
            ],
            model="gpt-3.5-turbo",
        )

        # Parse the response to extract the completion data
        completion = response.parse()
        
        # Extract the message content from the response
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


# Initialize the OpenAI client with your API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)
