import os, sys
__info__ = '''
There is a registry setting that keeps logs and dates of all launch programs, forensic experts can use this to build 
a digital timeline, we must disable this for computer security. Navigate to 
HKEY_Current_User/Software/Microsoft/Windows/Currentversion/ExplorerUser assist. 
Do this by hitting the Windows button on your keyboard and R at the same time and typing regedit in). 
You should see two subkeys called Count, delete both these keys. Now right-click the UserAssist key 
and create a new key named Settings. In this key (right clicking on it) create DWORD value named NoLog, 
set the value to 1
'''
def clean():
	print "\n[+] UserAssist Clean Sequence Start [+]"
	print "\nTimeline anti-forensic Removing Registry Key UserAssist"
	#Delete UserAssist - Digital timeline anti-forensic
	os.system('reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist /f') 
	print "\n[+] UserAssist Clean Sequence Stop [+]\n"