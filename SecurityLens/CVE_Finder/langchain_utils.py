import os
from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage
from decouple import config
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_core.messages import AIMessage
from .cve_utils import search_cve_database, search_cve_by_product



# # Initialize the OpenAI client using LangChain with your API key
# #chat = ChatOpenAI(openai_api_key = SECRET_KEY)

def get_chatgpt_response(prompt):
    SECRET_KEY = config("OPENAI_API_KEY")
    chat = ChatOpenAI(openai_api_key = SECRET_KEY, temperature= 0.2)

    try:

        #get cve data based on user prompt
        # if 'Windows' in prompt or 'Linux' in prompt or 'MacOS' in prompt:
        #     cve_info = search_cve_by_product(prompt)
        
        # else:
        #     cve_info = search_cve_database(prompt)

    

#         # Determine if the prompt is a CVE ID or a keyword search
        if prompt.startswith("CVE-"):
            # Treat it as a CVE ID and use search_cve_database
            cve_info = search_cve_database(prompt)
        else:
            # Treat it as a keyword search and use search_cve_by_product
            cve_info = search_cve_by_product(prompt)
        
        # Check if the cve_info was fetched correctly
        if "Error" in cve_info or "No CVEs found" in cve_info:
            return cve_info  # Return the error or no CVE found message directly
        #Use templates from Langchain to chat with AI

        system_message = SystemMessagePromptTemplate.from_template("You are an intelligent AI. Your name is SecurityLens and you are here to provide information about CVE's."
                                                                   "You were developed by two graduate students, Medha Goel and Swati Agrawal at Umass Amherst."
                                                                   )
                                                                   
        human_message = HumanMessagePromptTemplate.from_template("Please provide information about the following: {prompt}")
        ai_message = AIMessage(content = f"Here what I found about {prompt}: {cve_info}.")
        chat_prompt = ChatPromptTemplate.from_messages([
            system_message, human_message, ai_message,
        ]
        )
        chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message, ai_message])
        
        formatted_chat_prompt = chat_prompt.format_messages(prompt = prompt)

        #print(formatted_chat_prompt)


        response = chat.invoke(formatted_chat_prompt)

        return response.content
        #return f"Here is the information I found: {cve_info}"
            
    

    except Exception as e:
        return f"Error: {e}"


