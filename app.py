import streamlit as st
import pandas as pd
import pickle

result = 0
def recommend(title):
    global result
    title = title.replace(' ', '').lower()
    idx = indices[title]
    cosine_sim = cosine_sim2

    # calculating the similariity scores
    sim_score = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_score = sim_score[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_score]

    # Return the top 10 most similar movies
    result = netflix['title'].iloc[movie_indices]
    return result

netflix = pickle.load(open('movie_dict (2).pkl', 'rb'))
cosine_sim2 = pickle.load(open('similarity.pkl', 'rb'))
netflix_data = pickle.load(open('netflix_data.pkl', 'rb'))
movies = pd.DataFrame(netflix)

netflix_data=netflix_data.reset_index()
indices = pd.Series(netflix_data.index, index=netflix_data['title'])
indices.head()



#st.set_page_config(layout="wide")

#st.markdown("""<style>.big-font {font-size:50px !important;}</style>""", unsafe_allow_html=True)

#st.markdown('<p class="big-font">Movie recommender system !!</p>', unsafe_allow_html=True)

st.title('Movie/Series Recommender System')
selected_movie_name = st.selectbox('Select a movie!'
                      , movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

#new_title = '<p style="font-family:serif; color:Green; font-size: 42px;"New image</p'
#t.markdown(new_title, unsafe_allow_html=True)

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://t4.ftcdn.net/jpg/03/71/56/17/360_F_371561715_LVI4qVJ2hyWMDXdqJNGdktggEzjQuC15.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()