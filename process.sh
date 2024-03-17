#!/bin/bash

# Check if argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <string>"
    exit 1
fi

# Step 1: Generate audio file
whisper "$1".mp3 --model medium --task transcribe --language "$2"

# Step 2: Wait for "argument.txt" to be generated
while [ ! -f "$1.txt" ]; do
    sleep 1
done

python -u "/Users/tanaykumar/personal/coding/epoch/whisper-model/final.py" "$1" "$2"






