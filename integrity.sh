#!/bin/bash

read -p "Enter file name: " file

# Generate hash
sha256sum "$file" > hash.txt

echo "Hash stored in hash.txt"

echo "Checking integrity..."

sha256sum -c hash.txt