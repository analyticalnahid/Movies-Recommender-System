import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list_title = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
  response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f42668df92b16db7198c573051aa7b40".format(movie_id))
  data = response.json()
  return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
  movie_index = movies_list[movies_list['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list_nam = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:11]
  
  recommend_movies = []     
  recommend_movies_poster =[]                
  for i in movies_list_nam:
      movie_id = movies_list.iloc[i[0]].movie_id
      recommend_movies.append(movies_list.iloc[i[0]].title)
      recommend_movies_poster.append(fetch_poster(movie_id))
      
  return recommend_movies, recommend_movies_poster   



st.title("Movies Recommendation")
selected_movies_name = st.selectbox("How would like to connect?",
                       movies_list_title)


if st.button("Recommend"):
    names, poster = recommend(selected_movies_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
     st.text(names[0])
     st.image(poster[0])
    with col2:
     st.text(names[1])
     st.image(poster[1])
    with col3:
     st.text(names[2])
     st.image(poster[2])
    with col4:
     st.text(names[3])
     st.image(poster[3])
    with col5:
     st.text(names[4])
     st.image(poster[4])

    col6, col7,col8,col9,col10 = st.columns(5)
    with col6:
     st.text(names[5])
     st.image(poster[5])
    with col7:
     st.text(names[6])
     st.image(poster[6])
    with col8:
     st.text(names[7])
     st.image(poster[7])
    with col9:
     st.text(names[8])
     st.image(poster[8])
    with col10:
     st.text(names[9])
     st.image(poster[9])              
          