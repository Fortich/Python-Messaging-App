from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

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

@socketio.on('message')
def handle_message(message):
    print('received message: ' + str(message))

if __name__ == '__main__':
    socketio.run(app)