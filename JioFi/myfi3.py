import urllib2, os, sys
from bs4 import BeautifulSoup as BS
banner = '''
 MYJIO - 3 Wifi Personal HostSpot Information 
'''
quote_page = 'http://192.168.225.1/cgi-bin/en-jio/mStatus.html'
page = urllib2.urlopen(quote_page)  
soup = BS(page, 'html.parser')  
r = soup.findAll('label')
my_data = "bandwidthValue: " + r[4].string + "\n" + "Up Time: "+ r[1].string + "\n" +"APN: "+r[8].string + "\n" +"Cell: " + r[9].string + "\n" +"rsrpValue: "+ r[11].string + "\n" +"rsrqValue: "+ r[12].string + "\n" +"sinrValue: " +r[13].string + "\n" +"Local IPv4: "+ r[14].string + "\n" +"Local Ipv6: "+ r[18].string + "\n" +"Router IP: " +r[26].string + "\n" +"Total Downloaded: "+ r[34].string + "\n" +"Total Uploaded: " +r[33].string + "\n" +"Battery: " +r[45].string +"     Level: "+ r[46].string + "\n" +"cpuMaxUsage: "+ r[54].string + "\n" +"cpuMinUsage: "+ r[55].string + "\n" +"maxMemoryUsage: "+ r[56].string + "\n" +"minMemoryUsage: " +r[57].string + "\n" +"CurrentDownRate: "+ r[61].string + "\n" +"Current Time: "+r[37].string + "\n" +"Router LocalADDr :" +r[36].string + "\n" +"SecurityModeValue: "+ r[31].string + "\n" +"Wifi Name: "+ r[23].string
os.system('cls')
print banner
print my_data
