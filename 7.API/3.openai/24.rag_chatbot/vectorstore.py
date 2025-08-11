import os
from dotenv import load_dotenv

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

# 필요한 글로벌 변수 선언
VECTOR_DB = './chroma_db'
COLLECTION_NAME = 'data_hub'
store = None

# 프롬프트 작성, LLM 호출, 체인 생성
# llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2)

# template = '''
# 주어진 문서 내용을 바탕으로 질문에 답변해주세요.
# 모든 답변은 제공된 문서내용을 기반으로만 답변하고, 정보가 없을 경우 없다고 답변하세요.

# 문서내용 : {context}

# 질문 : {question}
# '''

# prompt = ChatPromptTemplate.from_template(template)
# chain = ({'context': RunnablePassthrough(), 'question': RunnablePassthrough()}) | prompt | llm | StrOutputParser()

def get_store():
    return store


# def initialize_vector_db():
    
#     # 이전 DB가 있을 경우 로딩
#     if os.path.exists(VECTOR_DB):
#         print('VECTOR DB 로딩...')
#     # 디렉토리 생성
#     else:
#         print('VECTOR DB 폴더 생성...')
#         os.makedirs(VECTOR_DB, exist_ok=True)


# 강사님꺼
def initialize_vector_db():
    global store
    
    # 이전 DB가 있을 경우 로딩
    if os.path.exists(VECTOR_DB) and os.listdir(VECTOR_DB):
        store = Chroma(collection_name=COLLECTION_NAME, embedding_function=OpenAIEmbeddings(), persist_directory=VECTOR_DB)
    # 디렉토리 생성
    else:
        os.makedirs(VECTOR_DB, exist_ok=True)

    return True


# def create_vector_db(file_path):
#     # 백터 DB 생성

#     # 1. 파일 가져온다
#     loader = PyPDFLoader(file_path)
#     pages = loader.load()
#     # print(pages)

#     # 2. 문서 분할
#     text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#         separator='\n\n', # 문서 분할 기준 (단락)
#         chunk_size=2000, # 단락이 너무 길면 안되니 최대 2000 token
#         chunk_overlap=500, # 중복 500 token 포함
#     )

#     texts = text_splitter.split_documents(pages)
#     # print(texts[10])

#     # 3. 임베딩 진행
#     embeddings = OpenAIEmbeddings()
#     store = Chroma.from_documents(texts, embeddings, collection_name=COLLECTION_NAME, persist_directory=VECTOR_DB)

#     return store


# 강사님꺼
def create_vector_db(file_path):
    # 백터 DB 생성
    global store

    # 1. 파일 가져온다
    documents = PyPDFLoader(file_path).load()

    # 경로 제외하고 파일명만 남기기
    # ./DATA 지우기
    for doc in documents:
        doc.metadata['source'] = os.path.basename(file_path) 

    # 2. 문서 분할
    texts = CharacterTextSplitter(
        chunk_size=100, # 500 token
        chunk_overlap=20, # 중복 100 token 포함
    ).split_documents(documents)

    # 3. 임베딩 진행
    embeddings = OpenAIEmbeddings()

    if store:
        store.add_documents(texts)
    else:
        store = Chroma.from_documents(texts, embedding=embeddings, collection_name=COLLECTION_NAME, persist_directory=VECTOR_DB)

    print('백터 DB가 정상적으로 생성되었습니다.')
    return store


def load_vector_db():

    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=VECTOR_DB)

    return store


def delete_file_from_vector(filename):

    # NoSQL 기반의 DB에서 자료 삭제하는것과 동일 (예. mongodb)
    store._collection.delete(where={'source': filename})

    # 백터 DB가 persist 옵션이 켜져 있으면? 저장..
    if hasattr(store, 'persist'):
        store.persist()

