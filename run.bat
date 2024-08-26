@echo off

set PYTHONPATH=%PYTHONPATH%;%~dp0/main

py main.py

pause >nul