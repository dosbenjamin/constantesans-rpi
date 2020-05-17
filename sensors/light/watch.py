from main import *
import time

time.sleep(0.5)
light_old = not GPIO.input(LIGHT_PIN)

while True:
  if GPIO.input(LIGHT_PIN) != light_old:
    if GPIO.input(LIGHT_PIN): light_state('on')
    else: light_state('off')

  light_old = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
