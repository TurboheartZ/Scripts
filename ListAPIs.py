#################################################
# This script is written by Mark.Zhang for the  #
# purpose of listing all the api urls and names #
# Hope this can be helpful for truckxi scm team #
# and anyone uses it.                           #
#                               ---Mark.Zhang   #
#################################################

# How to use it?
# 1, Put this python script right beside your project folder 
# 2, run 'python ListAPIs.py xxxx(your project folder)'

import json
from sets import Set
from glob import glob
import os
import sys
import re

print '#################################################'
print '# This script is written by Mark.Zhang for the  #'
print '# purpose of listing all the api urls and names #'
print '# Hope this can be helpful for truckxi scm team #'
print '# and anyone uses it.                           #'
print '#                               ---Mark.Zhang   #'
print '#################################################'

# Get the folder of Django Project
walk_dir = sys.argv[1]

# Compile the pattern for url lines
urlreg = re.compile(r"\s+url.+")

# Dive into each level-2 sub-folder to find url files
for subdirs in os.walk(walk_dir):
	appdir = subdirs[0].split("/")
	if len(appdir)>1 and appdir[1] != 'scm':
		path = subdirs[0]+'/urls.py'
		for f_name in glob(path):
			with open(f_name, 'r') as urlfile:
				for line in urlfile:
					if urlreg.match(line):
						line_components	= line.split(',')
						api_name = line_components[1].strip()
						api_url = 'v1/'+appdir[1]+'/'+line_components[0].split("'")[1][1:].strip()
						print '-------------------------------------------------------------'
						print 'URL:' 
						print api_url
						print 'NAME:'
						print api_name
