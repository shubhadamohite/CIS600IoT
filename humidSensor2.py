import os
import random
import time

# set the command to publish to Thingsboard
mqtt_cmd = 'mosquitto_pub -d -q 1 -h "mqtt.thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "k6HIAPTTXb2vFlrh85hf" -m'

# loop for 5 hours (18000 seconds)
for i in range(18000):
    # generate a random humidity value
    humidity = random.randint(0, 100)
    # build the message payload with the humidity value
    payload = '{"humidity":' + str(humidity) + '}'
    # build the full command with the message payload
    full_cmd = mqtt_cmd + ' ' + payload
    # execute the command
    os.system(full_cmd)
    # wait for 1 second before the next iteration
    time.sleep(1)
