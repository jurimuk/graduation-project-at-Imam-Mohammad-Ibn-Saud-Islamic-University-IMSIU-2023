import numpy as np
import os
import json
import sqlite3

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

def ceate_db():
    DB_FAISS_PATH = 'dp_faiss'
    if len(os.listdir('dp_faiss')) > 0:
        return
    #load the database
    conn = sqlite3.connect('instance\\university.db')
    #loop through every table and get every row and column
    c = conn.cursor()
    #get the table names
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    #loop through every table
    full_text = ""
    for table in tables:
        #get the column names
        if table[0] == "stats":
            continue
        c.execute("SELECT * FROM " +table[0] )
        #get the column names
        columns = [description[0] for description in c.description]
        text = f"{table[0]} : \n"
        #loop through every row
        for row in c.fetchall():
            r = ""
            for i in range(len(row)):
                r+= f"{columns[i]} : {row[i]}, "
            text += f"{r}\n"
        full_text += text + "\n"
    file_path = f"data\data.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(full_text)
    os.makedirs('data', exist_ok=True)
    DATA_PATH = 'data/'
    DB_FAISS_PATH = 'dp_faiss'

    print('Loading documents...')
    loader = DirectoryLoader(DATA_PATH,
                                glob='*.md',
                                )
    print('Splitting documents...')

    documents = loader.load()
    print("splitting documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                    chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    print("creating embeddings")
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                        model_kwargs={'device': 'cpu'})

    db = FAISS.from_documents(texts, embeddings)
    print("saving db")
    db.save_local(DB_FAISS_PATH)

