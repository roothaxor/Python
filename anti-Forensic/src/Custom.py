import os, sys, time
def clean():
	print "\n[+] Custom Clean Sequence Start [+]"
	#Remove Pentest-Box User Commands history
	print "\nDeleting PentestBox Command History"
	os.system('del /Q /S "E:\PentestBox\config\.history" > nul')
	#remove IDM-Download manager Downloaded history ( Exit program before run, Admin priv's )
	print "Clearing IDM-Download Manager Mess...."
	print "Killing the IDMan.exe Proccess"
	os.system('taskkill /F /IM IDMan.exe')
	time.sleep(7)
	print "Removing Registry Key DownloadManager"
	os.system('reg delete HKEY_CURRENT_USER\Software\DownloadManager /f')
	#InternetExplorer Data
	print "Removing Registry Key Internet Explorer"
	os.system('reg delete "HKCU\Software\Microsoft\Internet Explorer" /va /f')
	print "\n[+] Custom Clean Sequence Stop [+]\n"