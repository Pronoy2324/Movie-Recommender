import streamlit as st
import pickle
import pandas as pd
from tmdbv3api import TMDb
from tmdbv3api import Movie

movie_list = pickle.load(open('movies.pkl', 'rb'))
mov_lis = movie_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

def movieposter(m_id):
    try:
        tmdb = TMDb()
        tmdb.api_key = '2c0a8b0ecaaaaf14ea6220aecd7362a3'

        movie = Movie()
        response = movie.details(m_id)
        poster_path = response.poster_path

        poster_url = f'https://image.tmdb.org/t/p/w300{poster_path}'
    except:
        poster_url = 'https://default-poster-url.com/image.jpg'
    print(poster_url)
    return poster_url



def recommend(movie):
    L = []
    poster = []
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    mov_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    movie = Movie()
    for i in mov_list:
        poster.append(movieposter(movie_list.iloc[i[0]].movie_id))
        L.append(movie_list.iloc[i[0], 1])
    return L, poster




movies,posters=recommend('Avatar')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    (mov_lis))



if st.button('Search recommend'):
    recommendation_list, posters = recommend(selected_movie_name)

    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendation_list[0])
        st.image(posters[0])
    with col2:
        st.text(recommendation_list[1])
        st.image(posters[1])
    with col3:
        st.text(recommendation_list[2])
        st.image(posters[2])
    with col4:
        st.text(recommendation_list[3])
        st.image(posters[3])
    with col5:
        st.text(recommendation_list[4])
        st.image(posters[4])










