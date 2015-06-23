from flask import Flask, render_template, jsonify, request
from flask.ext.socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

app.debug = True

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/v1.0/scans', methods=['POST'])
def receive_scan_from_api():
    if not request.json:
        abort(400)
    print request.json
    
    msg = json.dumps({'message':'Received Scan'})
    socketio.emit('scan', msg)

    return jsonify({'Response':'All ok'}), 201


# Actual Socket Events
@socketio.on('first connect')
def handle_my_custom_event(jsonMessage):
    print('received json: ' + str(jsonMessage))
    reply = json.dumps({'message':'You are connected'})
    emit('pong', reply)


if __name__ == '__main__':
    socketio.run(app)
