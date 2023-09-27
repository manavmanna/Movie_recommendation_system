import streamlit as st
import pandas as pd
import pickle
import requests

movies_dict = pickle.load(open('C://Users//user//Desktop//Project//movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('C://Users//user//Desktop//Project//similarity.pkl','rb'))

def fetch_poster(movies_id):
    url = f"https://api.themoviedb.org/3/movie/{movies_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1N2YzZTFiNTg1NjMxMDI3ZWZjMmIwNmYwZDEwNDljOCIsInN1YiI6IjY1MTFhNjNjZTFmYWVkMDBlM2Y3MGQ1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1B232LgbdpPcSu2SUkE_g0J7mb7m11XXtNFDenqj2_w"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = list(sorted(enumerate(distances),reverse = True, key = lambda x:x[1]))[1:6]
    movies_id = []
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movies_id = movies['movie_id'].iloc[i[0]]
        recommended_movies.append(movies['title'].iloc[i[0]])
        recommended_movies_poster.append(fetch_poster(movies_id))
    return recommended_movies_poster,recommended_movies

st.title('Movie Recommender System')


option = st.selectbox(
    'What is your favourite movie?',
    movies['title'].values)

if st.button('Recommend'):
    poster,name = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col1:
        st.text(name[1])
        st.image(poster[1])
    with col1:
        st.text(name[2])
        st.image(poster[2])
    with col1:
        st.text(name[3])
        st.image(poster[3])
    with col1:
        st.text(name[4])
        st.image(poster[4])