#!/bin/bash
month=`date +"%m"`
day=`date +"%d"`

cd personal-activity

if [ $day -eq 26 ] && [ $month -eq 5 ]
then
    ./venv/Scripts/python.exe scraper/main.py
    git pull
    git add .
    git commit -m "automatic update $(date +"%d-%m-%Y")"
    git reset --soft HEAD~1
fi

