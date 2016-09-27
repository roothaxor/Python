import requests
import bs4
import time
from threading import Thread
from Queue import Queue	
import sys


def proxy_check(proxy):
	try:
		proxy = proxy.rstrip()
		proxy_judge = "http://www.proxyjudge.info/" # any proxy judge can go here
		
		proxyy={"http": "http://"+proxy}
		r = requests.get(proxy_judge,proxies= proxyy,timeout=10) 
		soup = bs4.BeautifulSoup(r.content,"html.parser") 
		data = soup.find_all("body") 
		
		
		for item in data:
		
			#Low anonymity
			if "HTTP_X_FORWARDED_FOR" in item.text and "HTTP_X_FORWARDED_FOR = unknown" not in item.text :
				
				if("L" in sys.argv[3]):
					poxy_save_file = open(sys.argv[2], 'a')
					poxy_save_file.write(str(proxy)+'\n') # save proxy to file
					poxy_save_file.close()
					
					print str(proxy) + "	Low		Alive"
					
				time.sleep(5.5)
				
				#Medium anonymity
			elif "HTTP_X_FORWARDED_FOR = unknown" in item.text:
				
				if("M" in sys.argv[3]):
					poxy_save_file = open(sys.argv[2], 'a')
					poxy_save_file.write(str(proxy)+'\n') # save proxy to file
					poxy_save_file.close()
					
					print str(proxy) + "	Medium		Alive"
					
				time.sleep(5.5)
				
			# High anonymity
			elif "HTTP_X_FORWARDED_FOR" not in item.text and "HTTP_X_FORWARDED_FOR = unknown" not in item.text and "REMOTE_ADDR" in item.text :
				
				
				if("H" in sys.argv[3]):
					poxy_save_file = open(sys.argv[2], 'a')
					poxy_save_file.write(str(proxy)+'\n') # save proxy to file
					poxy_save_file.close()
					
					print str(proxy) + "	High		Alive"
					
				time.sleep(5.5)
			else:
				time.sleep(5.5)
	except requests.exceptions.Timeout:
		time.sleep(.5)
	  #print str(proxy) + " Dead"
	except:
		time.sleep(.5)
		#print str(proxy) + " Dead"
	time.sleep(.5)



def get_proxy(i,q):
	#print "Starting thread [" + str(i)+"]\n"
	time.sleep(5)
	while True:
		proxy = q.get() # get proxy
		proxy_check(proxy)
		q.task_done() 	

if(len(sys.argv) < 4):
		print("\n\nHelp: proxy.py list.txt output.txt LMH \nPlease Put Proxy list in this form = 10.0.0.0:8080 (Using ':' before Port Number) \n\nFilter ANONYMITY LEVEL\n	L = Low\n	M = Med\n	H = High\n\nSuppose You need only High Anonymity Proxy List Use = proxy.py list.txt output.txt H\n")
else:
	num_threads = 300
	q_queue = Queue()
	
	for i in range(num_threads): # number of threads to spin up
		worker = Thread(target=get_proxy, args=(i,q_queue,))
		worker.setDaemon(True)
		worker.start()
		
	with open(sys.argv[1]) as fp:
		for line in fp:
			q_queue.put(line) # put list in queue
			
	q_queue.join() # wehen queue is empty exit
	print 'Done!!'