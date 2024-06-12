from pprint import pprint
import streamlit as st
import streamlit_authenticator as stauth
import os
import sys
from pathlib import Path
import pickle
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

def extract_users_data(docs):
    global MONGO_USER_FIELDS

    user_data = {'usernames': {}}

    for doc in docs:
        user_data['usernames'][doc['username']] = {}
        for k, v in doc.items():
            if k in MONGO_USER_FIELDS:
                user_data['usernames'][doc['username']][k] = v
    
    return user_data
# if 'message' not in st.session_state:
#     st.session_state['message'] = ''

# my_input = st.text_input('Enter message', 123)
# sumbit = st.button('submit')
# if sumbit:
#     st.session_state['message'] = my_input




























load_dotenv(".env")
URI = os.getenv("URI")
MONGO_USER_FIELDS = ['name', 
                    #  'username', 
                     'password', 'email']


client = MongoClient(URI)

db = client["projects"]
collection = db["users"]
docs = list(collection.find())
user_data = extract_users_data(docs)

# pprint(user_data)
# sys.exit()


authenticator = stauth.Authenticate(user_data,
    "fit-my-cv", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(location="main", max_login_attempts=15, clear_on_submit=True)

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.title("Main Web Page")
    st.write("Welcome to our main web page!")
    st.write("To navigate the web-site find 2 sections in a sidebar. First checkout the chat bot about your experience and then you can fit your cv to a speciffic job posting.")