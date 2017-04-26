import os, sys
def clean():
	print "\n[+] USBLOG History Clean Sequence Start [+]"
	#Remove USB logs in regservice
	print "\nRemoving Registry Key USBSTOR"
	os.system('reg delete HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR /va /f')
	print "\n[+] USBLOG History Clean Sequence Stop [+]\n"