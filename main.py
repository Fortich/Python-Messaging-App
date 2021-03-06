from flask import Flask, render_template, request
from flask_socketio import SocketIO
from dotenv import load_dotenv
from subprocess import call
import threading
import requests
import json
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('socket.html')


@app.route('/receive', methods=['POST'])
def receive_message():
    content = request.json
    socketio.emit('new', content)
    return 'ok'


def getToList():
    with open('toList.js') as json_file:
        data = json.load(json_file)
    print(data)
    return data


@socketio.on('message')
def handle_message(message):
    sendurl = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Authorization': 'key={}'.format(os.environ['ApiKey'])
    }
    json_string = {
        "registration_ids": getToList(),
        "notification": {
            "title": "",
            "body": str(message)
        }
    }
    res = requests.post(sendurl, headers=headers, json=json_string)
    print(res)


if __name__ == '__main__':
    targs = (app, 'localhost', os.environ['PORT'])
    threading.Thread(target=socketio.run, args=(targs)).start()
    call(["node", "index.js"])
