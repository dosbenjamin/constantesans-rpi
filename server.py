from aiohttp import web
import socketio

# Creates a new Async Socket IO Server.
sio = socketio.AsyncServer(cors_allowed_origins='*')

# Creates a new Aiohttp Web Application.
app = web.Application()

# Binds our Socket.IO server to our Web App instance.
sio.attach(app)

# We kick off our server.
if __name__ == '__main__':
  web.run_app(app)

# Event that tells middleware that RPi is connected.
@sio.event
async def connection_state(sid, state):
  await sio.emit('rpi_connected', state)
