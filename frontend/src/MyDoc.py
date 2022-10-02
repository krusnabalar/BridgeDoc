import streamlit as st
import cohere
from dotenv import load_dotenv
load_dotenv()

co = cohere.Client("qfjwp1pbZawgJ6Ob8vV0REhLDUcZxWg9FrXLEh0m")

# Initialization

if 'output' not in st.session_state:
    st.session_state['output'] = 'Output:'


def generate_hashtags(input):
    if len(input) == 0:
        return None
    response = co.generate(
        model='large',
        prompt='Given a post, this program will generate relevant hashtags.\n\nPost: Why are there no country songs about software engineering\nHashtag: #softwareengineering #code \n--\nPost: Your soulmate is in the WeWork you decided not to go to\nHashtag: #wework #work \n--\nPost: If shes talking to you once a day im sorry bro thats not flirting that standup\nHashtag: #standup #funny \n--\nPost: {}\nHashtags:'.format(
            input),
        max_tokens=20,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    st.session_state['output'] = response.generations[0].text


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('My Doctor Application')
st.subheader('Boilerplate for Co:here, Streamlit, Streamlit Cloud')
st.write('''This is a simple **Streamlit** app that takes in symptoms and returns the diagnosed illness.''')

input = st.text_area('Enter your post title caption here', height=200)
st.button('Generate Hashtags', on_click=generate_hashtags(input))

col1, col2 = st.columns(2)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

st.write(st.session_state.output)
