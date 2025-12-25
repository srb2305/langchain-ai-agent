"""
This RAG pipeline performs retrieval strictly from local documents stored in a vector database.
OpenAI is only used for embedding generation, 
not for fetching or searching external knowledge.
"""
from langchain_community.document_loaders import UnstructuredMarkdownLoader, UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Data files for RAG
md_path = "data/guide.md"
pdf_path = "data/report.pdf"

# Load documents: one loader per file type
loader_md = UnstructuredMarkdownLoader(md_path, mode="elements")
loader_pdf = UnstructuredPDFLoader(pdf_path)

docs_md = loader_md.load() # return a list of document object
docs_pdf = loader_pdf.load()

print(f"Loaded {len(docs_md)} markdown documents and {len(docs_pdf)} PDF documents.")


splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=50)
chunks = splitter.split_documents(docs_md + docs_pdf)
print(f"Split into {len(chunks)} text chunks.")

### ----------------------------------------------------------------###

#pip install langchain-chroma chromadb langchain-openai
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 1. Initialize embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# 2. Filter complex metadata from local documents
filtered_chunks = filter_complex_metadata(chunks)

# 3. Create the vectore store using filtered documents
vectore_store = Chroma.from_documents(
    documents=filtered_chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

retriver = vectore_store.as_retriever(search_kwargs={"k":3})

query = "What is Retrieval-Augmented Generation and why is it useful?"
#query = "What is then name of indian PM?"   # will not return any result
docs = retriver.invoke(query)

print(f"Top {len(docs)} retrived document chunks for the query: \n")

for i, doc in enumerate(docs, 1):
    text = doc.page_content.replace("\n", " ")
    print(f"Document {i} snippet: {text[:100]!r} ...")
### ----------------------------------------------------------------###

