from pprint import pprint
import streamlit as st
import streamlit_authenticator as stauth
import os
import sys
from pathlib import Path
import pickle
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# I should replace this line by dot env file
load_dotenv(".env")
URI = os.getenv("URI")
MONGO_USER_FIELDS = ['name', 
                    #  'username', 
                     'password', 'email']

# Create a new client and connect to the server
client = MongoClient(URI)

# Retrieve all documents from the database
db = client["projects"]
collection = db["users"]
docs = list(collection.find())
# I need to create user_data = from list of keys and values
user_data = {'usernames': {}}


for doc in docs:
    user_data['usernames'][doc['username']] = {}
    for k, v in doc.items():
        if k in MONGO_USER_FIELDS:
            user_data['usernames'][doc['username']][k] = v

# pprint(user_data)
# sys.exit()


authenticator = stauth.Authenticate(user_data,
    "fit-my-cv", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(location="main", max_login_attempts=15)

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.title("Hello, World!")