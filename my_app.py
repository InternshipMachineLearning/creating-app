import streamlit as st

st.write("Hello World: Getting Bore,  Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader To write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text")
# To create hyperlink
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[Streamlit CheatSheet](https://cheat-sheet.streamlit.app/)")
st.success("success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")
from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=200, caption="Satyamev Jayate")
video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.video("https://youtu.be/hecqlL-C7Qw?si=yORpo7RUSRIAyNPM")

audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")



st.header("Button Widgets")


if st.button("Play"):
	st.text("Enjoy Music")
	st.video("https://youtu.be/AvhePEUEnHg?si=IdsLVHQRKSqrYAXY")

    
if st.checkbox("Checkbox"):
	st.text("Checkbox selected")
	st.video("https://youtu.be/AvhePEUEnHg?si=IdsLVHQRKSqrYAXY")
    
    
    
    
    

