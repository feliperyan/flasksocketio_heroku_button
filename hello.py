from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello():
	return render_template('index.html')


@socketio.on('first connect')
def handle_my_custom_event(jsonMessage):
    print('received json: ' + str(jsonMessage))
    reply = json.dumps({'body':'You are connected'})
    emit('pong', reply)


if __name__ == '__main__':
    socketio.run(app)

