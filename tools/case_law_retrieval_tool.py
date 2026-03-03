import os

from dotenv import load_dotenv
from crewai.tools import tool
from tavily import TavilyClient

load_dotenv()

LEGAL_SOURCES = [
    "indiankanoon.org",
    "aironline.in",
    "lawfinderlive.com"
]

def _is_legal_source(url: str) -> bool:
    """Check if a URL belongs to one of the trusted legal domains."""
    return any(domain in url for domain in LEGAL_SOURCES)


@tool("Case Law Retrieval Tool")
def case_law_retrieval(query: str) -> list[dict]:
    """
    Use Tavily Search to find precedent legal cases for a given legal issue.
    sample tool input: "Home trespassing and theft - precedent cases in India"

    Args:
        query (str): The structured legal issue or case summary.

    Returns:
        list[dict]: Relevant case titles, summaries, and links from trusted Indian legal sources.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError(" 'TAVILY_API_KEY' Not Found")
    
    client = TavilyClient(api_key=api_key)
    
    #Search only trusted legal websites
    search_query = f"site:{' OR site:'.join(LEGAL_SOURCES)} {query}"

    response = client.search(
        query=search_query,
        max_results=10
    )

    raw_results = response.get("results", [])
    legal_results = [
        {
            "title": item.get("title"),
            "summary": item.get("content"),
            "link": item.get("url")
        }
        for item in raw_results
        if _is_legal_source(item.get("url", ""))
    ]

    return legal_results if legal_results else [{
        "title": "No relevant legal precedents found",
        "summary": "No matching results found from trusted Indian legal sources.",
        "link": None
    }]




# testing
# query = "Home trespassing and theft - precedent cases in India"
# results = case_law_retrieval.func(query)
# for r in results:
#     print(r)