import pprint
from langchain import llms
from langchain.llms import OpenAI
from langchain.agents import agent, get_all_tool_names, initialize_agent, load_tools  # ✅ Correct import path

prompt = "what was the 3rd president of the United States born? what is that year raised to the power of 3?"

llms = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llms)

agent = initialize_agent(tools, llms, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)

> Entering new AgentExecutor chain...
 I should use the wikipedia tool to find the birth year of the 3rd president of the United States and then use the Calculator tool to raise that year to the power of 3.
Action: wikipedia
Action Input: 3rd president of the United States
Observation: Page: Thomas Jefferson
Summary: Thomas Jefferson (April 13 [O.S. April 2], 1743 – July 4, 1826) was an American Founding Father and the third president of the United States from 1801 to 1809. He was the primary author of the Declaration of Independence. Jefferson was the nation's first U.S. secretary of state under George Washington and then the nation's second vice president under John Adams. Jefferson was a leading proponent of democracy, republicanism, and natural rights, and he produced formative documents and decisions at the state, national, and international levels.
Jefferson was born into the Colony of Virginia's planter class, dependent on slave labor. During the American Revolution, Jefferson represented Virginia in the Second Continental Congress, which unanimously adopted the Declaration of Independence. Jefferson's advocacy for individual rights, including freedom of thought, speech, and religion, helped shape the ideological foundations of the revolution and inspired the Thirteen Colonies in their revolutionary fight for independence, which culminated in the establishment of the United States as a free and sovereign nation.
Jefferson served as the second governor of revolutionary Virginia from 1779 to 1781. In 1785, Congress appointed Jefferson U.S. minister to France, where he served from 1785 to 1789. President Washington then appointed Jefferson the nation's first secretary of state, where he served from 1790 to 1793. In 1792, Jefferson and political ally James Madison organized the Democratic-Republican Party to oppose the Federalist Party during the formation of the nation's First Party System. Jefferson and Federalist John Adams became both personal friends and political rivals. In the 1796 U.S. presidential election between the two, Jefferson came in second, which made him Adams' vice president under the electoral laws of the time. Four years later, in the 1800 presidential election, Jefferson again challenged Adams and won the presidency. In 1804, Jefferson was reelected overwhelmingly to a second term.
Jefferson's presidency assertively defended the nation's shipping and trade interests against Barbary pirates and aggressive British trade policies, promoted a western expansionist policy with the Louisiana Purchase, which doubled the nation's geographic size, and reduced military forces and expenditures following successful negotiations with France. In his second presidential term, Jefferson was beset by difficulties at home, including the trial of his former vice president Aaron Burr. In 1807, Jefferson implemented the Embargo Act to defend the nation's industries from British threats to U.S. shipping, limit foreign trade, and stimulate the birth of the American manufacturing.
Jefferson is ranked among the upper tier of U.S. presidents by both scholars and in public opinion. Presidential scholars and historians have praised Jefferson's advocacy of religious freedom and tolerance, his peaceful acquisition of the Louisiana Territory from France, and his leadership in supporting the Lewis and Clark Expedition. They acknowledge his lifelong ownership of large numbers of slaves, but offer varying interpretations of his views on and relationship with slavery.



Page: List of presidents of the United States by home state
Summary: These lists give the states of birth and of primary affiliation for each president of the United States.

Page: President pro tempore of the United States Senate
Summary: The president pro tempore of the United States Senate (often shortened to president pro tem) is the second-highest-ranking official of the United States Senate, after the vice president. According to Article One, Section Three of the United States Constitution, the vice president of the United States is the president of the Senate (despite not being a senator), and the Senate must choose a president pro tempore to act in the vice president's absence.
The president pro tempore is elected by the Senate as a whole, usua
Thought: Now that I have the birth year of Thomas Jefferson, I can use the Calculator tool to raise it to the power of 3.
Action: Calculator
Action Input: 1743
Observation: Answer: 1743
Thought: I now know the final answer.
Final Answer: 1743

> Finished chain.