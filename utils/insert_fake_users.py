import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# I should replace this line by dot env file
load_dotenv(".env")
URI = os.getenv("URI")
MONGO_USER_FIELDS = ['name', 'username', 'password', 'email']

# Create a new client and connect to the server
client = MongoClient(URI)

# Retrieve all documents from the database
db = client["projects"]
collection = db["users"]

fake_users = [
    {"name": "John Doe", "username": "johndoe", "password": "1234567890", "email": "johndoe@example.com"},
    {"name": "Jane Smith", "username": "janesmith", "password": "1234567891", "email": "janesmith@example.com"},
    {"name": "Bob Johnson", "username": "bobjohnson", "password": "1234567892", "email": "bobjohnson@example.com"},
    {"name": "Alice Brown", "username": "alicebrown", "password": "1234567893", "email": "alicebrown@example.com"},
    {"name": "Michael Davis", "username": "michaeldavis", "password": "1234567894", "email": "michaeldavis@example.com"}
]

# Insert fake users into the collection
result = collection.insert_many(fake_users)
print(len(result.inserted_ids))