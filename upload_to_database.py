import streamlit_authenticator as stauth
import database as db


names = ["Peter Parker", "Rebecca Miller"]
usernames = ["kiran", "kshah"]
passwords = ["kiran","kir@N"]
emails =["kiran@gmail.com","max@gmail.com"]

hashed_passwords = stauth.Hasher(passwords).generate()


for (username, name, hash_password, email) in zip(usernames, names, hashed_passwords, emails):
    db.insert_user(username, name, hash_password, email)



