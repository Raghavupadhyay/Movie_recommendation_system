import streamlit as st
import pandas as pd

import requests
import pickle




def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return  recommended_movies

# --- Load similarity.pkl from Hugging Face ---
similarity_url = "https://huggingface.co/raghavu2108/movie-models/resolve/main/similarity.pkl"
similarity_response = requests.get(similarity_url)
similarity = pickle.loads(similarity_response.content)

# --- Load movies_dict.pkl from Hugging Face ---
movies_url = "https://huggingface.co/raghavu2108/movie-models/resolve/main/movies_dict.pkl"
movies_response = requests.get(movies_url)
movies_dict = pickle.loads(movies_response.content)
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')
#option=st.selectbox(
    #'How would you like to be connected?',
   # movies['title'].values)
selected_movie_name= st.selectbox(
    'Select a movie:',
    movies['title'].tolist())
if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)