# import streamlit as st
# import streamlit_authenticator as stauth
import os
import sys
from pathlib import Path
import pickle
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# I should replace this line by dot env file
load_dotenv(".env")
URI = os.getenv("URI")

# Create a new client and connect to the server
client = MongoClient(URI)

# Retrieve all documents from the database
db = client["projects"]
collection = db["users"]
documents = collection.find()

for k, v in documents[0].items():
    print(k, v)


names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#     "fit-my-cv", "abcdef", cookie_expiry_days=30)

# name, authentication_status, username = authenticator.login("Login", "main")

# if authentication_status == False:
#     st.error("Username/password is incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

# if authentication_status:
#     st.title("Hello, World!")