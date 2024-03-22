
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

import requests
def run_q(query):
        
    DB_FAISS_PATH = 'C:\\Users\\juri2\\Desktop\\uni\\2023\\second term 2023-2024\\GP2\\new new\\stud_chatbot\\dp_faiss'

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                        model_kwargs={'device': 'cpu'})

    ndb = FAISS.load_local(DB_FAISS_PATH, embeddings)
    
    results = ndb.search(query, k=1,search_type="similarity")  # You can adjust k as needed
    res = results[0].page_content 
    return res,query
#End Function 

def query_model(payload):
    
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {"Authorization": "Bearer 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"}


    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
#End Function

def improve_query(query):
    sim,query = run_q(query)
    prompt = "given this data: \n" + sim + "\n" + "\n" + query  + " Dont add any details dont add any infromation that was not given in the data just say the exact answer thats in the data no more."
    sim_arr = sim.split(",")
    output = query_model({
        "inputs": prompt,
    })
    try:
        response = output[0].get('generated_text')
    except:
        response = " " *len(prompt) +  "Sorry I could not understand the question."
    response = response[len(prompt):]
    return response,sim_arr
#End Function 

def method2(query,sim_arr):
    try:        
        sim_arr = [d for d in sim_arr if " : " in d]
        data = {d.split(" : ")[0].replace("_"," "):d.split(" : ")[1]  for d in sim_arr}
        dk = list(data.keys())
        og_query = query + "\nThe answer is: "
        query = " ".join(query.split(" ")[3:6])
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(dk + [query])

        # Calculate cosine similarity
        
        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(X[:-1], X[-1].reshape(1, -1))
        if max(cosine_similarities) < 0.2: return "Sorry I could not understand the question. can you please rephrase it like this: \nwhat is/are the [what you want to know] of the [what you want to know about]?"
        most_similar_index = cosine_similarities.argmax()
        # Find the index of the most similar string
        most_similar_string = dk[most_similar_index]
        res = og_query +data[most_similar_string]
        return res
    except:
        return "Sorry I could not understand the question. can you please rephrase it like this: \n what is/are the [what you want to know] of the [what you want to know about]?"
#End Function 
 
def get_answer(query):
    
    response,sim_arr = improve_query(query)
    ms = method2(query,sim_arr)
    return response , ms

# print(get_answer("What is the name of the university?"))
