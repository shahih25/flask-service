from flask import Flask, request, make_response
from data.data import add_user, get_user_by_username, update_password, delete_user
import json

app = Flask(__name__)

@app.get("/hello")
def hello_world():
    return {"name": "Hasan Shahid"}

@app.post("/login")
def login():
    username = request.json["username"]
    if "password" in request.json:
        print("hello")
        password = request.json["password"]
    else:
        password = ''
    return make_response(add_user(username, password), 201)
    
    
@app.get("/get-user")
def get_user():
    username = request.args.get("user")
    user = get_user_by_username(username)
    
    if user:
        return make_response(user, 200)
    else:
        return make_response({
            "message": "user doesn't exist"
        }, 404)
        
        
@app.put("/<username>/update-password")
def update_password_by_username(username):
    password = request.json["password"]
    user = update_password(username, password)
    if user is not None:
        return make_response(user, 200)
    else:
        return make_response({"message": "user doesn't exist"}, 404)
    
    
@app.delete("/<username>")
def delete_user(username):
    user = delete_user(username)
    if user is not None:
        return make_response(user, 200)
    else:
        return make_response({"message": "user doesn't exist"}, 404)