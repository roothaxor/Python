#!/usr/bin/python
#Email Filter multi thread.
#Python 2.7.x
#Copy this code and make a filter.py. Then put files with emails in same directory of filter.py, open cmd run the script and wait. :)
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
	except Exception:
		pass

if __name__ == '__main__':
	start_time = time.time()
	if not os.path.isdir('result'):
		os.mkdir('result')
	listdir = os.getcwd()
	ext = ['.txt']
	files = [f for f in os.listdir(listdir) if f.endswith(tuple(ext))] #Use tuple() for multiple
	for file in files:
		startx = open(file, 'r').readlines()
		lists = splitlist(startx, 9) # 2 meens 2, 9 means 9
		t = threading.Thread(target=main, args=(lists[0],))
		t1 = threading.Thread(target=main, args=(lists[1],))
		t2 = threading.Thread(target=main, args=(lists[2],))
		t3 = threading.Thread(target=main, args=(lists[3],))
		t4 = threading.Thread(target=main, args=(lists[4],))
		t5 = threading.Thread(target=main, args=(lists[5],))
		t6 = threading.Thread(target=main, args=(lists[6],))
		t7 = threading.Thread(target=main, args=(lists[7],))
		t8 = threading.Thread(target=main, args=(lists[8],))
		t.start()
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
	took = time.time() - start_time
	print "\nCore Execution time : ", took,"\n\nFiltering processes have been started, Listen songs for a while."
