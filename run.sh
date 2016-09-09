#!/bin/bash

# Executes robotina in a loop.
# Helps to respawn the application if something went wrong

until python robotina.py; do
    echo "Robotina failed with $?. Restarting the bot..."
    sleep 1
done
