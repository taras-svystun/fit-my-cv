from pprint import pprint
import streamlit as st
import streamlit_authenticator as stauth
import os
import sys
from pathlib import Path
import pickle
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from utils.utils import extract_users_data


load_dotenv(".env")
URI = os.getenv("URI")


client = MongoClient(URI)
db = client["projects"]
collection = db["users"]
docs = list(collection.find())
user_data = extract_users_data(docs)

# pprint(user_data)
# sys.exit()


with st.sidebar:
    "[View the source code](https://github.com/taras-svystun/fit-my-cv)"


authenticator = stauth.Authenticate(user_data,
    "fit-my-cv", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(location="main", max_login_attempts=15, clear_on_submit=True)

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    """
    # Main Web Page
    Welcome to our main web page!
    To navigate the web-site find 2 sections in a sidebar:
    
    1. First checkout the chat bot about your experience
    
    2. Then you can fit your cv to a speciffic job posting
    """
