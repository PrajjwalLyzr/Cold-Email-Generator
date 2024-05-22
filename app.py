from PIL import Image
import streamlit as st
import coldEmailGenerator

# page config
st.set_page_config(
        page_title="Lyzr - Personalized Cold Email Generator",
        layout="centered",   
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

# style the app
st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)


# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Personalized Cold Email Generator')
st.markdown('Personalizes subject lines, greetings, and content based on your prospect and product, boosting response rates !!!')

# Setting up the sidebar for input
st.sidebar.title("Instagram Script Generator")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type='password')
submit_api_key = st.sidebar.button("Submit API Key")

if submit_api_key:
    coldEmailGenerator.save_api_key(api_key)
    st.sidebar.success("API Key saved!")

col1, col2 = st.columns(2)

with col1:
    st.subheader('Prospect Details')
    prsopect_name = st.text_area('Prospect Name')
    company_information = st.text_area("Prospect's Company Information")

with col2:
    st.subheader('Senders Details')
    information = st.text_area('Senders Product/Service Information')
    outcome = st.text_area('Desired Outcome')


if (prsopect_name and company_information and information and outcome) != "":
    if st.button('Submit'):
        st.markdown('---')
        with open('api_key.txt', 'r') as file:
            api_key = file.read()
        api_key = api_key.replace(" ","")
        email = coldEmailGenerator.email_generator(API_KEY=api_key, 
                                                   prospect_name=prsopect_name, 
                                                   company_information=company_information, 
                                                   prodcut_service_info=information, 
                                                   outcome=outcome)
        st.subheader('Personalized Mail')
        st.write(email)

else:
    st.warning('Please provide the deatails')

