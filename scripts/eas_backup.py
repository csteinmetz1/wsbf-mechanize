import os
import sys
import json
from datetime import datetime
import requests
from requests.auth import HTTPDigestAuth

eas = json.load(open("config.json"))['eas']

now = datetime.now()
form = {'StartDate': now.strftime("%m/%d/%Y"), 
		# first date - 01/01/2010
		'EndDate': now.strftime("%m/%d/%Y"),
		'NumRecs': 100,
		'xmlfile': 'xml file',
		'StartRec': 0,
		'ProcessedRec': 21}

# connect to eas server, authenticate, and grab data
session = requests.session()
auth = HTTPDigestAuth(eas['username'], eas['password'])
req = session.post(eas['log'], auth=auth, data=form) 

# save collected xml file to disk
if not os.path.isdir(eas['output']):
	os.makedirs(eas['output'])

filename = now.strftime("%Y%m%dT%H%M%S") + '.xml'
filepath = os.path.join(eas['output'], filename)

with open(filepath, 'w') as f:
    f.write(req.text)
