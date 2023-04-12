import os
import random
import time

# set the command to publish to Thingsboard
mqtt_cmd = 'mosquitto_pub -d -q 1 -h "mqtt.thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "iOV9nnaTNJ0tdrky2UFR" -m'

# loop for 5 hours (18000 seconds)
for i in range(18000):
    # generate a random co2 value
    co2 = random.randint(300, 2000)
    # build the message payload with the co2 value
    payload = '{"co2":' + str(co2) + '}'
    # build the full command with the message payload
    full_cmd = mqtt_cmd + ' ' + payload
    # execute the command
    os.system(full_cmd)
    # wait for 1 second before the next iteration
    time.sleep(1)
