#!/bin/bash

# Execute the first microservice
python3 travel/manage.py runserver &

# Store the process id in a variable called pid1
pid1=$!

# Execute the second microservice
python3 bus/manage.py runserver 8001 &

# Store the process id in a variable called pid2
pid2=$!

# Kill both processes when pressing CTRL + C
trap 'kill $pid1; kill $pid2' INT

# Wait for the processes to be killed
wait