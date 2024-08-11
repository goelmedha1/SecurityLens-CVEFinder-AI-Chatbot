import os
from openai import OpenAI
from django.conf import settings
from .cve_utils import search_cve_database

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_chatgpt_response(prompt):
    try:
        # Fetch CVE data based on user prompt
        cve_info = search_cve_database(prompt)
        #with_raw_response
        # Create a chat completion with the given prompt
        response = client.chat.completions.with_raw_response.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please provide information about {prompt}."},
                {"role": "assistant", "content": f"Here's what I found about {prompt}: {cve_info}."}
            ],
            
        )

        # Parse the response to extract the completion data
        completion = response.parse()
        
        # Extract the message content from the response
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"




# # Initialize the OpenAI client with your API key
# client = OpenAI(api_key=settings.OPENAI_API_KEY)
