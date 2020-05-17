from main import *

@sio.on('light_check')
def light_check():
  if GPIO.input(LIGHT_PIN): light_state('on')
  else: light_state('off')
