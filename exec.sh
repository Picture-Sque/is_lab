#!/bin/bash

read -p "Enter the file name: " file

chmod -x "$file"

echo "Execution permission removed for $file"