import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from time import sleep
from embedding import CustomEmbeddingFunction
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



api_path = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-mpnet-base-v2"
api_key = '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'


default_ef = embedding_functions.DefaultEmbeddingFunction()


huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key=api_key,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="chroma_db")

embedding_function = CustomEmbeddingFunction(api_path, api_key)
collection = client.get_or_create_collection("test2",embedding_function=default_ef)

# loader = WebBaseLoader("https://python.langchain.com/docs/get_started/quickstart")

# docs = loader.load()
# print(docs[0].page_content)

# with open("test_data/langchain_quickstart.txt") as f:
#     raw_data = f.read()


# # print(raw_data)
# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=700,
#     chunk_overlap=70,
#     length_function=len,
#     is_separator_regex=False,
# )


# documents = []
# embeddings = []
# ids = []
# metadata = []
# id = 1;
# texts = text_splitter.create_documents([raw_data])
# for text in texts:
#     print(text.page_content)
#     # sleep(2)
#     # result = embedding_function.generate(text.page_content)
#     result = default_ef([text.page_content])
#     print(result)
#     # break
#     documents.append(text.page_content)
#     embeddings.append(result)
#     ids.append("id_"+str(id))
#     id = id +1 
    


# collection.add(
#     embeddings=embeddings,
#     documents=documents,
#     ids=ids
# )


# texts_to_generate = "text1"
# result = embedding_function.generate(texts_to_generate)
# print(result)


# collection.add(
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

results = collection.query(
    query_embeddings=default_ef(["what is langchain"]),

    # query_texts=["what is langchain"],
    n_results=2
)
print(results)

# val = default_ef(["foo"])
# print(val)


