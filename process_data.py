import pprint
from langchain_community.document_loaders import WebBaseLoader



# loader = WebBaseLoader("https://python.langchain.com/docs/get_started/quickstart")

# pp = pprint.PrettyPrinter(indent=4)


# print(docs[0].page_content)



def scrap_web(url:str):
    loader = WebBaseLoader(url)
    return loader.load()[0]


def parse_urls(urls, save=False) -> list:
    documents = []
    for url in urls:
        data = scrap_web(url)
        documents.append(data)
        if(save):
            save_doc_to_txt(data.page_content, data.metadata.title)
    return documents



def save_doc_to_txt(data:str, title:str)->None:
    file = open(title, 'a')
    file.write(data)
    file.close()






def prepare_data(text_splitter, raw_data):
    
    texts = text_splitter.create_documents([raw_data])




# TODO : create a db to preserve metadata while saving localy
def save_metadata(metadata):
    pass


