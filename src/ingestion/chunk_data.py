import os
import sys
from src.logger import logging
from src.exception import CustomException
from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_data(text,chunk_size=1000,chunk_overlap=200):
    """Split text into smaller chunks for processing."""
    logging.info("splitting data into chunks")
    try :
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        chunks = splitter.split_text(text)
        logging.info(f"data is splitted into {len(chunks)} chunks.")

        return chunks

    except Exception as e:
        raise CustomException(e,sys)

