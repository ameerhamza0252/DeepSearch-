import os
from dotenv import load_dotenv,find_dotenv
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, ModelSettings

load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
external_client = AsyncOpenAI(
    api_key=os.environ["My_Key"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

planner_agent = Agent(
    name="Planner",
    instructions="Break complex research questions into 2-6 clear subtasks as JSON.",
    model=model,
    model_settings=ModelSettings(temperature=0.2, max_tokens=2000)  # increased tokens
)
