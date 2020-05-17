from main import *

@sio.on('temperature_check')
def temperature_check():
  temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)[1]
  temperature_state(temperature)
