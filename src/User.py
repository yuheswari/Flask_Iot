import pymongo
from src . Database import Database
from time import time
from src import get_config
from random import randint  #a powerful tool for generating random integers between two specified values.
import bcrypt


db= Database.get_connection()
user=db.users  # db.users is a collection in the database

class User:
    def __init__(self,id):
        print("Init user with {}".format(id))
#todo build a user obj if user is avalable
    @staticmethod
    def login(username,password):
        result=user.find_one({
            "username":username
            })
        if result:
            #very very insecure
            #alternate if result.get['password'] == password:
           # if result['password'] == password:
               # #todo ininitize session token for additional  sequrity
               # return True
            #else:
               # raise Exception("Invalid Password")
       # else:
            #raise Exception("Incorrect credentials")

            hashpw=result['password']
            if bcrypt.checkpw(password.encode(),hashpw):
                #TODO :register a session and retuturn the session id succesfully
                return True
            else:
                raise Exception("Invalid Password")
        else:
            raise Exception("Incorrect credentials")
        
        
    @staticmethod
    def register(username, password, confirm_password):
        #todo avoid duplicate signup
        if password != confirm_password:
            raise Exception("Passwords do not match")
        password = password.encode()
        salt=bcrypt.gensalt()
        password=bcrypt.hashpw(password,salt);   #generate a salt
        id = user.insert_one({
            "username": username, #todo make username unique
            "password": password,
            "register_time": time(),
            "active": False,
            "active_token": randint(100000, 999999)
        })  

        # we should send this otp activate token via sms or email, but for now we will just print it
        # todo use email or sms service to send the otp 
        return id