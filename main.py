import streamlit as st
from PIL import Image
import base64

PAGE_TITLE = "Jagadeesh Digital Resume"
PAGE_ICON = "source/pageicon.png"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")
st.markdown("""
<style>
#MainMenu {visibility:hidden}
footer {visibility: hidden}
.css-15zrgzn {display: none}
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
""",unsafe_allow_html=True)
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
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
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
social_meadia={
    "Linkedin":"https://www.linkedin.com/in/jagadeesh-sanniboina-a8096816b/",
    "github":"https://github.com/Jaggusms",
    "kaggle":"https://www.kaggle.com/jagadeeshsanniboina",
    "medium": "https://medium.com/@jagadeeshmk",
    "stackoverflow":"https://stackoverflow.com/users/9774886/jagadeesh-sanniboina?tab=profile",
    "Twitter":"https://twitter.com/SanniboinaJ?t=Mw1069Dj1N5G0-kLGmCMKw",
    "HackerRank": "https://www.hackerrank.com/sanniboinajagad1",
    "HackerEarth":"https://www.hackerearth.com/@jagadeesh220"
}

#col1, col2 = st.columns([3, 1],gap='small')
col1,col2 = st.columns([3,1],gap="small")
with col2:
    #st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
    st.image('source/ProfilePic.png', caption=None, width=150)
with col1:
    st.title("JAGADEESH SANNIBOINA")
    st.markdown('<p style=" color:Blue; ">B-Tech 2017-2021</p>', unsafe_allow_html=True)
    st.write(''':heart_eyes:I am a Machine Learning Engineer who insights into Deep Learning, Neural Networks, Computer Vision
    and Natural Language Processing. I am extending myself towards Could, Data Engineering and Science
    to archive a full stack Machine Learner. I am Multitasking and Problem Solver.''')
    #cols=st.columns(len(social_meadia),gap="small")
    cols = st.columns(len(social_meadia),gap="small")
    for idx,(platform,link) in enumerate(social_meadia.items()):
        cols[idx].write(f"[{platform}]({link})")
    
# st.write('\n')
# st.markdown('<h3 style=" color:black; ">Experience & Qulifications</h3>', unsafe_allow_html=True)
# with open('html/img.html')as f:
#  st.markdown(f"<html>{f.read()}</html>", unsafe_allow_html = True)

# st.text(
#     """
# -  7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )

# path = "source/ProfilePic.png"
# image = Image.open(path)
# st.image(image, width = 150)





























