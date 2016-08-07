#this is simple code which deletes itself after execution 
#explanation: the self_path has __file__ which contains all the file functions
#can come handy in certain ways
import subprocess as sp
from os import path

# This gives us the absolute(full) path to this python script
self_path = path.abspath(__file__)

# Do stuff -- I just created a folder
sp.call(["mkdir", "/home/User/hp/Desktop/thinair"])

# At the end of the script, the file shreds itself
sp.call(["/usr/bin/shred", "-fuz" , self_path])

