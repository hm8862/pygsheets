############################################################################################################
# Documentation: https://developers.google.com/sheets/api/quickstart/python
# Python client for Google Sheets
# For accessing and manipulating data in Google Sheets
############################################################################################################

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from config import Config
import datetime
import json
import pandas

basedir = os.path.abspath(os.path.dirname(__file__))

SCOPES = 'https://www.googleapis.com/auth/spreadsheets' # allow to read/write
CLIENT_SECRET_FILE = basedir + '/client_secret.json'
APPLICATION_NAME = 'Google Sheets API Client'

def get_credentials():
	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
		Credentials, the obtained credential.
	"""
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir,
								   'sheets.googleapis.com-gsheets-api-client.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)
		print('Storing credentials to ' + credential_path)
	return credentials

class pygsheetsApiClient:

	def __init__(self):
		# login via OAuth if credentials are stale, build API client
		self.credentials = get_credentials()

		http = self.credentials.authorize(httplib2.Http())
		discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
						'version=v4')
		self.service = discovery.build('sheets', 'v4', http=http,
								  discoveryServiceUrl=discoveryUrl)

	def append(self, spreadsheetId, rangeName, data, valueInputOption="RAW"):
		return self.service.spreadsheets().values().append(
						spreadsheetId=spreadsheetId, range=rangeName,
						valueInputOption=valueInputOption, body=data).execute()

	def getAll(self, spreadsheetId, rangeName, valueInputOption="RAW"):
		result = self.service.spreadsheets().values().get(
						spreadsheetId=spreadsheetId, range=rangeName).execute()
		
		header = result["values"].pop(0)
		return pandas.DataFrame(result["values"], columns=header)