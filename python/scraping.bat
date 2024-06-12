@echo off
setlocal

set lockfile="./sample-scraping.lock"

if exist %lockfile% (
    echo "exit batch file because another process is running."
    pause
    exit 1
)

echo %date% %time% > %lockfile%

pip install -U pip
pip install pipenv==2024.0.0
pipenv install
pipenv run start

del %lockfile%

endlocal
