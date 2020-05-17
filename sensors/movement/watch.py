from utils.socketio_client import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 26
GPIO.setup(PIR_PIN, GPIO.IN)

@sio.event
def movement_state():
  sio.emit('movement_state')

while True:
  if GPIO.input(PIR_PIN): movement_state()
  time.sleep(0.1)
