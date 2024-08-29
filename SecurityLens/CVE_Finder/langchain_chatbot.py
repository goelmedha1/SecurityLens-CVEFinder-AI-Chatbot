#langchain_chatbot.py

import os
from langchain_openai import ChatOpenAI
# from langchain.chains import SimpleChain
# from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from .cve_utils import FetchCVEData

SECRET_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key = SECRET_KEY,model_name="gpt-4",temperature= 0.1)

def get_chatgpt_response(prompt):
# llm = OpenAI(model_name="text-davinci-003")
    fetch_cve_tool = FetchCVEData()

    agent = initialize_agent(tools=[fetch_cve_tool], llm=llm, agent="zero-shot-react-description")
    
    response = agent.run(prompt)
    return response  # Return the AI's response
    #print(response)