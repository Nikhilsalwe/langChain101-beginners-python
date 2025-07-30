
from langchain_community.llms import OpenAI 

llm = OpenAI(temperature=0.9)

prompt = "What would a good company name for a company that makes colorful socks?"

response = llm.invoke(prompt)  # use .invoke instead of calling as function
print(response) # to get data as string 

result = llm.generate([prompt]*5)

for company_name in result.generations:
    print(company_name[0].text)