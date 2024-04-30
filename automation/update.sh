cd ..
if [ $(date +%d) -eq 1 ] ; then
    ./venv/Scripts/python.exe scraper/main.py
    git pull
    git add .
    git commit -m "automatic update $(date +%d/%m/%y)"
    git push origin main
fi
