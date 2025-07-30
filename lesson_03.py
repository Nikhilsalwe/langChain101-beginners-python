# prompt template and chaining 
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI

template = "You are a naming consultant for new companies. What is a good name and suggest 5 name for a company that makes {product}? and also give me a short description for each name. and mentioned something like here are the interest name of company etc"

prompt = PromptTemplate.from_template(template)
llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))

