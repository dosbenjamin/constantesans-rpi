from main import *

while True:
  temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)[1]
  temperature_state(temperature)
