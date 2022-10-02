import cohere
import streamlit as st
from cohere.classify import Example
from dotenv import load_dotenv

from helper import getTopLabels

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

n = 3
m = 3
isSubmitted = False


def generate_hashtags(input):
    if len(input) == 0:
        return None
    n = 3

    response = co.classify(
        model='large',
        inputs=[input],
        examples=[Example("feeling of being cold without an apparent cause", "chills"),
                  Example("vibratory muscular movement", "chills"), Example("involuntary trembling", "chills"),
                  Example("shivers ", "chills"), Example(
                "i don\'t know what\'s wrong with me, but i feel so cold and shaky all the time.\n\nit\'s not just my hands or feet either, it\'s my whole body.\n",
                "chills"), Example(
                "when i get really hot (like in a hot shower) then i start shaking again because of how cold i am.\n\ni\'ve been feeling this way for about two weeks now and it doesn\'t seem to be getting any better at all!",
                "chills"), Example(
                "I\'ve been having a lot of those lately, and it\'s not because I\'m cold. It\'s because my body is trying to tell me something. It\'s telling me that I need to slow down, take care of myself, and get some rest. So this week has been all about taking care of myself - eating well (and by \"well\" I mean healthy), getting enough sleep, drinking lots of water...all the things you\'re supposed to do when",
                "chills"), Example("feeling cold", "chills"),
                  Example("I have phlegm, but it is not yellow or green. It\'s clear and white. Is that normal?",
                          "cough"), Example("I coughed up blood", "cough"),
                  Example("I have dry cough with no other symptoms", "cough"),
                  Example("I have a constant dry hacking cough.\n\n", "cough"),
                  Example("I get a persistent dry hacking cough in the morning after waking up from sleep ", "cough"),
                  Example(
                      "My throat feels like it is on fire all of the time.\n My chest hurts too (not as much as my throat), but still hurts enough to make it hard",
                      "cough"), Example("it hurts to swallow anything (even water)", "cough"),
                  Example("lack of energy,", "fatigue"), Example("excessive tiredness", "fatigue"),
                  Example("I can\'t do this anymore", "fatigue"), Example(
                "Basically, when your muscles are working really hard (like during exercise), they use up all their energy and start using protein in your body as fuel instead of carbohydrates or fat. This is called \"glycogen depletion\" and it can make you feel tired and weak if not replenished",
                "fatigue"), Example("constant tiredness or weakness", "fatigue"),
                  Example("constant state of weariness ", "fatigue"), Example("I fell down", "fatigue"),
                  Example("extreme tiredness", "fatigue"), Example("over tired ", "fatigue"),
                  Example("exhausted.", "fatigue"), Example("My legs keep asking me to rest", "fatigue"), Example(
                "I don\'t think they\'re migraines. They are usually on the right side and feel like my head is being squeezed in a vise.",
                "headache"), Example(
                "Sometimes it feels like someone is hitting me with an axe or hammer inside my skull. It\'s not always on the same spot, either; sometimes it\'s at the back of my head, sometimes near the top or front (but never behind). The pain can be so bad that I throw up from",
                "headache"), Example(
                "it\'s not going away.\n\nIt\'s been there for days now, and I don\'t know what to do about it.\n\nI\'ve tried everything: Tylenol, Advil, Excedrin Migraine... nothing works!",
                "headache"), Example(
                "And the worst part is that my head hurts all over - in my forehead, behind my eyes, on top of my head... everywhere! It feels like someone has taken a hammer to the inside of my skull and",
                "headache"), Example("I have a dizzying pain", "headache"),
                  Example("The migraines would come of too much cheese or chocolate", "headache"),
                  Example("join discomfort", "joint pain"), Example("a burst of pain in my joints", "joint pain"),
                  Example(
                      "I walk like my limbs don’t really belong to me and each step is a negotiation rather than an order",
                      "joint pain"),
                  Example("my knuckles felt too large and like they didn\'t want to bend", "joint pain"), Example(
                "I\'ve been in a lot of pain for the past few days, and it\'s not getting better. It\'s actually getting worse. I can\'t sleep because my hip hurts so much that when I lie down on one side, it feels like someone is stabbing me with a knife in the other hip. My back hurts too, but at least that doesn\'t keep me awake at night (yet).\n\nI have an appointment with my rheumatologist tomorrow morning, and hopefully",
                "joint pain"), Example("Don\'t show me food dont\' show me drinks", "nausea"),
                  Example("my stomach is tumbling like a dryer...", "nausea"), Example("Sick to my stomach", "nausea"),
                  Example("MY STOMACH IS KNOTTING", "nausea"),
                  Example("Stomach doing flip flops or turning somersaults", "nausea"),
                  Example("Butterflies? I have a whole swarm of bees in there.", "nausea")])

    getSymps = getTopLabels(response, n)
    # getSymps returns a list of 3 objects [(symptom1:confidence1),(symptom2:confidence2),(symptom3:confidence3)]

    newInput=''.join(str(x) for x in getSymps)

    newResponse: cohere.classify.Classifications

    newResponse = co.classify(
        model='medium',
        inputs=[newInput],
        examples=[Example("fatigue, tussis, fever, breathlessness", "Bronchial Asthma"), Example("tussis, fever", "Bronchial Asthma"), Example("tussis, fever, breathlessness", "Bronchial Asthma"), Example("tussis, fever, breathlessness", "Bronchial Asthma"), Example("fatigue, breathlessness", "Bronchial Asthma"), Example("fatigue, yellowish skin, nausea", "Hepatitis C"), Example("fatigue, yellowish skin", "Hepatitis C"), Example("yellowish skin, nausea", "Hepatitis C"), Example("fatigue, nausea", "Hepatitis C"), Example("nausea", "Hepatitis C"), Example("yellowish skin", "Hepatitis C"), Example("fatigue, weight loss, mood swings", "Hypothyroidism"), Example("fatigue", "Hypothyroidism"), Example("weight loss, mood swings", "Hypothyroidism"), Example("fatigue, mood swings", "Hypothyroidism"), Example("mood swings", "Hypothyroidism"), Example("chills, vomiting, fever", "Malaria"), Example("chills, vomiting, fever", "Malaria"), Example("vomiting, fever, headache", "Malaria"), Example("vomiting, chills, headache", "Malaria"), Example("vomiting, fever", "Malaria"), Example("vomiting, fever", "Malaria"), Example("fatigue, fever, breathlessness, tussis", "Pneumonia"), Example("fatigue, fever", "Pneumonia"), Example("breathlessness, tussis", "Pneumonia"), Example("fatigue, tussis", "Pneumonia"), Example("breathlessness, tussis, fever", "Pneumonia"), Example("chills, fatigue, fever", "Typhoid"), Example("chills, fatigue", "Typhoid"), Example("chills, fever", "Typhoid"), Example("fatigue, chills, nausea", "Typhoid"), Example("vomiting, chills, headache", "Typhoid")])

    getDiseases = getTopLabels(newResponse, m)

    for i in range(n):
        st.session_state[i] = getSymps[i]

    for j in range(m):
        st.session_state[n + j] = getDiseases[j]

    global isSubmitted
    isSubmitted = True

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('My Doctor Application')
st.subheader('Describe your symptoms to find plausible illnesses')

col1, col2, col3 = st.columns(3)

with col1:
    input = st.text_area('Enter your symptoms here', height=200)
    st.button('Submit', on_click=generate_hashtags(input))

with col2:
    st.write("Symptoms")
    if isSubmitted is True:
        for i in range(n):
            st.write(str(st.session_state[i][1]) + " : " + str(st.session_state[i][0]))

with col3:
    st.write("Diseases")
    if isSubmitted is True:
        for j in range(n, n + m):
            st.write(str(st.session_state[j][1]) + " : " + str(st.session_state[j][0]))
