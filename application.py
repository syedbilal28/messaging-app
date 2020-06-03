import os

from flask import Flask,render_template,request,redirect
from flask_socketio import SocketIO, emit
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
Session(app)

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

@app.route("/login/<channel_name>")
def channel(channel_name):
    return render_template("chatroom.html",channel_name= channel_name)
@socketio.on('Send message')
def send(data):
    message = data['message']
    emit('message sent',message,broadcast=True)



if __name__ == "__main__":
    app.run(debug=True)