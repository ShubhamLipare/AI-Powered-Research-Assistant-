import os
import sys
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from src.logger import logging
from src.exception import CustomException

class VectorStore:
    def __init__(self,index_path="data/vectorestore.index"):

        try:
            self.index_path=index_path
            self.embedding=HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            logging.info("Vectore store initiallized sucessfully")

            os.makedirs(index_path,exist_ok=True)
            index_file=os.path.join(index_path,"index.faiss")

            if os.path.exists(index_file):
                logging.info(f"Loading existing FAISS index from {index_file} ")
                self.vectore_store=FAISS.load_local(index_file,self.embedding,allow_dangerous_deserialization=True)
            else:
                logging.info("No FAISS index found, creating a new one..")
                self.vectore_store=FAISS.from_texts(["dummy test"],self.embedding)
                self.vectore_store.save_local(self.index_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def add_text(self,texts):
        try:
            if isinstance(texts,str):
                texts=[texts]
            elif not isinstance(texts,list) or not all(isinstance(t,str) for t in texts):
                raise ValueError("Text should be a string or list of strings")
            
            if not texts:
                logging.info("Received empty list, not updating FAISS")
                return 
            logging.info(f"Generating embedding for {len(texts)} texts")
            embedding=self.embedding.embed_documents(texts)

            if self.vectore_store.index.ntotal==0:
                self.vectore_store=FAISS.from_embeddings(embedding,texts)
            else:
                self.vectore_store.add_texts(texts)

            self.vectore_store.save_local(self.index_path)
            logging.info(f"Sucessfully added {len(texts)} texts to FAISS index")

        except Exception as e:
            raise CustomException(e,sys)
        

    def as_retriever(self):
        """Returns a retriever from the FAISS index."""
        return self.vectore_store.as_retriever(search_kwargs={"k": 10})

    def search(self,query,k=5):
        """Search FAISS for similar results."""
        try:
            logging.info(f"Searching {query} in FAISS databse")
            retriever=self.as_retriever()
            doc=retriever.invoke(query)[:k]

            if not doc:
                logging.info("No relevent document found")
            return doc
        except Exception as e:
            raise CustomException(e,sys)

