from aiohttp import web
import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connection_state(sid, state):
  await sio.emit('rpi_connected', state)

# Humidity events
@sio.on('check_humidity')
async def check_humidity(sid):
  await sio.emit('humidity_check')

@sio.on('humidity_state')
async def humidity_update(sid, value):
  await sio.emit('humidity_update', value)

# Light events
@sio.on('check_light')
async def check_light(sid):
  await sio.emit('light_check')

@sio.on('light_state')
async def light_update(sid, state):
  await sio.emit('light_update', state)

# Movement event
@sio.on('movement_state')
async def movement_update(sid):
  await sio.emit('movement_update')

# Temperature events
@sio.on('check_temperature')
async def check_temperature(sid):
  await sio.emit('temperature_check')

@sio.on('temperature_state')
async def temperature_update(sid, value):
  await sio.emit('temperature_update', value)

# Vibration event
@sio.on('vibration_state')
async def vibration_update(sid):
  await sio.emit('vibration_update')

if __name__ == '__main__': web.run_app(app)
