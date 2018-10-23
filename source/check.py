import pandas as pd 

import hashlib

import os 

import logging

def file_as_bytes(file):

    with file:

        return file.read()



def check(dirname,total):

	'''

	check the md5 for each file downloaded. if md5 does not match, report error.

	'''

	count = 0

	for idname in os.listdir(dirname):

		# list all the ids 

		if idname.find("-") != -1:

			idpath = dirname +"/" + idname



			for filename in os.listdir(idpath):

				# check the miRNA file

				if filename.find("-") != -1:

					filepath = idpath + "/" + filename

					filehash = hashlib.md5(file_as_bytes(open(filepath, 'rb'))).hexdigest()

					if df.loc[df['filename'] == filename].md5.values[0] != filehash:

						logging.info("file id {} download fails, please downlaod again".format(idname))

					else:

						count +=1

	if count == total:

		logging.info("successful downloads")





if __name__ == '__main__':



	logging.info(4*"="+"start checking"+4*"=")

	# the manifest file. modify file when use

	manifest_file = "manifest.txt"

	df = pd.read_csv(manifest_file,sep='\t')

	total = df.shape[0]

	

	# The directory that holds the data. Modify this when use.

	dirname = "live_miRNA"

	check(dirname,total)

	logging.info(4*"="+"check finished"+4*"=")
