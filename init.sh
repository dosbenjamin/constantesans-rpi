export PYTHONPATH="./"

# Start server
python3 server.py & sleep 0.5;

# Start light sensor
python3 sensors/light/light_update.py
# python3 sensors/light.py
