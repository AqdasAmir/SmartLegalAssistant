from dotenv import load_dotenv
from crew import legal_assistant_crew

load_dotenv()

def run(user_input: str):
    result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

    print("-"*50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    user_input = (
        "I was walking on the footpath when a speeding bike hit me from behind. "
        "The rider was drunk and not wearing a helmet. "
        "I suffered a fracture in my leg and my phone was destroyed. "
        "Bystanders caught him, but he is claiming it was an accident. "
        "What charges apply for drunk driving and causing injury?"
    )

    run(user_input)