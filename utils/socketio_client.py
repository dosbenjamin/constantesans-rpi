import socketio

# Socket connection as client
sio = socketio.Client()
sio.connect('http://localhost:8080')
