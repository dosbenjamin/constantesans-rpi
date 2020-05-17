from utils.socketio_client import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 23
GPIO.setup(LIGHT_PIN, GPIO.IN)

@sio.event
def light_state(state):
  sio.emit('light_state', state)
