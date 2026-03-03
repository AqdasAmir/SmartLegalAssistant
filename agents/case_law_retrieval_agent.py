from crewai import Agent, LLM
from tools.case_law_retrieval_tool import case_law_retrieval

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
)

case_law_retrieval_agent = Agent(
    role="Legal Precedent Agent",
    goal="Find relevant legal precedent cases based on the user's legal issue.",
    backstory=(
        "You're an expert legal researcher who specializes in finding case law and precedent judgments. "
        "You are skilled in identifying relevant case summaries based on natural language descriptions of legal issues. "
        "Your task is to search trusted legal databases to support legal analysis with past judgments."
    ),
    tools=[case_law_retrieval],
    llm=llm,
    verbose=True,
)