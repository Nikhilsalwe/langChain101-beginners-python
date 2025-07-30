import os
from langchain_openai import ChatOpenAI, OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain_experimental.tools.python import PythonAstREPLTool
from langchain.agents.tools import Tool
from langchain.chains.llm_math.base import LLMMathChain
from langchain_core.tools import Tool as CoreTool  # used by new langchain_core-based setup

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["SERPAPI_API_KEY"] = "your-serpapi-key"

# Initialize tools
llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    CoreTool(
        name="Search",
        func=search.run,
        description="Useful for answering questions about current events",
    ),
    CoreTool(
        name="Calculator",
        func=llm_math_chain.run,
        description="Useful for answering math questions",
    ),
]

# Planner and executor
chat_model = ChatOpenAI(temperature=0)

planner = load_chat_planner(chat_model)
executor = load_agent_executor(chat_model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

# Run the agent
result = agent.run(
    "Where will the next summer olympics be hosted? What is the population of that country raised to the 0.43 power?"
)

print(result)
