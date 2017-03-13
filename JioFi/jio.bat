@echo off
title MiFi-3 Hotspot Info
mode con:cols=54 lines=30
:loop
python myfi3.py
timeout /t 0 >null
goto loop

