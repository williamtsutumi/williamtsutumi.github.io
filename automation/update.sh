#!/bin/bash

month="7"

cd personal-activity

if [ $month -le $(date +"%m") ]
then
    echo "updating github pages"
    git pull
    ./venv/Scripts/python.exe scraper/main.py
    git add .
    git commit -m "automatic update $(date +"%d-%m-%Y")"
    git push origin main
else
    echo "github pages already updated this month"
fi

cd

