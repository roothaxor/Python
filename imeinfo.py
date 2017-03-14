#!usr/bin/python
import urllib2, os, sys, time
from bs4 import BeautifulSoup as bs

imei = raw_input("Input IMEI Here: ")
if (len(imei) < 13):
	print "\n[+] Oops! Something Went Wrong Enter IMEI Correctly [+]" 
	exit()
elif (len(imei) > 13):
	print "\nProcessing Data on server! Wait a Minute "
link = "http://iphoneimei.info/?imei=%s"%(imei)
open = urllib2.urlopen(link).read()
soup = bs(open, 'html.parser')
t =  soup.findAll('span')
text = []
if (t[5].text == "Lost Mode"):
	stolen = "Phone is either Stolen or lost"
elif (t[5].text != "Lost Mode"):
	stolen = "Phone Activated"
#for x in range(0,14):
#	print t[x].text
banner = '''
Priv8 Imei Info Python Script 
'''
if (os.name == "nt"):
	os.system('cls')
	print banner
elif (os.name == "posix"):
	os.system('clear')
	print banner
hr = soup.findAll('a')
print "\n"+t[0].text + t[1].text +"\n"+ t[2].text + t[3].text +"\n"+ t[4].text + stolen + "\n"+ t[6].text + t[7].text +"\n" +t[8].text + t[9].text + "\n"+t[10].text +t[11].text+"\n"+t[12].text+t[13].text +"\n"+ "Check For Blacklist: " + hr[4]['href'] + "\n\n"+ "Gathering Information From Blacklist url ....\n"
time.sleep(3)
link1 = hr[4]['href']
open1 = urllib2.urlopen(link1).read()
soup = bs(open1, 'html.parser')
tt = soup.findAll('td')
text = []
print tt[0].text + tt[1].text +"\n"+ tt[2].text+ tt[3].text+"\n"+tt[4].text+tt[5].text+"\n"+tt[6].text+tt[7].text+"\n"+tt[8].text+tt[9].text+"\n"+tt[10].text+tt[11].text+"\n"+tt[12].text+tt[13].text+"\n"+tt[14].text+tt[15].text+"\n"+tt[16].text+tt[17].text+"\n"+tt[18].text+tt[19].text+"\n"+tt[20].text+tt[21].text+"\n"+tt[22].text+tt[23].text+"\n"+tt[24].text+tt[25].text+"\n"+tt[26].text+tt[27].text+"\n"+tt[28].text+tt[29].text+"\n"+tt[30].text+tt[31].text+"\n"+tt[32].text+tt[33].text+"\n"+tt[34].text+tt[35].text+"\n"+tt[36].text+tt[37].text+"\n"+tt[38].text+tt[39].text+"\n"+tt[40].text+tt[41].text+"\n"+tt[42].text+tt[43].text+"\n"+tt[44].text+tt[45].text
