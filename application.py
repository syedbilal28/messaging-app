import os

from flask import Flask,render_template,request,redirect,json
from flask_socketio import SocketIO, emit
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
Session(app)
conversation = {"message":""}
username =None
@app.route("/")
def index():
    global username
    if username:
        return redirect('login')

    return render_template("index.html")

@app.route("/login", methods = ["POST","GET"])
def login():
    global username
    if username== None:
        username = request.form.get("username")
    return render_template("menu.html" , username=username)

@app.route("/channel/<channel_name>")
def channel(channel_name):
    print(channel_name)
    infile = open(str(channel_name)+".txt","a")
    try:
        content= infile.readlines()
    except:
        content= []
    return render_template("chatroom.html",channel_name= channel_name,messages= content)
@socketio.on('Send message')
def send(data):
    message = data['message']
    channel_name = data['channel_name']
    print(message)
    infile = open(str(channel_name)+".txt","a")
    infile.write(message)
    infile.close()
    emit('message sent',message,broadcast=True)
@socketio.on("create channel")
def create(data):
    channel_name = data['channel_name']
    infile = open(str(channel_name)+".txt","w")
    infile.close()
    


if __name__ == "__main__":
    app.run(debug=True)