MONGO_USER_FIELDS = ['name', 
                    #  'username', 
                     'password', 'email']

def extract_users_data(docs):
    global MONGO_USER_FIELDS

    user_data = {'usernames': {}}

    for doc in docs:
        user_data['usernames'][doc['username']] = {}
        for k, v in doc.items():
            if k in MONGO_USER_FIELDS:
                user_data['usernames'][doc['username']][k] = v
    
    return user_data