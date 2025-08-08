from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# 외부 라이브러리를 불러오기 위한 langchain 라이브러리 : pip install langchain-community 
# 백터 DB: pip install chromadb
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
# langchain 과 chroma를 연결하는 라이브러리 : pip install langchain-chroma
from langchain_chroma import Chroma

load_dotenv()

PERSIST_DIR = './chroma_db'

# 새롭게 문서 로딩 함수
def create_vechor_db():
    # 1. 문서 로딩
    loader = TextLoader('./nvme.txt', encoding='utf-8')
    documents = loader.load()

    # 2. 문서를 청크(chunk) 단위로 짜르기
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
    texts = text_splitter.split_documents(documents)

    # 3. 임베딩 하기
    embeddings = OpenAIEmbeddings()
    store = Chroma.from_documents(texts, embeddings, collection_name='nvme', persist_directory=PERSIST_DIR)

    return store

# 해당 문서가 있으면 로딩
def load_vector_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name='nvme', embedding_function=embeddings, persist_directory=PERSIST_DIR)

    return store

import os
if os.path.exists(PERSIST_DIR):
    print('이전 DB를 로딩 중입니다.')
    store = load_vector_db()
else:
    print('이전 DB가 없어, 새로 생성중입니다.')
    store = create_vechor_db()

print('DB 준비가 완료되었습니다.')

# 4.실제로 질문할 준비
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2) 

retriever = store.as_retriever()

template = '''
다음 내용을 바탕으로 질문에 답변해주세요.
{context}

질문 : {question}
'''

prompt = ChatPromptTemplate.from_template(template)

# 체인 구성
chain = {'context' : retriever, 'question' : RunnablePassthrough()} | prompt | llm

question = 'NVME와 SATA의 차이점을 100글자로 요약해 주세요.'
response = chain.invoke(question)

print(response.content)

