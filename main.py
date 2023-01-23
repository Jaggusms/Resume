import streamlit as st
from PIL import Image
import base64,os
PAGE_TITLE = "Jagadeesh Digital Resume"
PAGE_ICON = "source/pageicon.png"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")
st.get_option("theme.primaryColor")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""<style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-attachment: fixed;
        background-size: cover
    }}</style>""",unsafe_allow_html=True)
add_bg_from_local('source/charcoal.png') 
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
            <img align="left" src="data:image/{img_format};base64,{bin_str}" width="25"/>
        </a>'''
    return html_code 
def get_img(local_img_path,message):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
            <p ><img align="left" src="data:image/{img_format};base64,{bin_str}" width="20"/>{message}</p>'''
    return html_code 

tab1s = st.tabs(["Home", "Education", "Work Experience","Portfolio",'Skills','Projects','Contact']) 
# st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
# with open('html/img.html')as f:
#  st.markdown(f"<html>{f.read()}</html>", unsafe_allow_html = True)
#  components.html(f"<html>{f.read()}</html>")
with tab1s[0]:
    with open("css/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)



    # def img_to_bytes(img_path):
    #   return base64.b64encode(Path(img_path).read_bytes()).decode()
    # def img_to_html(img_path):
    #   return "<img src='data:image/png;base64,{}' class='img-fluid'>  ".format(img_to_bytes(img_path))
    social_meadia={
        "source/linkdin.png":"https://www.linkedin.com/in/jagadeesh-sanniboina-a8096816b/",
        "source/github_logo.png":"https://github.com/Jaggusms",
        "source/kaggle.png":"https://www.kaggle.com/jagadeeshsanniboina",
        "source/medium.png": "https://medium.com/@jagadeeshmk",
        "source/stackoverflow.png":"https://stackoverflow.com/users/9774886/jagadeesh-sanniboina?tab=profile",
        "source/twitter.png":"https://twitter.com/SanniboinaJ?t=Mw1069Dj1N5G0-kLGmCMKw",
        "source/hacker_rank.png": "https://www.hackerrank.com/sanniboinajagad1",
        "source/hacker_earth.png":"https://www.hackerearth.com/@jagadeesh220",
        "source/insta.png":"https://www.instagram.com/forgot_your_login_details/",
        "source/facebook.png": "https://www.facebook.com/jagadeesh.sanniboina.3/"
    }

    #col1, col2 = st.columns([3, 1],gap='small')
    col1,col2 ,col3= st.columns([2,1,0.5],gap="medium")
    with col2:
        #st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
        st.image('source/ProfilePic.png', caption=None, width=200)
    with col1:
        st.markdown("<p style='font-family:sans-serif; font-size: 20px;'>Hello, I'm</p>", unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; font-size: 42px;"><i>JAGADEESH SANNIBOINA<i></p>', unsafe_allow_html=True)
        st.write('Machine Learning Engineer | Data Scientist')
        #st.markdown('''<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 1rem;}</style>''', unsafe_allow_html=True)
        st. write("--")
        gif_html = get_img("source/mail1.png",". sanniboinajagadeesh@gmail.com")
        st.markdown(gif_html, unsafe_allow_html=True)
        gif_html = get_img("source/contact.png",". 8500060896")
        st.markdown(gif_html, unsafe_allow_html=True)
        gif_html = get_img("source/location.png",". Nellore,AP, India")
        st.markdown(gif_html, unsafe_allow_html=True)
    cols = st.columns([0.5 if i in [0,1,2]  else 3 if i==7 else 1 for i in range(10) ],gap="large")
    with cols[0]:
        gif_html = get_img_with_href("source/linkdin.png", social_meadia["source/linkdin.png"])
        cols[0].markdown(gif_html, unsafe_allow_html=True)
        gif_html = get_img_with_href("source/insta.png", social_meadia["source/insta.png"])
        cols[1].markdown(gif_html, unsafe_allow_html=True)
        gif_html = get_img_with_href("source/facebook.png", social_meadia["source/facebook.png"])
        cols[2].markdown(gif_html, unsafe_allow_html=True)
        with open("source/Jagadeesh_ML_Resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            cols[7].download_button(label=" 📄 Download CV",data=PDFbyte,file_name="souce/Jagadeesh_ML_Resume.pdf",mime="application/octet-stream")
                
                
        
    cols=st.columns([0.25,1,2],gap="small")
    cols[1].image("source/ml.png",width=200)
    cols[2].markdown("<p style='font-family:sans-serif; font-size: 25px;'><b>Bio:<b> </p>", unsafe_allow_html=True)
    cols[2].markdown(''':arrow_right: I am a **Machine Learning Engineer** who insights into _Deep Learning, Neural Networks, Computer Vision and Natural Language Processing_.
                    I am extending myself towards Could, Data Engineering and Science to archive a full stack Machine Learner. 
                    I am Multitasking and good Problem Solver.''')
        #cols=st.columns(len(social_meadia),gap="small")

    #cols = st.columns(5,gap="large")
    #for idx,(platform,link) in enumerate(social_meadia.items()):
        # gif_html = get_img_with_href(platform, link)
        # cols[idx%5].markdown(gif_html, unsafe_allow_html=True)
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
        

        #cols[idx%4].markdown("[![](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
        #cols[idx%4].markdown("[![linkdin](source\\linkdin.png)](https://www.linkedin.com/in/jagadeesh-sanniboina-a8096816b/)")
    # st.write('\n')
    # st.markdown('<h3 style=" color:black; ">Experience & Qulifications</h3>', unsafe_allow_html=True)
    # with open('html/img.html')as f:
    #  st.markdown(f"<html>{f.read()}</html>", unsafe_allow_html = True)






























