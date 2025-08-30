import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, ModelSettings
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
external_client = AsyncOpenAI(api_key=os.environ["My_Key"], base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)

synthesizer_agent = Agent(
    name="Synthesizer",
    instructions="Combine all research results into structured insights with citations.",
    model=model,
    model_settings=ModelSettings(temperature=0.5, max_tokens=4000)
)
