#Simple Code For Removing The Exif Data From Files
#Exif Data Contains Values which can be peril for your privacy
#Make a folder drop files in that folder, also drop this script in same folder and run.
#Have a Happy Privacy before uploading content online
from PIL import Image
import os, sys

image_file = raw_input(" Enter the file: ")

if os.path.isfile(image_file):

	directory, filename = os.path.split(image_file)

	image = Image.open(image_file)

	data = list(image.getdata())

	image_without_exif = Image.new(image.mode, image.size)

	image_without_exif.putdata(data)

	image_without_exif.save(directory + "/x_" + filename)

	print(" file saved: %s/x_%s" % (directory, filename))

	sys.exit(0)
else:
	print(" File Path not correct or found try again bitch !!!")
	
	sys.exit(1)