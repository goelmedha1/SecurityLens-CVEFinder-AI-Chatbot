import os
from django.conf import settings
from langchain import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from decouple import config
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_core.messages import AIMessage
from .cve_utils import search_cve_database, search_cve_by_product

# Initialize the OpenAI client using LangChain with your API key
# openai_client = ChatOpenAI(openai_api_key = SECRET_KEY)

def get_chatgpt_response(prompt):
    SECRET_KEY = config("OPENAI_API_KEY")
    chat = ChatOpenAI(openai_api_key = SECRET_KEY)

    try:

        #get cve data based on user prompt
        if 'Windows' in prompt or 'Linux' in prompt or 'MacOS' in prompt:
            cve_info = search_cve_by_product(prompt)
        
        else:
            cve_info = search_cve_database(prompt)

        
        #Use templates from Langchain to chat with AI

        system_message = SystemMessagePromptTemplate.from_template("Your name is SecurityLens and you are here to provide information about CVE's."
                                                                   "You were developed by two graduate students, Medha Goel and Swati Agrawal at Umass Amherst")
                                                                   
        human_message = HumanMessagePromptTemplate.from_template('{prompt}')
        ai_message = AIMessage(content = f"Here what I found about {prompt}: {cve_info}.")
        chat_prompt = ChatPromptTemplate.from_messages([
            system_message, human_message, ai_message
        ]
        )

        formatted_chat_prompt = chat_prompt.format_messages(prompt = prompt)

        #print(formatted_chat_prompt)


        response = chat.invoke(formatted_chat_prompt)

        return response.content

    except Exception as e:
        return f"Error: {e}"
