from langchain_community.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import TextLoader

loader = TextLoader("./state-of-union.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name="state-of-union");

llm =OpenAI(temperature=0)
chain = RetrievalQA.from_chain_type(llm=llm, retriever=store.as_retriever())

print("Answer : ", chain.run("What did biden talk about Ohio?"))
print("Answer 2: ", chain.run("What did biden talk about semi conductor factories where will those build?"))
