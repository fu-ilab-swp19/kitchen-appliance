# Sensor Simulator 

This program simulates sensors. To run, use `python main.py` in this directory.

Right now, two temperature sensors attached to water boilers will be simulated. The update interval of these is 2 seconds for the sensor with id 1 and 3 seconds for the sensor with id 2. This is defined in the `main.py` file. However, for testing purposes, the update speed is increased by the factor 10, meaning: the sensor with id 1 will give a new value every 0.2 seconds, and the sensor with id 2 will give a new value every 0.3 seconds.

The simulator simulates a simple, but fairly realistic temperature progress. The characteristics are:

* there is an ambient temperature
* there are active phases, where the temperature increases up to 100
* there are cooldown phases, where the temperature decreses down to the ambient temperature
* there is always a small error in the simulated sensor data

With every simulated sensor an TCP server socket (IPv6 only) is created. The IP address is `::1`, and the port will be written into the console. Any request on these sockets will be answered with the current sensor value.

To visualize the simulated sensor values, a small backend simulator is available in `backend-simulator`. When the sensor simulator program runs, the backend simulator can be executed with `python backend-simulator/main.py <port> <update-interval>`, where `<port>` must be replaced with the port of the server socket to connect to, and `<update-interval>` must be replaced with a float that specifies the sleep time between requests. An example execution is `python backend-simulator/main.py 49358 0.2` to request the sensor simulation whose server listens on port 49538 every 0.2 seconds. 

## Please note

Right now, both applications only terminate by killing its processes. Furthermore, the GUI of the backend simulator is not usable, because the sleep commands are synchronous and blocking.