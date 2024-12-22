import sys
import os
from dotenv import load_dotenv
import openai


from typing import Any
from pydantic import BaseModel, Field
from agency_swarm import BaseTool, Agent, Agency, set_openai_key

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
set_openai_key(api_key)

# Define the custom tool
class NegotiationTool(BaseTool):
    user_proposal: str = Field(
        ..., description="Player's proposal to convince the agent to outsource semiconductor production."
    )

    def run(self):

        return self.generate_response(self.user_proposal)

    def generate_response(self, proposal):
        from openai import completions
        prompt = (
            "You are evaluating proposals to outsource semiconductor production. Engage in meaningful dialogue with the player. "
            "While discussing proposals, occasionally use metaphors or analogies related to hiking (e.g., taking a safe trail, avoiding pitfalls, steady progress) to explain your points. "
            "Focus on dynamic, conversational interactions, and avoid formal or email-like language. Stay true to your priorities: quality, cost, and reliability."
            "You are part of a negotiation game where each agent has its own personality and standards for signing contracts. "
            "Engage in dynamic, conversational interactions with players, ensuring every agent brings their unique perspective and style into the discussions."
            f"\n\nProposal: {proposal}"
        )

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a business owner passionate about hiking, who is looking to outsource semiconductor production with a focus on quality, cost, and reliability. His love for the outdoors influences his decision-making, favoring clarity, steady progress, and avoiding risks."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

class BusinessAgent(Agent):
    def evaluate_proposal(self, proposal: str):
        tool = NegotiationTool(user_proposal=proposal)
        return tool.run()

agent = BusinessAgent(
    name="David",
    description="A business owner passionate about hiking, who is looking to outsource semiconductor production with a focus on quality, cost, and reliability. His love for the outdoors influences his decision-making, favoring clarity, steady progress, and avoiding risks.",
    instructions=(
        "You are evaluating proposals to outsource semiconductor production. Engage in meaningful dialogue with the player. "
        "While discussing proposals, occasionally use metaphors or analogies related to hiking (e.g., taking a safe trail, avoiding pitfalls, steady progress) to explain your points. "
        "Focus on dynamic, conversational interactions, and avoid formal or email-like language. Stay true to your priorities: quality, cost, and reliability."
        "It is a face to face conversation"
    ),
    tools=[NegotiationTool]
)

agency = Agency(
    [agent],
    shared_instructions=(
        "You are part of a negotiation game where each agent has its own personality and standards for signing contracts. "
        "Engage in dynamic, conversational interactions with players, ensuring every agent brings their unique perspective and style into the discussions."
    )
)


def main():
    print("Approach the business owner and convince them to outsource semiconductor production to you. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Thanks for playing.")
            break
        try:
            response = agent.evaluate_proposal(user_input)
            print(f"{agent.name}: {response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

