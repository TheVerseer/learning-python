@echo off

python -m pip install -r requirements.txt

set PYTHONPATH=%PYTHONPATH%;%~dp0

py main/main.py

pause >nul