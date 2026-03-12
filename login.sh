#!/bin/bash

read -p "Enter username: " user

while true
do
    if who | grep -w "$user" > /dev/null
    then
        echo "User $user has logged in."
        break
    else
        echo "User $user not logged in. Checking again in 30 seconds..."
        sleep 30
    fi
done