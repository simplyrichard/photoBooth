#!/bin/bash

#Capture current time for timestamp
DATE=$(date +"%Y-%m-%d_%H%M")

#Take photo using webcam and save with timestamp as name
fswebcam -r 1280x720 --no-banner /var/www/webcam/$DATE.jpg
