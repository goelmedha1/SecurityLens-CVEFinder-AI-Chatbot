from langchain.tools import BaseTool
from .cve_utils import FetchCVEData



# Define additional tools for complex query handling
class ComplexQueryHandlerTool(BaseTool):
    name = "complex_query_handler"
    description = "Handles complex queries involving multiple filters, severity levels, and specific technologies."

    def _run(self, query: str):
        # Custom logic to parse and handle complex queries
        # Example: Filter CVEs by OS, severity, and other criteria
        # Parse the query and route to FetchCVEData with appropriate parameters
        if "severity" in query.lower() and "windows" in query.lower():
            # Logic to fetch CVEs specifically for Windows with severity filtering
            return FetchCVEData()._run(f"{query}")
        else:
            return "This tool currently supports queries involving specific OS and severity combinations."

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported")