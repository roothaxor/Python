import os, sys
def clean():
	#Stop Seach History from Services, delete search history files contains vast information
	# /Q swtich for quiet mode, /S switch for delete files from all subdirectories with attribute SYSTEM files
	print "\n[+] Search History Clean Sequence Start [+]"
	print "\nDeleting Search History Data"
	os.system('del /Q /S "%programdata%\Microsoft\Search\Data\Applications\Windows\*.*" > nul')
	print "\n[+] Search History Clean Sequence Stop [+]\n"