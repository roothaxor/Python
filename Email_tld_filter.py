#!/usr/bin/python
#Email Filter multi thread.
#Fully automated Script, Single Command in Terminal and woooohooooo
#Copy this code, make a script.py
#Then put files with emails in same directory of script.py, open cmd run the script and wait. :)
#Usage:python script.py 13 ( 13 is number of threads you want to run, default is 10 )
import re, os , sys, threading, time

def splitlist(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def get_addr(email_addr):
	maybe = email_addr.split('@')[1]
	return maybe.split('.')[0]

def main(emails):
	#Domain tld's
	ru = ['yandex']
	au = ['bigpond']
	microsoft_family=['hotmail', 'live', 'outlook', 'msn']
	yahoo_family=['yahoo', 'ymail', 'yahoomail', 'btinternet', 'bt', 'rocketmail', 'sky']
	google_family=['gmail', 'google', 'googlemail']
	aol_family=['aol']

	try:
		for i in emails:
			dmn = get_addr(str(i)) #Confused
			#dmn = dmn.strip('\t\n\r')#Output: gmail.com, aol.com
			for x in aol_family: #Send Loops =D
				if str(dmn) == x:
					file = open('result/aol_fam.txt', 'a')
					file.write(i)
			for xx in yahoo_family:
				if str(dmn) == xx:
					file = open('result/yahoo_fam.txt', 'a')
					file.write(i)
			for xxx in google_family:
				if str(dmn) == xxx:
					file = open('result/google_fam.txt', 'a')
					file.write(i)
			for xxxx in microsoft_family:
				if str(dmn) == xxxx:
					file = open('result/microsoft_fam.txt', 'a')
					file.write(i)
			for xz in au:
				if str(dmn) == xz:
					file = open('result/au_tld.txt', 'a')
					file.write(i)
			for zx in ru:
				if str(dmn) == zx:
					file = open('result/ru_tld.txt', 'a')
					file.write(i)
			if str(dmn) not in ru + au + microsoft_family + google_family + yahoo_family + aol_family:
				file = open('result/unknown.txt', 'a')
				file.write(i)
	except Exception as e:
		pass

if __name__ == '__main__':
	global shit
	try:
		shit = int(sys.argv[1])
	except IndexError:
		shit = 9
		pass
	start_time = time.time()
	if not os.path.isdir('result'):
		os.mkdir('result')
	listdir = os.getcwd()
	ext = ['.txt']
	files = [f for f in os.listdir(listdir) if f.endswith(tuple(ext))] #Use tuple() for multiple
	for file in files:
		startx = open(file, 'r').readlines()
		lists = splitlist(startx, shit) # 0 - 8, seems to have no 8
		for i in range(0,shit): # 0 - 8
			t = threading.Thread(target=main, args=(lists[i],))
			tp =  t.start()
			print("Task {} assigned to thread: {}".format(i, threading.current_thread().getName()))
	print("\nTotal active threads : {}".format(threading.activeCount()))
	took = time.time() - start_time
	print "\nCore Execution time : ", str(took)[:4]+" Seconds","\n\nFiltering processes have been started, Listen songs for a while."
	startt = time.time()
	t.join()
	stopp = time.time() - startt
	print "\nTasks Completed, Total time: ",str(stopp)[:4],"Seconds"
