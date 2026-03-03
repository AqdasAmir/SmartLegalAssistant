from crewai import Crew

from agents.case_intake_agent import case_intake_agent
from agents.ipc_section_agent import ipc_section_agent
from agents.case_law_retrieval_agent import case_law_retrieval_agent
from agents.legal_editor_agent import legal_editor_agent
from tasks.case_intake_task import case_intake_task
from tasks.ipc_section_task import ipc_section_task
from tasks.case_law_retrieval_task import case_law_retrieval_task
from tasks.legal_editor_task import legal_editor_task

legal_assistant_crew = Crew(
    agents=[case_intake_agent, ipc_section_agent, case_law_retrieval_agent, legal_editor_agent],
    tasks=[case_intake_task, ipc_section_task, case_law_retrieval_task, legal_editor_task],
    verbose=True
)