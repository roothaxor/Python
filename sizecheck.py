import urllib2, os, sys
import shutil
if os.name == 'posix':
    os.system ('clear')
else:
    os.system('cls')
def url():
    banner = """
    			Welcome MothaFucka. I Know i am useless, but you still using
    """
    print banner
    url = raw_input("Link You Wana check Size oF : ")
    response = urllib2.urlopen(url)
    result = len(response.read())
    final = result/float(1024)
    print "\n\nPage Size is : %s KB" % (round(final))
url()