import os, sys 
def clean():
	print "\n[+] C:/$RECYCLE.BIN Clean Sequence Start [+]"
	#Remove hidden RECYCLE.BIN
	print "\nRemoving Directory C:/$RECYCLE.BIN"
	os.system('rmdir /Q /S "C:\$RECYCLE.BIN" > nul')
	print "\n[+] C:/$RECYCLE.BIN Clean Sequence Stop [+]"