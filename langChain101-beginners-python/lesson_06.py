from langchain.llms import OpenAI
from langchain.agents import agent, initialize_agent, load_tools  # ✅ Correct import path

prompt = "what is the surname name of my friend Swastik?"

llms = OpenAI(temperature=0)
tools = load_tools(["human"])

agent = initialize_agent(tools, llms, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)