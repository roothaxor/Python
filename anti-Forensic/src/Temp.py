import os, sys
def clean():
	#REM Clean Temp Folders
	print "\n[+] Temp Files/Folder Clean Sequence Start [+]"
	print "\nDeleting \AppData\Local\Temp"
	os.system('rmdir /Q /S "C:\Users\%username%\AppData\Local\Temp" > nul')
	os.system('mkdir "C:\Users\%username%\AppData\Local\Temp" > nul')
	print "Deleting \AppData\LocalLow\Temp"
	os.system('rmdir /Q /S "C:\Users\%username%\AppData\LocalLow\Temp" > nul')
	os.system('mkdir "C:\Users\%username%\AppData\LocalLow\Temp" > nul')
	print "Deleting C:\Users\All Users\Temp"
	os.system('rmdir /Q /S "C:\Users\All Users\Temp" > nul')
	os.system('mkdir "C:\Users\All Users\Temp" > nul')
	print "Deleting C:\Program Files (x86)\Temp"
	os.system('rmdir /Q /S "C:\Program Files (x86)\Temp" > nul')
	os.system('mkdir "C:\Program Files (x86)\Temp" > nul')
	print "Deleting Contacts"
	os.system('del /Q /S "C:\Users\%username%\Contacts\*.*" > nul')
	#del /Q /S "C:\Users\%username%\Downloads\*.*" > nul') Do not mess untill you know
	print "Deleting Music"
	os.system('del /Q /S "C:\Users\%username%\Music\*.*" > nul')
	print "Deleting Pictures"
	os.system('del /Q /S "C:\Users\%username%\Pictures\*.*" > nul')
	print "Deleting Videos"
	os.system('del /Q /S "C:\Users\%username%\Videos\*.*" > nul')
	print "Deleting C:\Users\Public"
	os.system('del /Q /S "C:\Users\Public\*.*" > nul')
	print "[+] Temp Files/Folder Clean Sequence Stop [+]\n"