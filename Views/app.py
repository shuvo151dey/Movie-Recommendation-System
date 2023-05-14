import pandas as pd
import streamlit as st
import pickle

movie_dict = pickle.load(open('movies.pkl', 'rb'))
movie_list = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    index = movie_list[movie_list['title'] == movie].index[0]
    recommended_list = sorted(list(enumerate(similarity[index])), reverse=True, key=(lambda x: x[1]))[1:7]
    return_list = []
    for i in recommended_list:
        return_list.append(movie_list.iloc[i[0]].title)
    return return_list


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Search Your Movie', movie_list['title'].values)

if st.button('Recommended'):
    recommended_list = recommend(selected_movie_name)
    for i in recommended_list:
        st.write(i)
