# 
# Felipe Ryan Jul 2015
#

from flask import Flask, render_template, jsonify, request, abort
from flask.ext.socketio import SocketIO, emit
import json
from corsdecorator import crossdomain

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

app.debug = True

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/v1.0/scans', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def receive_scan_from_api():
    if not request.json:
        return 'not json...'

    msg = json.dumps(request.json)

    print '\nJson Received from External Source:'
    print msg
    print '\n'
    
    socketio.emit('scan', msg)

    return jsonify({'Response':'All ok'}), 201


# Actual Socket Events
@socketio.on('ping')
def handle_my_custom_event(jsonMessage):
    print('received json: ' + str(jsonMessage))
    reply = json.dumps({'message':'You are connected'})
    emit('pong', reply)


if __name__ == '__main__':
    socketio.run(app)
