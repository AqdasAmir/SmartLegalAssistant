from crewai import Task
from agents.legal_editor_agent import legal_editor_agent
from tasks.case_law_retrieval_task import case_law_retrieval_task
from tasks.case_intake_task import case_intake_task
from tasks.ipc_section_task import ipc_section_task

legal_editor_task = Task(
    agent= legal_editor_agent,
    context=[case_intake_task, ipc_section_task, case_law_retrieval_task],
    description=(
        """
        Take the raw legal research provided by the Researcher (including IPC sections and Case Laws).
        
        Your job is NOT to do new research, but to reorganize the existing information into a 
        client-friendly format.
        
        1. Review the retrieved IPC sections.
        2. Review the retrieved Precedent Cases.
        3. Format them using Markdown as requested in the expected output.
        4. Add a polite concluding sentence advising the client to consult a human lawyer.
        """
        ),
    expected_output=(
        """
        A beautifully formatted Markdown response that follows this structure:

        # Legal Opinion Summary
        
        "A detailed paragraph explaining the user importance and consequence of the current issue."

        ## 1. Applicable Legal Sections
        * **[Section Number]**: [Brief description of what this section covers]
        * **[Section Number]**: [Brief description]

        ## 2. Relevant Precedent Cases
        * **[Case Name]**: [detailed summary of the precedent case followed by link to case detail]
        * **[Case Name]**: [detailed summary of the precedent case followed by link to case detail]

        ## 3. Conclusion
        [A brief summary of how these laws apply to the user's specific situation]
        """
    )
)