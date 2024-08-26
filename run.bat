@echo off
python -m pip --version
IF %ERRORLEVEL% NEQ 0 (
    echo Pip is not installed, installing pip...
    python -m ensurepip --upgrade
)

python -m pip install -r requirements.txt

py main.main.py
pause >nul