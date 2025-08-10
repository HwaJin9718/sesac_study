from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# 외부 라이브러리를 불러오기 위한 langchain 라이브러리 : pip install langchain-community 
# 백터 DB: pip install chromadb
from langchain_community.vectorstores import Chroma

load_dotenv()

# 1. 문서 로딩
loader = TextLoader('./nvme.txt', encoding='utf-8')
documents = loader.load()
# print(documents)

# 2. 문서를 청크(chunk) 단위로 짜르기
# 1000개 token 단위로 자른다 단, 자를때 200개 token은 겹치게 (1000/200) or (2000/500)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
texts = text_splitter.split_documents(documents)
# print(text)

# 3. 임베딩 하기
# 백터 공간에 찍기
embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')
# print(store)

# 4.실제로 질문할 준비
# RAG모델은 temperature를 낮추는게 일반적!!
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2) 

retriever = store.as_retriever()

template = '''
다음 내용을 바탕으로 질문에 답변해주세요.
{context}

질문 : {question}
'''

prompt = ChatPromptTemplate.from_template(template)

# 체인 구성
# RunnablePassthrough : 사용자 질문은 question에 담아서 그대로 넘어감
# context 는 retriever로 부터 추출해서 {context} 라는 공간에 채워줄 예정
# 프롬프트 -> LLM -> 응답
chain = {'context' : retriever, 'question' : RunnablePassthrough()} | prompt | llm

question = 'NVME와 SATA의 차이점을 100글자로 요약해 주세요.'
response = chain.invoke(question)

print(response.content)

# 6. 확인작업 -> 실제로는 할 필요 없음!
# context_docs = retriever.invoke(question)
# print('----- 검색된 문서는 -----')
# # print(context_docs) # 전체가 통으로 보여짐 (구분이 좀 어려움)
# for i, doc in enumerate(context_docs, start=1): # for 문으로 1개씩 나눠져 보여짐
#     print(f"[== {i} ==] {doc.page_content}")
