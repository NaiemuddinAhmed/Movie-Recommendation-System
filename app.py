import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
list_movies = movies['title'].values

st.header("Movie Recommender System")
selected_value = st.selectbox("Select movie from dropdown", list_movies)


def rec(str_movie):
    index = movies[movies['title'] == str_movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse =True, key=lambda vector:vector[1])
    r_movies = []
    for i in distance[1:6]:
         r_movies.append(movies.iloc[i[0]].title)
    return r_movies

def text(text, width):
        padding = " " * (width - len(text))
        st.text(f"{text}{padding}")

def fetch_poster(id):
     url = 
     data=requests.get(url)

if st.button("Show Recommend"):
    name = rec(selected_value)
    c1,c2,c3,c4,c5 = st.columns(5)
    c_width = 10
    
    with c1:
        text(name[0],c_width)
    with c2:
        text(name[1], c_width)
    with c3:
        text(name[2],c_width)
    with c4:
        text(name[3],c_width)
    with c5:
        text(name[4],c_width)
       


