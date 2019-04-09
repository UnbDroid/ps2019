#!/bin/sh

# Start the server process in background
python rasp_server.py &

# Start the main buttons sequence
python main.py

# If sequence finished
clear

echo "\033[5mReiniciando o sistema...\033[0m"

sleep 5

python menu_hacker.py