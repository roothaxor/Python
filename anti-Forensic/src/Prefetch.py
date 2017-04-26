import os, sys, time
def clean():
	print "\n[+] C:/Windows/Prefetch Clean Sequence Start [+]"
	#Remove Prefetch, Database file
	#Can be disabled via 
	#HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters
	print "\nDeleting Database (*.db) Files"
	os.chdir('C:/Windows/Prefetch')
	os.system('del *.db')
	time.sleep(2)
	print "Deleting Prefetch (*.pf) Files"
	os.system('del *.pf')
	print "\n[+] C:/Windows/Prefetch Clean Sequence Stop [+]\n"