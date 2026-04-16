@echo off
set BOT_TOKEN=8272885781:AAE1z9tH2waZRu2gSeyd1KoV_6U8utxeZaA
cd /d "%~dp0"
:loop
python bot.py
echo Bot crashed, restarting in 5 seconds...
timeout /t 5 /nobreak >nul
goto loop
