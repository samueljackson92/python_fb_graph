import requests
import json
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
	request = requests.get(FOAUTH_FB_API + query, auth=AUTH)
	return request

#convert the data returned to JSON
def queryJSON(url):
	data = query(url)
	return json.loads(data.text)
