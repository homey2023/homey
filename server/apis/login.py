from flask_restx import Namespace, Resource
from flask import Flask, render_template, url_for, request, session, redirect, flash
from pymongo.mongo_client import MongoClient
from flask_bcrypt import Bcrypt
import config 

login_api = Namespace(
    name='login',
    description='Authentication API'
)

USER_NAME = config.MONGODB_USERNAME
PASSWORD = config.MONGODB_PASSWORD

client = MongoClient(f'mongodb://{USER_NAME}:{PASSWORD}@43.202.53.29', 27017, tlsInsecure= True)
db = client.homey
users = db.user

@login_api.route('/login', methods = ['POST', 'GET'])
class Login(Resource):
    def post(self):
        # Code to handle user authentication
        if request.method == 'POST':
            user_id = request.form.get("id")
            user_found = users.find_one({'id': user_id})

            #signup_user = user.find_one({'id': request.form['id']})
        
        if user_found:
            #message = 'Successful Login'
            success = True
            return success
        pass

@login_api.route('/logout')
class Logout(Resource):
    def post(self):
        # Code to handle user logout
        pass
