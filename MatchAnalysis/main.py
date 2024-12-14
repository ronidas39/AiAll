from podcastfy.client import generate_podcast
import streamlit as st 

st.title("post match analysis by AI CRICKET")
url=st.text_input("enter your url")

config={
    "conversation_style":["detailed cricket match analysis","discussion","question-answer","summary"],
    "roles_person1":"cricketing expert with good analytical knowledge,professionally fluent in english,charming young male voice",
    "roles_person2":"young female cricket analyst",
    "podcast_name":"daily post match summary",
    "podcast_tagline":"cricket season is going on"
}
if url is not None:
    btn=st.button("submit")
    if btn:
        audiofile=generate_podcast(urls=[url],tts_model="openai",conversation_config=config)
        st.audio(audiofile)

