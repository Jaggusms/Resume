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
@st.cache_resource()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
@st.cache_resource()
def get_img_with_href(local_img_path, target_url,width):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'<a href="{target_url}"><img align="left" src="data:image/{img_format};base64,{bin_str}" width="{width}"/></a>'
    return html_code
#@st.cache_resource() 
def get_img_with_href_message(local_img_path, target_url,message):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img align="left" src="data:image/{img_format};base64,{bin_str}" width="25"/>
        </a><span style="color:white;float: left;">{message}</span>'''
    return html_code
def get_img(local_img_path,message):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
            <p ><img align="left" src="data:image/{img_format};base64,{bin_str}" width="20"/>{message}</p>'''
    return html_code 


listTabs=["Home", "Education", "Work Experience",'Skills','Projects','Contact',"Portfolio"]
#tab1s = st.tabs(listTabs) 
tab1s = st.tabs([s.center(10," ") for s in listTabs])
# st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
# with open('html/img.html')as f:
#  st.markdown(f"<html>{f.read()}</html>", unsafe_allow_html = True)
#  components.html(f"<html>{f.read()}</html>")
with tab1s[0]:
    with open("css/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    social_meadia={
        "source/linkdin.png":"https://www.linkedin.com/in/jagadeeshsanniboina/",
        "source/github_logo.png":"https://github.com/Jaggusms",
        "source/kaggle.png":"https://www.kaggle.com/jagadeeshmemories",
        "source/medium.png": "https://medium.com/@jagadeeshmk",
        "source/stackoverflow.png":"https://stackoverflow.com/users/9774886/jagadeesh-sanniboina?tab=profile",
        "source/twitter.png":"https://twitter.com/SanniboinaJ?t=Mw1069Dj1N5G0-kLGmCMKw",
        "source/hacker_rank.png": "https://www.hackerrank.com/sanniboinajagad1",
        "source/hacker_earth.png":"https://www.hackerearth.com/@jagadeesh220",
        "source/facebook.png": "https://www.facebook.com/jagadeesh.sanniboina.3/",
        "source/leetcode.png": "https://leetcode.com/u/sanniboinajagadeesh/",
        "source/insta.png":"https://www.instagram.com/forgot_your_login_details/",
        "source/MITS.jpg": "https://mits.ac.in/",
        "source/APRJC.png" : "https://aprs.apcfss.in/",
        "source/ZPPH.png"  : "https://spsnellore.ap.gov.in/public-utility/28193202104-zphs-kondagunta-gudur-mandal/",
        "source/location_zpph": "https://www.google.com/maps/place/Zilla+Parishad+High+School/@14.0816058,79.7909562,17z/data=!4m10!1m2!2m1!1sZPHS+Kondagunta,+Andhra+Pradesh!3m6!1s0x3a4ce1ce312463bd:0xa82ae7d18ce022e1!8m2!3d14.0815407!4d79.7927177!15sCh9aUEhTIEtvbmRhZ3VudGEsIEFuZGhyYSBQcmFkZXNokgERZ292ZXJubWVudF9zY2hvb2zgAQA!16s%2Fg%2F11g8y97071",
        "source/location_aprjc":"https://www.google.com/maps/place/A+P+Residential+Junior+College+For+Boys/@13.943345,79.592139,17z/data=!3m1!4b1!4m6!3m5!1s0x3a4d25b79cabd9ad:0x2bebd90682c4fa76!8m2!3d13.943345!4d79.5943277!16s%2Fg%2F1q69wq87s",
        "source/location_btech" : "https://www.google.com/maps/place/Madanapalle+institute+of+technology+and+Science/@13.6296148,78.47635,17z/data=!3m1!4b1!4m6!3m5!1s0x3bb2677c83886ad7:0xad73159e2bddda33!8m2!3d13.6296148!4d78.4785387!16s%2Fm%2F010hplvm",
        "source/carelon.jpg": "https://www.carelonglobal.in/",
        "linkdin_carelon": "https://www.linkedin.com/company/carelon-global-solutions/",
        "glassdoor_carelon":"https://www.glassdoor.co.in/Overview/Working-at-Carelon-Global-Solutions-EI_IE8326220.11,35.htm",
        "resume_git":"https://github.com/Jaggusms/Resume",
        "moneylanduring_git":"https://github.com/Jaggusms/MonayLaundering",
        "Price_Predictor" : "https://github.com/Jaggusms/laptop_price_pridiction",
        "login_page_using_sql":"https://github.com/Jaggusms/login_page_using_sqlserver_flask",
        "login_page_using_mongodb": "https://github.com/Jaggusms/login_mongodb",
        "Messenger":"https://messenger-jagadeesh.streamlit.app/"
        
    }

    # def img_to_bytes(img_path):
    #   return base64.b64encode(Path(img_path).read_bytes()).decode()
    # def img_to_html(img_path):
    #   return "<img src='data:image/png;base64,{}' class='img-fluid'>  ".format(img_to_bytes(img_path))


    #col1, col2 = st.columns([3, 1],gap='small')
    col1,col2= st.columns([5,3],gap="small")
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
        gif_html = get_img("source/location.png",". Tirupati, AP, India")
        st.markdown(gif_html, unsafe_allow_html=True)
        linkdin = get_img_with_href("source/linkdin.png", social_meadia["source/linkdin.png"],25)
        leetcode = get_img_with_href("source/leetcode.png", social_meadia["source/leetcode.png"],25)
        gihub = get_img_with_href("source/github_logo.png", social_meadia["source/github_logo.png"],25)
        kagle=get_img_with_href("source/kaggle.png", social_meadia["source/kaggle.png"],25)
        st.markdown(f"<p> {linkdin} {gihub} {kagle} {leetcode}</p>", unsafe_allow_html=True)
        
    with col2:
        #st.markdown(img_to_html('source/ProfilePic.png'), unsafe_allow_html=True)
        st.image('source/ProfilePic.png', caption=None, width=155)
        with open("source/JAGADEESH SANNIBOINA.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(label="📄 Download CV",data=PDFbyte,file_name="JAGADEESH_SANNIBOINA.pdf",mime="application/octet-stream")
       
    
    #cols = st.columns([0.5 if i in [0,1,2]  else 3 if i==7 else 1 for i in range(10) ],gap="large")
    
    # with cols[0]:
        
        
    #     gif_html = get_img_with_href("source/linkdin.png", social_meadia["source/linkdin.png"],25)
    #     cols[0].markdown(gif_html, unsafe_allow_html=True)
    #     gif_html = get_img_with_href("source/insta.png", social_meadia["source/insta.png"],25)
    #     cols[1].markdown(gif_html, unsafe_allow_html=True)
    #     gif_html = get_img_with_href("source/github_logo.png", social_meadia["source/github_logo.png"],25)
    #     cols[2].markdown(gif_html, unsafe_allow_html=True)
             
                
        
    cols=st.columns([0.25,1,2],gap="small")
    cols[1].image("source/ml.png",width=200)
    cols[2].markdown("<p style='font-family:sans-serif; font-size: 25px;'><b>Bio:<b> </p>", unsafe_allow_html=True)
    cols[2].markdown(''':arrow_right: Dedicated professional transitioning into the field of ***Computer Vision***, with a strong foundation in programming, data analysis, and machine learning. Building expertise in image processing, object detection, and deep learning using Python, OpenCV, and TensorFlow. Eager to apply analytical skills and technical knowledge to develop innovative solutions in computer vision. Committed to continuous learning and contributing to advancements in this dynamic field.''')
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
with tab1s[1]:

    cols = st.columns([0.08,1,1.8,1.5],gap="small")
    with cols[0]:
        #st.write(":classical_building:")
        #st.markdown("#")
        gif_html = get_img_with_href("source/MITS.jpg", social_meadia["source/MITS.jpg"],25)
        st.markdown(gif_html, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<p style='font-family:sans-serif; font-size: 18px;'><b> B-Tech(2017-2021)<b> </p>", unsafe_allow_html=True)
    with cols[-2]:
        #st.markdown("<p style='font-family:sans-serif; font-size: 15px;'>Madanapalle Institute of Technology and Sciences </p>", unsafe_allow_html=True)
        
        st.write('Institute: Madanapalle Institute of Technology and Sciences')
        st.write("Course: Electrical and Electronics Engineering")
        st.write("CGPA: 8.3")
    with cols[-1]:
       #st.write("source/location_btech") 
        st.write('''Adress:                                
                Kadiri Road, Angallu Village                                 
                Madanapalle,                                     
                Andhra Pradesh 517325''')
        #gif_html = get_img("source/location.png",". Tirupati, AP, India")
        gif_html = get_img_with_href_message("source/location.png", social_meadia["source/location_btech"],"Location")
        st.markdown(gif_html, unsafe_allow_html=True)

    
    cols = st.columns([0.08,1,1.8,1.5],gap="small")
    with cols[0]:
        #st.write(":classical_building:")
        #st.markdown("#")
        gif_html = get_img_with_href("source/APRJC.png", social_meadia["source/APRJC.png"],25)
        st.markdown(gif_html, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<p style='font-family:sans-serif; font-size: 18px;'><b> Intermediate (2015-2017)<b> </p>", unsafe_allow_html=True)
    with cols[-2]:
        #st.markdown("<p style='font-family:sans-serif; font-size: 15px;'>Madanapalle Institute of Technology and Sciences </p>", unsafe_allow_html=True)
        
        st.write('Institute: AP Residential Educational Institutions Society')
        st.write("Course: Mathematics,Physices and Chemistry")
        st.write("Marks: 976")
    with cols[-1]:
        st.write('''Adress:                                
                Cross Road, Near APSRTC Depot, Tirupathi Road,                            
                State Highway 59, Venkatagiri,                                        
                Andhra Pradesh 524132''')
        #gif_html = get_img("source/location.png",". Tirupati, AP, India")
        gif_html = get_img_with_href_message("source/location.png", social_meadia["source/location_aprjc"],"Location")
        st.markdown(gif_html, unsafe_allow_html=True)



    cols = st.columns([0.08,1,1.8,1.5],gap="small")
    with cols[0]:
        #st.write(":classical_building:")
        #st.markdown("#")
        gif_html = get_img_with_href("source/ZPPH.png", social_meadia["source/ZPPH.png"],25)
        st.markdown(gif_html, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<p style='font-family:sans-serif; font-size: 18px;'><b>SSC:10th (2014-2015)<b> </p>", unsafe_allow_html=True)
    with cols[-2]:
        #st.markdown("<p style='font-family:sans-serif; font-size: 15px;'>Madanapalle Institute of Technology and Sciences </p>", unsafe_allow_html=True)
        
        st.write('Institute: Zilla Parishad High School ')
        #st.write("Course: Mathematics,Physices and Chemistry")
        st.write("CGPA: 9.0")
    with cols[-1]:
        st.write('''Adress:                                
                Kondagunta                                                             
                Gudur (524101)                              
                Tirupati (Andhra Pradesh)''')
        #gif_html = get_img("source/location.png",". Tirupati, AP, India")
        gif_html = get_img_with_href_message("source/location.png", social_meadia["source/location_zpph"],"Location")
        st.markdown(gif_html, unsafe_allow_html=True)
              
with tab1s[2]:
    cols = st.columns([4,1.5],gap="small")
    with cols[1]:
        st.markdown("##")
        gif_html = get_img_with_href("source/carelon.jpg", social_meadia["source/carelon.jpg"],100)
        st.markdown(gif_html, unsafe_allow_html=True)
        st.markdown("Follow on ")
        carelon_linkdin = get_img_with_href("source/linkdin.png", social_meadia["linkdin_carelon"],20)
        carelon_glassdoor=get_img_with_href("source/glassdoor.png", social_meadia["glassdoor_carelon"],20)
        st.markdown(f"<p> {carelon_linkdin} &nbsp; &nbsp;  {carelon_glassdoor }</p>", unsafe_allow_html=True)
    with cols[0]:
        st.markdown("##")
        st.markdown(":office: <b style='font-size:25px'>Carelon Global Solutions</b> (3rd June-2021- 28th July 2023)",unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("Project 2 ")
        st.markdown("<b>Name:</b> Privacy Assignment Using RAG Model",unsafe_allow_html=True)
        st.markdown("<b>Client:</b> Anthem",unsafe_allow_html=True)
        st.markdown("<b>Description:</b>  ",unsafe_allow_html=True)
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Objective: Developed a robust solution for the privacy assignment of LOINC codes to protect sensitive health information..")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Technologies Used: RAG (Retrieval-Augmented Generation) model, bge-env 1.5, Mistral 8*7B model.")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Project Details: Data Collection and Documentation: Gathered comprehensive information on sensitive and privacy-related health categories, including HIV, sexual transmission, substance abuse disorder, drug rehabilitation, abortion.")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Building various regression and classification algorithms by using various Sklearn also ensemble methods")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Created detailed context documents to store the collected information. Embedding and Vector Selection: Utilized bge-env 1.5 to embed privacy-related information into vector representations.")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Implemented an efficient algorithm to select the top 5 nearest context-related vectors, ensuring high relevance and accuracy. ")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Model Integration: Integrated the selected vectors with the Mistral 8*7B model.")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Designed and implemented a mechanism to pass LOINC codes along with the top 5 vectors and a prompt to the model.")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar:  Ensured that the model leverages the context for accurate privacy assignment and categorization.")
        

       
        st.markdown("#")
        st.markdown("Project 3 ")
        st.markdown("<b>Name:</b> Automation for Control-M by python",unsafe_allow_html=True)
        st.markdown("<b>Client:</b> Anthem",unsafe_allow_html=True)
        st.markdown("<b>Description:</b>  ",unsafe_allow_html=True)
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar: we have create automation python code to migrate one environment to another of CTM folder &nbsp;i.e DEV to SIT vice versa etc..")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar: Generate, modify and pulls require details of the XML file  of Contol M tool by python and the process like web scraping")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar: we need to fill color of Control M folders details in excel by comparing the old and new files of xml format") 
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar: need to get text reports by comparing Elastic Scheduling Platform (ESP) text reports, ControlM xml Reports ")
        st.markdown("&ensp; &nbsp;:black_right_pointing_triangle_with_double_vertical_bar: we have been decrease 50 percent of human efforts in Control M ")
        st.markdown("<b>Libraries Used:</b>  Pandas, xml.etree, openpyxl ",unsafe_allow_html=True)
        
        
    
        


with tab1s[-1]:
    st.markdown("<p style='font-family:sans-serif; font-size: 25px;' ><b> Yet to create<b> </p>", unsafe_allow_html=True)

with tab1s[3]:
    #st.markdown("<p style='font-family:sans-serif; font-size: 20px;' > 1. Programming Language : <br style='color:#EAEFF5'/>Python <Br> 2. Machine Learning <Br> 3. Natural Laguage Processing </p>", unsafe_allow_html=True)
    #st.markdown("")
    st.markdown(":headphones: Programming languages: "+"&nbsp;"*5+"Python(professional)"+"&nbsp;"*5+"R(Basic)")
    st.write("&nbsp;"*8+"Libraries in Python as follows: ")        
    skills=[("Pandas",5),("Numpy",5),("Pyspark",4),("Scikit-Learn",4),("Nltk",3),("Keras",3),("Open-CV",3),("Flask ",4),("Streamlit",4)]

    for library,rating in skills:
        #st.markdown("&nbsp;"*10+" :point_right: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating+"&nbsp;"*5+str(rating)+"/"+"5")
        st.markdown("&nbsp;"*20+" :point_right: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating)
    databases=[("SQL Server",5),("MongoDB",4)] 
    st.markdown(":headphones: DataBase: ")
    for library,rating in databases:
        #st.markdown("&nbsp;"*10+" :point_right: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating+"&nbsp;"*5+str(rating)+"/"+"5")
        st.markdown("&nbsp;"*20+" :pushpin: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating)
    st.markdown(":headphones: Machine Learning:")
    st.markdown("<p style='font-size: 15px;'> <i> "+"&nbsp;"*20+" Exploratory Data Analysis, Feature Engineering, and Selection, Regression Classification Clustering and Ensemble Techniques, Hyper parameter tunning and Model Evalution etc..  </i>", unsafe_allow_html=True)

    st.markdown(":headphones: Natural Language Processing:")
    st.markdown("<p style='font-size: 15px;'> <i> "+"&nbsp;"*20+" POS, Sentiment Analysis, Doc2vec, Word2vec, TF and IDF, BERT, Transformers, Self-Attention, Transfer Learning models etc..  </i>", unsafe_allow_html=True)

    st.markdown(":headphones: Deep Learning:")
    st.markdown("<p style='font-size: 15px;'> <i> "+"&nbsp;"*20+" Artificial Neural Network, Convolutional Neural Network, Recurrent Neural Network, LSTM, etc..  </i>", unsafe_allow_html=True)

    st.markdown(":headphones: Computer Vision:")
    st.markdown("<p style='font-size: 15px;'> <i> "+"&nbsp;"*20+"YOLO,  Object segmentation, Tracking and detection, Data Argumentation, Pooling Techniques, etc..  </i>", unsafe_allow_html=True)


    visuvalizer=[("PowerBI",4),("Tableau",3)] 
    st.markdown(":headphones: Visualization: ")
    for library,rating in visuvalizer:
        #st.markdown("&nbsp;"*10+" :point_right: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating+"&nbsp;"*5+str(rating)+"/"+"5")
        st.markdown("&nbsp;"*20+" :waxing_crescent_moon: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating)

    Devops=[("Git",5),("Docker",3),("Jenkin",2)] 
    st.markdown(":headphones: DevOps Tools:  Basic level")
    for library,rating in Devops:
        #st.markdown("&nbsp;"*10+" :point_right: "+"&nbsp;"*5+library+"&nbsp;"*(25-len(library))+" :star:"*rating+"&nbsp;"*5+str(rating)+"/"+"5")
        st.markdown("&nbsp;"*20+" :truck: "+"&nbsp;"*5+library+"&ensp;"*(15-len(library))+" :star:"*rating)
    
    

with tab1s[4]:
    st.markdown("#")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Sentiment Analysis ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +"We can find whether the sentence is positive or negative by using the pre-trained model from Hugging Face ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Skills: </b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; I used the transformer pipeline library from hugging face as the pre-trained model and streamlet as the deployment ",unsafe_allow_html=True)
    gif_html = get_img_with_href_message("source/Browser.png", "https://sentiment-analysis-jagadeesh.streamlit.app/","Click me")
    st.markdown(gif_html, unsafe_allow_html=True)


    st.markdown("#")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Image Style Adding ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +"This project is based on adding our new styles of original images like artists. It is based on the deep learning concept i.e., Neural Style Transfer ,I used Streamlit as frontend and TensorFlow hub pre-trained model ",unsafe_allow_html=True)
    #st.markdown(":violin: <b>Skills: </b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; data preprocessing, Feature Engineering, Model Building, Model Deployment.. ",unsafe_allow_html=True)
    gif_html = get_img_with_href_message("source/Browser.png", "https://nst-dl.streamlit.app/","Click me")
    st.markdown(gif_html, unsafe_allow_html=True)
    
    st.markdown("#")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Mini Messenger ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +"It acts like messenger we can tranfer any text and links over the site, i used streamlit as frontend and MongoDB as Backend",unsafe_allow_html=True)
    st.markdown(":violin: <b>Skills: </b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Curd Operations on Mondodb and streamlit web fromwork",unsafe_allow_html=True)
    gif_html = get_img_with_href_message("source/Browser.png", social_meadia["Messenger"],"Click me")
    st.markdown(gif_html, unsafe_allow_html=True)
    
    st.markdown("#")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Laptop Price Predictor ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +"Laptop Price Prediction is a regression problem. Given the training instances extracted from various websites we are expected to predict the price of any laptop.",unsafe_allow_html=True)
    st.markdown(":violin: <b>Skills: </b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;  Ensemble models, EDA, Feature Engineering ",unsafe_allow_html=True)
    gif_html = get_img_with_href_message("source/github_logo.png", social_meadia["Price_Predictor"],"Click me")
    st.markdown(gif_html, unsafe_allow_html=True)
    

    st.markdown("#")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Login Page using Flask ",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +" I have created the sample Login page using Rest API Framework (Flask) and backend as SQL and Mondodb as well.",unsafe_allow_html=True)
    st.markdown(":violin: <b>Skills: </b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;  Curd operations on SQL, MongoDB and Rest API requests like POST,GET,PUT managements.   ",unsafe_allow_html=True)
    SQL = get_img_with_href_message("source/github_logo.png", social_meadia["login_page_using_sql"],"SQL")
    mongodb = get_img_with_href_message("source/github_logo.png", social_meadia["login_page_using_mongodb"],"MongoDB")
    # col = st.columns([0.8,1.5,10],gap="small")
    # col[0].markdown(SQL, unsafe_allow_html=True)
    # col[1].markdown(mongodb, unsafe_allow_html=True)
    #print()
    st.markdown(f"<p>{SQL}{mongodb}</p>" , unsafe_allow_html=True)

    st.markdown("##")
    st.markdown(":musical_keyboard: <b>Title:</b>"+"&ensp;"*10 +"Digital Resume",unsafe_allow_html=True)
    st.markdown(":violin: <b>Description:</b>"+"&ensp;"*4 +"This digital resume was developed with streamlit library in python. Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.",unsafe_allow_html=True)
    st.markdown(":violin: <b>Libraries Used:</b>&ensp; streanlit, PIL ",unsafe_allow_html=True)
    gif_html = get_img_with_href_message("source/github_logo.png", social_meadia["resume_git"],"Click me")
    st.markdown(gif_html, unsafe_allow_html=True)
    


with tab1s[5]:
    st.write("You can get some more works of mine by following sites: ")
    st.text(" ")
    string=""
    for idx, data in enumerate(list(social_meadia.items())[3:8]):
        gif_html = get_img_with_href(data[0], social_meadia[data[0]],25)
        string +=gif_html
        
    st.markdown("<p>"+string+"</p>", unsafe_allow_html=True)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.markdown("<p > <center style='color:white; font-family:sans-serif; font-size: 20px;'> Let's Talk </center></p>", unsafe_allow_html=True)
    with st.form("form 3",clear_on_submit=True):
        c1,c2=st.columns(2)
        fn=c1.text_input(label="First Name",placeholder="Please enter First Name")
        sn=c2.text_input(label="Second Name",placeholder="Please enter Second Name")
        em=c1.text_input(label="Mail",placeholder="Please enter valid Email")
        phone=c2.text_input(label="Mobile",placeholder="Please enter Mobile Number")
        message=st.text_area(label="Message",placeholder="Suggestion on this website or for me")
        out=st.form_submit_button("Submit")
        if out:
            if fn=="" or sn=="":
                st.warning("please fill First or Second Name")
            elif "@" not in em:
                st.warning("Please Enter Valid Email")
            else:
                st.success("Submit Successfully, I'll respond soon and Thank you")


import sys
























