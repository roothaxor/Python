import urllib2 
import time
from urllib2 import urlopen
file = open('abc.txt')
line = file.read()
words = line.split()
word = words

for url in word:
    print 'Checking URL {0}'.format(url)
    start = time.clock()
    try:
        response = urlopen(url)
        print response.getcode()
    except StandardError as e:
        print 'Checker: {0}'.format(e)

    print 'took {0}s\n'.format(time.clock() - start)