@echo off
title VertoX Setup

echo Installing required Python packages from requirements.txt...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
:: requirements.txt'yi sil
del /f /q "requirements.txt"
if %errorlevel% neq 0 (
    echo Failed to install required packages. Please check the requirements.txt file.
    exit /b 1
)
echo.
echo Running setup.py...
python setup.py