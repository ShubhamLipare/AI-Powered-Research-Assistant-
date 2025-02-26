from src.ingestion import load_data
from src.ingestion import chunk_data
from src.utils import filepath

def main():

    text=load_data.load_pdf(filepath)
    chunks=chunk_data.split_data(text)


if __name__=="__main__":
    main()