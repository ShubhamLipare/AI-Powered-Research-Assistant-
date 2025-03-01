from src.ingestion import load_data
from src.ingestion import chunk_data
from src.utils import filepath
from src.retriever.vectorstore import VectorStore


def main():

    text=load_data.load_pdf(filepath)
    with open("data/text.csv","w", encoding="utf-8") as file:
        file.write(text)

    chunks=chunk_data.split_data(text)
    
    vectore_store=VectorStore()
    doc=vectore_store.add_text(texts=chunks)




if __name__=="__main__":
    main()