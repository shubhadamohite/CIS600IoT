# CIS600IoT

In this assignment, we are required to build a cloud-based IoT system which collects data from a set of virtual sensors that are deployed to collect environmental information using the MQTT protocol to display the following information: 

a) Display the latest sensor data values received from all the sensors of a specified environmental station.

b) Display the sensor data values received during the last five hours from all environmental station of a specified sensor.

I have used [ThingsBoard](https://demo.thingsboard.io/login) to perform the above. 
The code files in this repository were used to generate sensor data for a period of 5 hours and this data was sent to the telemetry profile of each individual device using their access token. 


# Installation steps for MQTT client on MaCOS: 

brew install mosquitto-clients

# Command to send the telemetry data to each individual device: 

mosquitto_pub -d -q 1 -h "mqtt.thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}

The above sends individual readings to the devices. 

The scripts I have written are doing the same over a period of five hours.

# To run the scripts and send data to individual devices use: 

python tempSensor1.py 

# The following interfaces were built using the dashboarding functionality of ThingsBoard: 
**
Virtual Station 1: **
<img width="1294" alt="image" src="https://user-images.githubusercontent.com/47294531/231549301-44daa02f-9357-4180-a238-f9ccfdb1c381.png">
**
Virtual Station 2: **
<img width="1294" alt="image" src="https://user-images.githubusercontent.com/47294531/231549603-4fc4d020-5a0b-42fb-b363-acadb8eced4e.png">




