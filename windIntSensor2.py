import os
import random
import time

# set the command to publish to Thingsboard
mqtt_cmd = 'mosquitto_pub -d -q 1 -h "mqtt.thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "KpujAwwbrUmupPzb7m0j" -m'

# loop for 5 hours (18000 seconds)
for i in range(18000):
    # generate a random windSensor value
    windSensor = random.randint(-50, 50)
    # build the message payload with the windSensor value
    payload = '{"windIntensity":' + str(windSensor) + '}'
    # build the full command with the message payload
    full_cmd = mqtt_cmd + ' ' + payload
    # execute the command
    os.system(full_cmd)
    # wait for 1 second before the next iteration
    time.sleep(1)
