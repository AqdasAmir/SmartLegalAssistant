import os

from dotenv import load_dotenv
from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


@tool("IPC Search Tool")
def search_ipc(query: str) -> list[dict]:
     """
    Search IPC vector database for sections relevant to the input query.

    Args:
        query (str): User query in natural language.

    Returns:
        list[dict]: List of matching IPC sections with metadata and content.
    """
     load_dotenv()

     persist_dir = os.getenv("VECTORDB_PATH")
     if not persist_dir:
          raise EnvironmentError("VectorDB path not found")
     
     persist_dir_path = os.getenv("VECTORDB_PATH")
     collection_name = os.getenv("IPC_COLLECTION_NAME")

     embedding_function = HuggingFaceEmbeddings()

     vector_db = Chroma(
          collection_name=collection_name,
          persist_directory=persist_dir_path,
          embedding_function=embedding_function
     )


     docs = vector_db.similarity_search(query,k=3)

     return [
          {
              "section": doc.metadata.get("section"),
            "section_title": doc.metadata.get("section_title"),
            "chapter": doc.metadata.get("chapter"),
            "chapter_title": doc.metadata.get("chapter_title"),
            "content": doc.page_content 
          }
          for doc in docs
     ]


# testing

# query = "What is the IPC section for Theft?"
# results = search_ipc.func(query)
# for r in results:
#     print(r)