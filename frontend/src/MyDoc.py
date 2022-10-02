import streamlit as st
import cohere
from dotenv import load_dotenv
load_dotenv()

co = cohere.Client("qfjwp1pbZawgJ6Ob8vV0REhLDUcZxWg9FrXLEh0m")

# Initialization
# page_bg_img = """
# <style>
# body {
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
# background-size: cover;
# }
# </style>
# """
#
# st.markdown(page_bg_img, unsafe_allow_html=True)

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
st.subheader('Describe your symptoms to find plausible illnesses')

col1, col2 = st.columns(2)

with col1:
    st.write("Enter your symptoms:")
    input = st.text_area('Enter your symptoms here', height=200)
    st.button('Generate Hashtags', on_click=generate_hashtags(input))

with col2:
    st.write("Classifications")
    st.write(st.session_state.output)
