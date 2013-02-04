import requests
from requests.exceptions import HTTPError
import json
from sys import exit
from getpass import getpass

#Location of the foauth API
FOAUTH_FB_API = 'https://foauth.org/graph.facebook.com/'

#Variable to hold email and password
AUTH = None

#get the users authentication detials
def auth():
	global AUTH
	user, password = None, None

	#Collect data from user
	user = raw_input('Email: ')
	password = getpass()

	#If we have input, set them.
	if user and password:
		AUTH = user, password

#query the facebook API via foauth
def query(query):
	try:
		request = requests.get(FOAUTH_FB_API + query, auth=AUTH)
	   	request.raise_for_status()
	except HTTPError:
		print "Failed to get response from Facebook server."
		exit(-1)
	else:
		return request

#convert the data returned to JSON
def queryJSON(url):
	data = query(url)
	return json.loads(data.text)
