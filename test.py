# import chromadb
# import pprint
# from chromadb.config import Settings
# from chromadb.utils import embedding_functions
# from time import sleep
# from embedding import CustomEmbeddingFunction
# from langchain_community.document_loaders import WebBaseLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# pp = pprint.PrettyPrinter(indent=4)

# chroma_client = chromadb.Client()
# default_ef = embedding_functions.DefaultEmbeddingFunction()



# collection = chroma_client.create_collection(name="my_collection11",embedding_function=default_ef)

# with open("test_data/langchain_quickstart.txt") as f:
#     raw_data = f.read()

# # print(raw_data)
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=700,
#     chunk_overlap=70,
#     length_function=len,
#     is_separator_regex=False,
# )


# documents = []
# embeddings = []
# ids = []
# metadata = []
# id = 1
# texts = text_splitter.create_documents([raw_data])
# for text in texts:
#     # print(text.page_content)
#     result = default_ef([text.page_content])
#     # print(result)
#     documents.append(text.page_content)
#     embeddings.append(result)
#     ids.append("id_"+str(id))
#     id = id +1 
    



# collection.add(
#     documents=documents,
#     ids=ids
# )

# results = collection.query(
#     query_embeddings=default_ef(["what is langchain"]),
#     n_results=4
# )
# pp.pprint(results)


