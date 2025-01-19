
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAKdbmUcgE7iutygvdQPMbwf97pvQmZv_4",
  "authDomain": "authpython-163ca.firebaseapp.com",
  "projectId": "authpython-163ca",
  "storageBucket": "authpython-163ca.firebasestorage.app",
  "messagingSenderId": "701861074902",
  "appId": "1:0177867774977:web:1ab4ebf8367d06d4s47677",
  "databaseURL": "https://authpython-173ca-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def signUp():
    email = input("email: ")
    password = input("password: ")

    auth.create_user_with_email_and_password(email, password)
    print("User created.")

def login():
    email = input("email: ")
    password = input("password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
        print(auth.get_account_info(user["idToken"]))
        print("login")
    except:
        print("incorrect email or password")

#signUp()
login()