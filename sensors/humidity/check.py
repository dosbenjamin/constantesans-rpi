from main import *

@sio.on('humidity_check')
def humidity_check():
  humidity = Adafruit_DHT.read_retry(sensor, DHT11_pin)[0]
  humidity_state(humidity)
