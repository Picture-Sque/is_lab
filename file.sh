#!/bin/bash

i=1

for file in *
do
    if [ -f "$file" ]
    then
        date=$(stat -c %y "$file" | cut -d' ' -f1)
        echo "$i. $file - $date"
        ((i++))
    fi
done