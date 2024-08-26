@echo off

python -m pip install -r requirements.txt

set PYTHONPATH=%PYTHONPATH%;%~dp0\path\to\library
py main.py
pause >nul