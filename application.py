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
<<<<<<< HEAD
    print("channel_name")
    infile = open(str(channel_name)+".txt","r")
    content= infile.readlines()
    infile.close()
    return render_template("chatroom.html",channel_name= channel_name,messages = json.dump(content))
=======
    print(channel_name)
    infile = open(str(channel_name)+".txt","a")
    try:
        content= infile.readlines()
    except:
        content= []
    return render_template("chatroom.html",channel_name= channel_name,messages= content)
>>>>>>> 6493cd9b81a7485012052f841a7d53f1942b500c
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
<<<<<<< HEAD
    channel_name = data["channel_name"]
    infile = open(str(channel_name)+".txt","w")
    infile.close()
    print ("channel {} created".format(channel_name))
=======
    channel_name = data['channel_name']
    infile = open(str(channel_name)+".txt","w")
    infile.close()
    
>>>>>>> 6493cd9b81a7485012052f841a7d53f1942b500c


if __name__ == "__main__":
    app.run(debug=True)