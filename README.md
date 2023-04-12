# CIS600IoT

In this assignment, we are required to build a cloud-based IoT system which collects data from a set of virtual sensors that are deployed to collect environmental information using the MQTT protocol to display the following information: 
a) Display the latest sensor data values received from all the sensors of a specified environmental station.
b) Display the sensor data values received during the last five hours from all environmental station of a specified sensor.

I have used ThingsBoard to perform the above. The code files in this repository were used to generate sensor data for a period of 5 hours and this data was sent to the telemetry profile of each individual device using their access token. 
