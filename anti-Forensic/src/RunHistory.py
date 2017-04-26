import os, sys
def clean():
	#delete run history ( /va switch delete all values inside it, /f switch force )
	print "\n[+] Run History Clean Sequence Start [+]"
	print "\nRemoving Registry Key RunMRU"
	os.system('reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f')
	print "\n[+] Run History Clean Sequence Stop [+]\n"