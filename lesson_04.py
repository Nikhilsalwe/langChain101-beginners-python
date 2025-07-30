# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_community.llms import OpenAI

# template = "You are a naming consultant for new companies. What is a good name and suggest 5 name for a {company} that makes {product}? and also give me a short description for each name. and mentioned something like here are the interest name of company etc"

# prompt = PromptTemplate.from_template(template)
# llm = OpenAI(temperature=0.9)

# chain = LLMChain(llm=llm, prompt=prompt)

# print(chain.run({'company': "ABC startup", 'product': "colorful socks"}))

#sequentials chain
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature=0)
template = "what is a good name for a company that makes {product}?"

first_prompt = PromptTemplate.from_template(template)
first_chain = LLMChain(llm=llm, prompt=first_prompt)

second_template = "write a catch phrase for the following company: {company_name}"

second_prompt = PromptTemplate.from_template(second_template)
second_chain = LLMChain(llm=llm, prompt=second_prompt)

overall_chain = SimpleSequentialChain(chains=[first_chain, second_chain], verbose=True)

catchPharase = overall_chain.run("colorful socks")
print(catchPharase)
