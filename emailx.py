#!/usr/bin/env python
#updated on 28/dec/2k17 @root_haxor
#fixed code errors
#emailx directory will contain the list of files, result (inside the emailx dir) directory will contain the final result files.
# ! Warning !: Make sure you move the final result file to another folder after script execution.
try:
    import re
except ImportError:
    print '[!] Failed to Import regex ( re )'
    try:
        choice = raw_input('[*] Wana install regex? [y/n] ')
    except KeyboardInterrupt:
        sys.exit('\n[!] User Interrupted Choice')
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install regex... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 're'])
            import re
            print '[DONE]'
        except Exception:
            sys.exit("[FAIL]")
    elif choice.strip().lower()[0] == 'n':
        sys.exit('[*] User Denied Auto-install')
    else:
        sys.exit('[!] Invalid Decision')

try:
    import timeit
except ImportError:
    print '[!] Failed to Import timeit'
    try:
        choice = raw_input('[*] Wana install timeit module? [y/n] ')
    except KeyboardInterrupt:
        sys.exit('\n[!] User Interrupted Choice')
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install timeit... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'timeit'])
            import timeit
            print '[DONE]'
        except Exception:
            sys.exit("[FAIL]")
    elif choice.strip().lower()[0] == 'n':
        sys.exit('[*] User Denied Auto-install')
    else:
        sys.exit('[!] Invalid Decision')
try:
    import termcolor
except ImportError:
    print '[!] Failed to Import termcolor'
    try:
        choice = raw_input('[*] Wana install termcolor module? [y/n] ')
    except KeyboardInterrupt:
        sys.exit('\n[!] User Interrupted Choice')
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install termcolor... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'termcolor'])
            from termcolor import colored
            print '[DONE]'
        except Exception:
            sys.exit("[FAIL]")
    elif choice.strip().lower()[0] == 'n':
        sys.exit('[*] User Denied Auto-install')
    else:
        sys.exit('[!] Invalid Decision')

try:
    import colorama
except ImportError:
    print '[!] Failed to Import colorama'
    try:
        choice = raw_input('[*] Wana install colorama module? [y/n] ')
    except KeyboardInterrupt:
        sys.exit('\n[!] User Interrupted Choice')
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install colorama... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'colorama'])
            import colorama
            print '[DONE]'
        except Exception:
            sys.exit("[FAIL]")
    elif choice.strip().lower()[0] == 'n':
        sys.exit('[*] User Denied Auto-install')
    else:
        sys.exit('[!] Invalid Decision')

import os, sys
from sys import platform as _platform
from termcolor import colored
if _platform == 'win32':
    import colorama
    colorama.init()
def green(text):
    return colored(text, 'green', attrs=['bold'])
def cyan(text):
    return colored(text, 'cyan', attrs=['bold'])
def red(text):
    return colored(text, 'red', attrs=['bold'])
def yellow(text):
    return colored(text, 'yellow', attrs=['bold'])

#Email Regex
regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def main():
	os.system('cls')
	banner = '''\n 		  Feel the joy of automation with python
	          	  Developer: @root_haxor         
	usage
	'''
	print yellow(banner)
	try:
		raw_input("     		[+] PRESS ENTER TO TRIGGER THE SCRIPT [+]\n")
	except Exception:
		sys.exit("Forcefully exit...")
#Generator func, email filter using regex
def get_emails(file):
    with open(file) as f:
        for line in f:
            for email in re.findall(regex, line.lower()):
                if not email[0].startswith('//'):
                    yield email[0]

def removeduplicate(filename, output):
    s = set()
    with open(output, 'w') as out:
        for line in open(filename):
            if line not in s:
                out.write(line)
                s.add(line)

if __name__ == '__main__':
    main()
    #Start the timer
    start = timeit.default_timer()
    #Get current directory path
    dirc = os.getcwd()
    #Check if output file already exists then delete.
    listdir = dirc+'\emailx'
    if not os.path.exists(listdir):
        os.makedirs(listdir)
        sys.exit(red('\n[!] Put files in emailx directory'))

    os.chdir(listdir)
    if not os.path.exists('result'):
        os.makedirs('result')
    if os.path.isfile('result\output_combined.txt'):
        print red("\n[!] Output file already existed! OverWriting....")
        os.system('del result\output_combined.txt')
    #Add more extensions if needed
    ext = ['.sql', '.txt', '.log']
    #Listing current directory for files, with given extensions
    files = [f for f in os.listdir(listdir) if f.endswith(tuple(ext))]
    #if files are none break code
    if len(files) == 0:
        sys.exit(red("\n[!] No files in emailx directory."))
    #just a for loop for generator
    for onebyone in files:
        for email in get_emails(onebyone):
            wrt = open('result\output_combined.txt', 'a')
            wrt.write(email+"\n")
        #if you wanna use the commented code below, import datetime and add this line: to code datetime = datetime.datetime()
        #count = open('dup_final.txt', 'r').readlines()
        #report ='''\n#############################################################
######## Total no. of emails: %s, Y/M/D: %s ########
############ Say thankyou to author: @root_haxor ############
#############################################################\n'''%(len(count), datetime.date())
        #with file('dup_final.txt', 'r') as original: data = original.read()
        #with file('dup_final.txt', 'w') as modified: modified.write(report+'\n' + data)
        print cyan("Processing file: ")+onebyone
        #print cyan("Processing file: ")+onebyone+cyan(" Time: "),(timeit.timeit("get_emails(file)", setup="from __main__ import get_emails", number=10000))
    
    #stop timer
    stop = timeit.default_timer()
    #count the total between start and stop interval
    total_time = stop - start
    #divide into minutes and seconds
    mins, secs = divmod(total_time, 60)
    print cyan("\nTotal, %s files processing time: ")%(len(files))+("%s")%(float(str(secs)[:4]))+"s"+"\n"
    print green("\n[+] Combined output file path: ")+"result\output_combined.txt"
    print cyan("\n[+] Removing duplicates from combined list, please wait ! ")
    #start timer
    start = timeit.default_timer()
    #output files for result after duplicate removed from combined emails list
    finaloutput = "result\dup_output.txt"
    if os.path.isfile("result\dup_output.txt"):
        print red("[!] dup_output.txt already exists. OverWriting...")
        os.remove("result\dup_output.txt")
    try:
        removeduplicate('result\output_combined.txt', finaloutput)
    except Exception as e:
        sys.exit("\n[!] Error: No emails or files found.")
    stop = timeit.default_timer()
    totaltime = stop - start
    mins, secs = divmod(totaltime, 60)
    sec = float(str(secs)[:4])
    print green("[+] Duplicates removing succesful, took ")+"%ss"%(sec)
    print green("\n[+] Final output file path: ")+finaloutput