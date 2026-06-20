from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from tavily import TavilyClient

load_dotenv()


tavily_client = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Searches the web for the given query and returns the results.
    
    Args:
        query (str): The search query.
    returns:
        str: The search results.    
    """
    print(f"Searching for: {query}")
    return tavily_client.search(query=query)


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from react-search-engine!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for AI engineer job using \
        langchain in South Africa on LinkedIn and list their details")]})

    print(result)

if __name__ == "__main__":
    main()
