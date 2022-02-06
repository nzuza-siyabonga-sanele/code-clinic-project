from __future__ import print_function
from asyncio import events
from calendar import calendar
import json
import datetime
import os.path

import pickle
from pathlib import Path
from urllib import response
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 
'https://www.googleapis.com/auth/calendar']


#TODO authenticate and login user
def authenticate_account():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        return build('calendar', 'v3', credentials=creds)
       
    except HttpError as error:
        print('An error occurred: %s' % error)
    

def register_user():
    email =  get_user_input("Email Address: ",str).strip()
    campus  = get_user_input("Campus -(DBN/CPT/JHB): ",str)
    service = authenticate_account()
    calendars =  get_user_calender(service, email)
    print(calendars)


def get_user_calender(service, email):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    calendars = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=7, singleEvents=True, 
                                              orderBy='startTime').execute().get('items', [])
                            

    return calendars


 
def get_user_input(question, return_type):
    if return_type is int:

        response = input(question)
        while not response.isnumeric():
            response = input(question)
        return response

    return input(question)



#TODO store user information
def store_user_info():
    pass




       

    