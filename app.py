import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(page_title="Text to Audio Converter", page_icon="🎤")

st.title("🎤 AI Text to Audio Converter")

text = st.text_area("Enter your text here")

voice = st.selectbox(
    "Select Voice",
    [
        "en-US-AriaNeural",
        "en-US-GuyNeural",
        "en-IN-NeerjaNeural",
        "en-IN-PrabhatNeural"
    ]
)

async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save("output.mp3")

if st.button("Convert to Audio"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        asyncio.run(generate_audio(text, voice))

        st.success("Audio Generated Successfully!")

        audio_file = open("output.mp3", "rb")

        st.audio(audio_file.read())

        st.download_button(
            label="Download MP3",
            data=audio_file,
            file_name="speech.mp3",
            mime="audio/mpeg"
        )