import os, sys
__author__ = 'roothaxor'
__description__  = 'Personal Use Code for performing Anti-forensic actions'

To_Do_Manually_Once = '''

Disable last access logs ( ADMIN Priv's ) - digital timeline anti-forensic
Command : fsutil behavior set disablelastaccess 1

'''
#delete run history ( /va switch delete all values inside it, /f switch force )
os.system('reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f')

#Stop Seach History from Services, delete search history files contains vast information
# /Q swtich for quiet mode, /S switch for delete files from all subdirectories with attribute SYSTEM files
os.system('del /Q /S "%programdata%/\Microsoft\Search\Data\Applications\Windows\*.*" > nul')

#Remove USB logs in regservice
os.system('reg delete HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR /va /f')

#Remove hidden RECYCLE.BIN
os.system('rmdir /Q /S "C:\$RECYCLE.BIN" > nul')

#REM Clean Temp Folders
os.system('rmdir /Q /S "C:\Users\%username%\AppData\Local\Temp" > nul')
os.system('mkdir "C:\Users\%username%\AppData\Local\Temp" > nul')
os.system('rmdir /Q /S "C:\Users\%username%\AppData\LocalLow\Temp" > nul')
os.system('mkdir "C:\Users\%username%\AppData\LocalLow\Temp" > nul')
os.system('rmdir /Q /S "C:\Users\All Users\Temp" > nul')
os.system('mkdir "C:\Users\All Users\Temp" > nul')
os.system('rmdir /Q /S "C:\Program Files (x86)\Temp" > nul')
os.system('mkdir "C:\Program Files (x86)\Temp" > nul')
os.system('del /Q /S "C:\Users\%username%\Contacts\*.*" > nul')
#del /Q /S "C:\Users\%username%\Downloads\*.*" > nul') Do not mess untill you know
os.system('del /Q /S "C:\Users\%username%\Music\*.*" > nul')
os.system('del /Q /S "C:\Users\%username%\Pictures\*.*" > nul')
os.system('del /Q /S "C:\Users\%username%\Videos\*.*" > nul')
os.system('del /Q /S "C:\Users\Public\*.*" > nul')

#Remove Pentest-Box User Commands history
os.system('del /Q /S "E:\PentestBox\config\.history" > nul')

#remove IDM-Download manager Downloaded history ( Exit program before run, Admin priv's )
os.system('taskkill /F /IM IDMan.exe')
os.system('reg delete HKEY_CURRENT_USER\Software\DownloadManager /f')

#Delete UserAssist - Digital timeline anti-forensic
os.system('reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist /f') 
'''There is a registry setting that keeps logs and dates of all launch programs, forensic experts can use this to build 
a digital timeline, we must disable this for computer security. Navigate to 
HKEY_Current_User/Software/Microsoft/Windows/Currentversion/ExplorerUser assist. 
Do this by hitting the Windows button on your keyboard and R at the same time and typing regedit in). 
You should see two subkeys called Count, delete both these keys. Now right-click the UserAssist key 
and create a new key named ‘Settings’. In this key (right clicking on it) create DWORD value named NoLog, 
set the value to 1.'''

#InternetExplorer Data
os.system('reg delete "HKCU\Software\Microsoft\Internet Explorer" /va /f')

#Remove Prefetch, Database file
#Can be disabled via HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters
os.system('cd %SystemRoot%\Prefetch | del *.db')
os.system('cd %SystemRoot%\Prefetch | del *.pf')



















