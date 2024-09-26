#langchain_chatbot.py

import os
from langchain_openai import ChatOpenAI
# from langchain.chains import SimpleChain
# from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from .cve_utils import FetchCVEData
from langchain.tools import Tool
from .ComplexQuery import ComplexQueryHandlerTool 
from .nmap_tool import NmapScanTool   #Import the nmap tool

# Initialize the language model
SECRET_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key = SECRET_KEY,model_name="gpt-4",temperature= 0.2)

fetch_cve_tool = FetchCVEData()
complex_query_handler_tool = ComplexQueryHandlerTool()
nmap_scan_tool = NmapScanTool()

# Initialize the agent with multiple tools
agent = initialize_agent(
    tools=[fetch_cve_tool, complex_query_handler_tool, nmap_scan_tool],
    llm=llm,
    agent="zero-shot-react-description",
    handle_parsing_errors=True
)

def get_chatgpt_response(prompt):
    # Initialize the FetchCVEData tool
    # fetch_cve_tool = FetchCVEData()
    
    # # Define additional agents if necessary for more complex queries
    # additional_tool = Tool(
    #     name="complex_query_handler",
    #     func=lambda x: "Handling complex queries is not yet implemented.",  # Placeholder for future tools
    #     description="Handles more complex queries if needed."
    # )

    # # Initialize the agent with multiple tools
    # agent = initialize_agent(
    #     tools=[fetch_cve_tool, additional_tool], 
    #     llm=llm, 
    #     agent="zero-shot-react-description", 
    #     handle_parsing_errors=True
    # )
    
    try:
        # Run the agent with the provided prompt
        response = agent.run(prompt)

         # Ensure that the response from the agent uses the actual data fetched
        if "No CVEs found" in response:
            return "Sorry, I couldn't find any CVEs matching your query."
        return response  # Return the AI's response with real data
        #return response  # Return the AI's response
    except Exception as e:
        # Log or handle the exception appropriately
        return f"Error: {e}"