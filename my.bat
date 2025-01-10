@echo off
REM Clone the repository
git clone https://github.com/farooq-001/emil.git

REM Change file permissions (Windows does not support chmod, so this is optional)
REM You can skip this part or adjust according to your needs

REM Run the Python script
python3 emil\ip.py

REM Clean up by removing the cloned repository
rd /s /q emil
