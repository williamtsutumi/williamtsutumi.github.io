#!/bin/bash
month="6"
cd personal-activity

if [ $month -le $(date +"%m") ]
then
    ./venv/Scripts/python.exe scraper/main.py
    git pull
    git add .
    git commit -m "automatic update $(date +"%d-%m-%Y")"
    git push origin main
fi
