import streamlit as st
from PIL import Image
import base64,os
PAGE_TITLE = "Jagadeesh Digital Resume"
PAGE_ICON = "source/pageicon.png"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")
st.markdown("""
<style>
#MainMenu {visibility:hidden}
header {visibility: hidden}
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
    "source/linkdin.png":"https://www.linkedin.com/in/jagadeesh-sanniboina-a8096816b/",
    "source/github.png":"https://github.com/Jaggusms",
    "source/kaggle.png":"https://www.kaggle.com/jagadeeshsanniboina",
    "source/medium.png": "https://medium.com/@jagadeeshmk",
    "source/stackoverflow.png":"https://stackoverflow.com/users/9774886/jagadeesh-sanniboina?tab=profile",
    "source/twitter.png":"https://twitter.com/SanniboinaJ?t=Mw1069Dj1N5G0-kLGmCMKw",
    "source/hacker_rank.png": "https://www.hackerrank.com/sanniboinajagad1",
    "source/hacker_earth.png":"https://www.hackerearth.com/@jagadeesh220",
    "source/insta.png":"https://www.instagram.com/forgot_your_login_details/"
    "source/facebook.png": "https://www.facebook.com/jagadeesh.sanniboina.3/"
}

#col1, col2 = st.columns([3, 1],gap='small')
col1,col2 = st.columns([3,1],gap="small")
with col2:
    #st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
    st.image('source/ProfilePic.png', caption=None, width=150)
with col1:
    st.title("JAGADEESH SANNIBOINA")
    st.markdown(':heart_eyes: :wave: <p style=" color:Blue; ">B-Tech 2017-2021</p>', unsafe_allow_html=True)
    st.markdown('''<p style=" color:skyblue; " >
                I am a Machine Learning Engineer who insights into Deep Learning, Neural Networks, Computer Vision and Natural Language Processing.
                I am extending myself towards Could, Data Engineering and Science to archive a full stack Machine Learner. 
                I am Multitasking and Problem Solver.</p>''', unsafe_allow_html=True)
    #cols=st.columns(len(social_meadia),gap="small")
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" width="25"/>
        </a>'''
    return html_code
cols = st.columns(5,gap="large")
for idx,(platform,link) in enumerate(social_meadia.items()):
    #cols[idx%4].write(f"[{platform}]({link})")
    #cols[idx%4].markdown(f"[![linkdin]({platform})]({link})")
    # st.markdown('''
    # <a href="https://docs.streamlit.io>
    #     <img src="data:image/gif;base64,{source/linkdin.png}" alt="cat gif"/>
    # </a>''',
    # unsafe_allow_html=True)
    # st.markdown('''
    # <a href="https://docs.streamlit.io">
    #     <img src="source\\linkdin.png" />
    # </a>''',unsafe_allow_html=True)
    
    gif_html = get_img_with_href(platform, link)
    cols[idx%5].markdown(gif_html, unsafe_allow_html=True)
    #cols[idx%4].markdown("[![](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
    #cols[idx%4].markdown("[![linkdin](source\\linkdin.png)](https://www.linkedin.com/in/jagadeesh-sanniboina-a8096816b/)")
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





























