#!/bin/bash
month="7"
cd personal-activity

if [ $month -le $(date +"%m") ]
then
    echo "updating github pages"
    ./venv/Scripts/python.exe scraper/main.py
    git pull
    git add .
    git commit -m "automatic update $(date +"%d-%m-%Y")"
    git reset --hard HEAD~1
fi
