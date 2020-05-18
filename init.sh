export PYTHONPATH="./"

# Start server
python3 server.py & sleep 0.5

# Start humidity sensor
python3 sensors/humidity/check.py & python3 sensors/humidity/watch.py &

# Start light sensor
python3 sensors/light/check.py & python3 sensors/light/watch.py &

# Start movement sensor
python3 sensors/movement/watch.py &

# Start temperature sensor
python3 sensors/temperature/check.py & python3 sensors/temperature/watch.py &

# start vibration sensor
python3 sensors/vibration/watch.py
