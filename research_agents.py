import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, ModelSettings, function_tool
from tavily import AsyncTavilyClient
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
external_client = AsyncOpenAI(api_key=os.environ["My_Key"], base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)
tavily_client = AsyncTavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

@function_tool()
async def search(query: str) -> str:
    """Search the web using Tavily API."""
    return str(await tavily_client.search(query))

factfinder_agent = Agent(
    name="FactFinder",
    instructions="Find verified facts for a research subtask, include sources.",
    model=model,
    tools=[search],
    model_settings=ModelSettings(temperature=0.4, max_tokens=3000)
)

sourcechecker_agent = Agent(
    name="SourceChecker",
    instructions="Check reliability of sources and flag conflicts.",
    model=model,
    tools=[search],
    model_settings=ModelSettings(temperature=0.3, max_tokens=3000)
)

research_agents = [factfinder_agent, sourcechecker_agent]
