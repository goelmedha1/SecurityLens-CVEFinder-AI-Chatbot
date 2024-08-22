# import os
# from openai import OpenAI
# from django.conf import settings
# from .cve_utils import search_cve_database
# from .cve_utils import search_cve_by_product

# # Initialize the OpenAI client with your API key
# client = OpenAI(api_key=settings.OPENAI_API_KEY)


# def get_chatgpt_response(prompt):
#     try:
#         #Fetch CVE data based on user prompt
#         if 'Windows' in prompt or 'Linux' in prompt or 'MacOS' in prompt:
#             cve_info = search_cve_by_product(prompt)
#         else:
#             cve_info = search_cve_database(prompt)
#         #with_raw_response
#         # Create a chat completion with the given prompt
#         response = client.chat.completions.with_raw_response.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "user", "content": prompt},
#                 {"role": "assistant", "content": f"Here's what I found about {prompt}: {cve_info}."}
#                 #content: 
#             ],
            
#         )

#         # Parse the response to extract the completion data
#         completion = response.parse()
        
#         # Extract the message content from the response
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error: {e}"




# # Initialize the OpenAI client with your API key
# client = OpenAI(api_key=settings.OPENAI_API_KEY)




