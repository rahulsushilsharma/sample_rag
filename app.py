import pprint
import chromadb
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from process_data import scrap_web
import re


pp = pprint.PrettyPrinter(indent=4)
client = chromadb.PersistentClient(path="chroma_db")
default_ef = embedding_functions.DefaultEmbeddingFunction()
collection = client.get_or_create_collection("langchain",embedding_function=default_ef)
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=30,
    length_function=len,
    is_separator_regex=False,
    )



def prepare_data(text_splitter, raw_data):
    texts = text_splitter.create_documents([raw_data])
    return texts


def save_to_database( splitted_chunks,metadata, embeddings=None):
    ids = []
    metadatas = []
    documents = []
    id = 1
    print(metadata)
    for chunk in splitted_chunks:
        ids.append("id_"+str(id))
        id = id +1 
        metadatas.append(metadata)
        documents.append(chunk.page_content)
    
    if(embeddings):
        collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    else:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
    
 
def run():
    urls = [
        'https://www.hindustantimes.com/education/news/iit-hyderabad-to-host-the-second-edition-of-r-d-innovation-fair-iinventiv-101704460769704.html'
    ]
    for url in urls:
        print(url)
        
        raw_data =  scrap_web(url)
        # print(raw_data.page_content)
        splitted_chunks = prepare_data(recursive_splitter, raw_data.page_content)
        pp.pprint(splitted_chunks)
        # embeddings = genrate_embeddings([splitted_chunks])
        save_to_database(splitted_chunks,raw_data.metadata)
        print('+================================== DATA SAVED =======================================+')
        
        
# run()

querry = "give me information on Ministry of Education's at flagship event IInvenTiv-2024 "
print(default_ef([querry]))
# results = collection.query(
#     query_embeddings=default_ef([querry]),
#     n_results=4
# )
# # pp.pprint(results)
# context = ''
# for result in results["documents"][0]:
    
#     context  = context + result + '\n'
#     pp.pprint(re.sub(r'\n+', '\n', result))
#     print('________________________________________________________________________________________________________')
        
# context = re.sub(r'\n+', '\n', context)
# prompt = f"""
#         With the following context 
#         `{context}`
        
#         response to the querry
#         `{querry}`
# """
        
# import requests

# url = 'http://localhost:3000/api/data'



# data = {'message': prompt}
# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, json=data, headers=headers)

# if response.status_code == 200:
#     res = response.json()
#     # print(f'Success! Server response: {response.json()}')
#     print('________________________________________________________________________________________________________')
#     pp.pprint(res["message"])
#     print('________________________________________________________________________________________________________')
#     pp.pprint(res["response"])
    
    
# else:
#     print(f'Error! Server response: {response.status_code} - {response.text}')
