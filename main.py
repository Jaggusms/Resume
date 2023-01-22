import streamlit as st
from PIL import Image
import base64
from pathlib import Path
import streamlit.components.v1 as components  # Import Streamlit
PAGE_TITLE = "Jagadeesh Digital Resume"
PAGE_ICON = "source/pageicon.png"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.markdown("""
<style>
#MainMenu {visibility:hidden}
footer {visibility: hidden}
.css-15zrgzn {display: none}
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
""",unsafe_allow_html=True)
# st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
# with open('html/img.html')as f:
#  st.markdown(f"<html>{f.read()}</html>", unsafe_allow_html = True)
#  components.html(f"<html>{f.read()}</html>")

with open("css/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)



def img_to_bytes(img_path):
  return base64.b64encode(Path(img_path).read_bytes()).decode()
def img_to_html(img_path):
  return "<img src='data:image/png;base64,{}' class='img-fluid'>  ".format(img_to_bytes(img_path))

col1, col2 = st.columns([3, 1],gap='small')
with col2:
    #st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
    st.image('source/ProfilePic.png', caption=None, width=150)
with col1:
    st.title("JAGADEESH SANNIBOINA")
    st.write("B-Tech 2017-2021")
    st.write('''I am a Machine Learning Engineer who insights into Deep Learning, Neural Networks, Computer Vision
    and Natural Language Processing. I am extending myself towards Could, Data Engineering and Science
    to archive a full stack Machine Learner. I am Multitasking and Problem Solver.''')
    


# path = "source/ProfilePic.png"
# image = Image.open(path)
# st.image(image, width = 150)





























def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('source/wte.jpg')  