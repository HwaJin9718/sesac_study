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

load_dotenv()

# 1. 문서 로딩
document1 = TextLoader('./nvme.txt', encoding='utf-8').load()
document2 = TextLoader('./ssd.txt', encoding='utf-8').load()
# print(documents)

# 2. 문서를 청크(chunk) 단위로 짜르기
# 1000개 token 단위로 자른다 단, 자를때 200개 token은 겹치게 (1000/200) or (2000/500)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
texts1 = text_splitter.split_documents(document1)
texts2 = text_splitter.split_documents(document2)
# print(text)

# 필요 시 추가적인 메타데이터를 추가해서 '출처' 등을 명시할 때 사용
# documents = [Document(page_content=doc.page_content, metadata={'source': 'nvme.txt'}) for doc in documents]
for i, doc in enumerate(texts1, start=1):
    doc.metadata.update({'chunk_id': i, 'created_date' : '2025-08-08'})
for i, doc in enumerate(texts2, start=1):
    doc.metadata.update({'chunk_id': i, 'created_date' : '2025-08-08'})

# 모든 청크 합치기
texts = texts1 + texts2

# 3. 임베딩 하기
# 백터 공간에 찍기
embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')
# print(store)

# 4.실제로 질문할 준비
# RAG모델은 temperature를 낮추는게 일반적!! temperature=0.2
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2) 

# search_kwargs={'k':3} -> 유사도 기준 상위 3개의 문서를 고르시오
retriever = store.as_retriever(search_kwargs={'k':5}) 

template = '''
다음 내용을 바탕으로 질문에 답변해주세요. 해당 문서에 내용이 없을 경우, 모른다고 답변해주세요.
참고문서 : {context}

질문 : {question}

답변을 작성하고, 마지막에 참고한 문서의 "출처: [파일명:청크번호]" 형식으로 참고한 문서 정보를 명시해 주세요.
예시) 출처: nvme.txt:1, ssd.txt:3
출처 내에 답변이 없을 경우 출처에 "없음" 이라고 명시해주세요.
'''

prompt = ChatPromptTemplate.from_template(template)

# 체인 구성
# RunnablePassthrough : 사용자 질문은 question에 담아서 그대로 넘어감
# context 는 retriever로 부터 추출해서 {context} 라는 공간에 채워줄 예정
# 프롬프트 -> LLM -> 응답
chain = {'context' : retriever, 'question' : RunnablePassthrough()} | prompt | llm | StrOutputParser()

def answer_question(question):
    print('-' * 50)
    print(f"Q : {question}")
    response = chain.invoke(question)
    print(f"A : {response}")
    return response

def debug_retrivelal(question):
    retrieved_docs = retriever.invoke(question)
    print('-' * 50)
    print(f"Q : {question}")
    print(f"검색된 문서 개수 : {len(retrieved_docs)}")

    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"\n--- 문서 {i} ---")
        print(f"출처: {doc.metadata}")
        print(f"내용 (처음 200자): {doc.page_content[:200]}...(중략)")
        if hasattr(doc, 'score'): # 문서에 유사도 점수가 있을 경우
            print(f'유사도 점수: {doc.score}')
    print('=' * 50)


# question1 = 'NVME와 SATA의 차이점을 100글자로 요약해 주세요.'
# answer_question(question1)

# question2 = 'PCIe는?'
# answer_question(question2)

# question3 = '우주의 크기는 얼마나 되나요?'
# answer_question(question3)

question4 = 'PCIe는?'
debug_retrivelal(question4)
