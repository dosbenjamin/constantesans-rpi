from utils.socketio_client import *
import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

@sio.event
def vibration_state():
  sio.emit('vibration_state')

def callback(channel):
  if GPIO.input(channel): vibration_state()
  else: vibration_state()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
  time.sleep(1)
