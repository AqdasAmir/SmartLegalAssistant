from crewai import Task
from agents.case_law_retrieval_agent import case_law_retrieval_agent
from tasks.case_intake_task import case_intake_task
from tasks.ipc_section_task import ipc_section_task

case_law_retrieval_task = Task(
    agent=case_law_retrieval_agent,
    description=(
        "You are provided with a brief legal summary of the issue. Based on this, search for relevant Indian legal precedents.\n\n"
        "Use your tool to retrieve case titles, brief summaries, and links to full judgments. "
        "Only use results from trusted Indian legal sources.\n\n"
        "Now write a single, cohesive, and well-structured paragraph that summarizes the key precedent cases, "
        "explains their importance, and how they relate to the legal issue at hand."
    ),
    expected_output=(
        "A detailed paragraph summarizing the most relevant precedent cases and explaining their legal relevance to the current issue."
        "And link to each case detail"
    ),
    context=[case_intake_task, ipc_section_task]
)