import os, sys
#Add links in links.txt.
#Downloaded videos will be saved at same directory
banner = '''
		Facebook Video Downloader .PY Powered
'''
os.system('cls')
print banner
with open('links.txt', 'r') as f:
	links = f.read().splitlines()
for i in links:
	os.system('python use-run-py-to-download-files.py '+i)