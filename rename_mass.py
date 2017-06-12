import os, sys
banner = '''

String remove from multiple file names- v.0.1.2

'''
curpath = os.getcwd()
try:
	inn = str(raw_input('\n\nInput String : '))
except KeyboardInterrupt:
	print "Order: Close this program!\n\n"
	sys.exit()
paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(curpath)
        for filename in filenames)

for path in paths:
	newname = path.replace(inn, '')
	if newname != path:
		os.rename(path, newname)

print "\nSuccess!"
