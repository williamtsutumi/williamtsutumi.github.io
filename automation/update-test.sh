cd ..
if [ $(date +%d) -eq 17 ] ; then
    ./venv/Scripts/python.exe scraper/main.py
    git pull
    git add .
    git commit -m "automatic update $(date +%d/%m/%y)"
    git reset --soft HEAD~1
fi
