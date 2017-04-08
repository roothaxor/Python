#Simple Code For Removing The Exif Data From Files
#Exif Data Contains Values which can be peril for your privacy
#Make a folder drop files in that folder, also drop this script in same folder and run.
#Have a Happy Privacy before uploading content online
from PIL import Image
import os, sys

'''Old works single file work, sucks

image_file = raw_input(" Enter the file: ")

if os.path.isfile(image_file):

	
	directory, filename = os.path.split(image_file)

	image = Image.open(image_file)

	data = list(image.getdata())

	image_without_exif = Image.new(image.mode, image.size)

	image_without_exif.putdata(data)

	image_without_exif.save(directory + "/notrace_" + filename)

	print(" file saved: %s/x_%s" % (directory, filename))

	sys.exit(0)
else:
	print(" File Path not correct or found try again Sucka !")
	
	sys.exit(1)'''
#exif remove data from files directorys
relevant_path = os.getcwd()
included_extenstions = ['jpg', 'bmp', 'png', 'gif']
l = [files for files in os.listdir(relevant_path)
          	if any(files.endswith(ext) for ext in included_extenstions)]
for image_file in l:
	image  = Image.open(image_file)
	data = list(image.getdata())
	image_without_exif = Image.new(image.mode, image.size)
	image_without_exif.putdata(data)
	directory = os.getcwd()
	image_without_exif.save(directory + "/ex_" + image_file)
	print "Exif data removed, saved as %s\ex_%s" % (directory, image_file)
	delete = os.remove(image_file)
print "\n\nFiles with exif data deleted automatically, thankyou"
