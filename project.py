import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict= pickle.load(open('movies_dict.pkl','rb'));
similarity = pickle.load(open('similarity.pkl','rb'));
movies = pd.DataFrame(movies_dict)



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d56fe04e5ff1e7c4583166523b68f4c8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


def Recommended(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]   ## it will return the index of the movie
    
    recommended_list = []
    recommended_movies_posters = []
    
    for i in  movie_list:
        recommended_list.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]]['id']))

    return recommended_list,recommended_movies_posters



st.title(':blue[Movie Recommender System]')
Selected_movie = st.selectbox(":green[Search Movie]", movies['title'].values)


if st.button(":blue[Recommend]", type="secondary"):
    names,posters = Recommended(Selected_movie)
    
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])   

    with col5:
        st.text(names[4])
        st.image(posters[4])     
