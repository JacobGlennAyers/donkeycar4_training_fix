# used to go through directories and check filesize
import os
# used for command line arguments
import sys
# used to copy contets from the old folder into the new folder
import shutil

# sys.argv[1] ==> path to the data folder
# sys.argv[2] ==> path to the new data folder


# initializing a set that will contain the filenames of all of the faulty images
faulty_image_set = set()
# Walking through the directory passed in by the user. Should be data/images/
for root, dirs, files in os.walk(sys.argv[1]+"/images/"):
	# looping through each file in the relevant folder
	for file in files:
		# making sure only the images are looked at
		if file.endswith(".jpg"):
			#print(os.path.getsize(root+file))
			# checking if the image is either all black or a faulty recording
			if os.path.getsize(root+file) < 1000:
				# adding to the bad image set
				faulty_image_set.add(file)


# copying the old directory to the new
shutil.copytree(sys.argv[1],sys.argv[2])

# Deleting references to faulty files

for root, dirs, files in os.walk(sys.argv[1]+'/'):
	# going through all files in the directory
	for file in files:
		# Looking into the catalog files
		if file.endswith(".catalog"):
			print(file)
			# opening the catalog files in read mode
			with open(root+file,'r') as catalog_file_read:
				# Creating a list of lines to go through
				lines = catalog_file_read.readlines()
				# creating the fixed manifest file in the new directory
				with open(sys.argv[2]+'/'+file,'w') as catalog_file_write:
					# looping through each line in the read in file
					for line in lines:
						# reading in the filename from the line
						filename = line.split('\"')[11]
						if filename in faulty_image_set:
							print(filename + "is faulty\n")
							continue
						catalog_file_write.write(line)
						
