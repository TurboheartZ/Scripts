import csv
import sys
import json
from glob import glob
import os.path

# Get the translate option
option = sys.argv[1]
if option != "1" and option != "2":
	print 'option must be either 1 or 2 !'
	exit(0)
else:
	option = int(option) + 1	

# Read the csv file
result = {}
path = '*.csv'
for f in glob(path):
	csv_data = csv.reader(file(f))
	for row in csv_data:
		result[row[1]] = row[option]

# Write to json file
# If result.json already exist, fetch the value first

if os.path.isfile('result.json'):
	with open('result.json', 'r+') as outfile:
		try:
			prev_data = json.load(outfile)
			for key in prev_data:
				result[key] = prev_data[key]
		except ValueError:	
		 	print 'Value Error'
with open('result.json', 'w+') as outfile:
	json.dump(result, outfile, indent=4, sort_keys=True)	

# Print done	
print "Done"