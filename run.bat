@echo off

python -m pip install -r requirements.txt

set PYTHONPATH=%PYTHONPATH%;%~dp0/main

py main.py

pause >nul