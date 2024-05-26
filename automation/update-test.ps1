cd C:\Projetos\personal-activity

if ((Get-Date).day -eq 30) {
    ./venv/Scripts/python.exe main.py
    git pull
    git add .
    git commit -m "automatic update $((Get-Date).ToString('dd-MM-yyyy'))"
    git reset --soft HEAD~1
}
else {
    echo "hoje n eh dia 01"
}
