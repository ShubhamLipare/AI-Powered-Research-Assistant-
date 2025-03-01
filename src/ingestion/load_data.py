import os
import PyPDF2
import sys
from src.logger import logging
from src.exception import CustomException

def load_pdf(path):
    "Load text from PDF file."

    try:
        if not os.path.exists(path):
            logging.info(f"File not found:{path}")
            return 
        logging.info("Loading data from PDF")
        with open(path,"rb") as file:
            reader=PyPDF2.PdfReader(file)
            text="\n".join([page.extract_text() for page in reader.pages])

        if not text.strip():
            logging.info("Extracted text is empty. Check the PDF content.")
            return None
        
        logging.info("Data loaded sucessfully!!!")
        return text
    
    except Exception  as e:
        raise CustomException(e,sys)
    

