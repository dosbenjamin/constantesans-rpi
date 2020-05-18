from main import *

while True:
  humidity = Adafruit_DHT.read_retry(sensor, DHT11_pin)[0]
  humidity_state(humidity)
