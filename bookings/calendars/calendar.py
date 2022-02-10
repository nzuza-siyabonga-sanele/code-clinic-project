
from authentication import authentication
#get wethinkcode code clinics calendar

import datetime
from api_services import calender_service
from dateutil.parser import parse as dtparse
from datetime import datetime as dt
from tabulate import tabulate

service= calender_service.get_calendar_service()
#date and time coverter
def convert_to_RFC_datetime(year,month,day,hour,minute):
    dt =datetime.datetime(year,month,day,hour,minute,0).isoformat()+'z'
    return dt
#retrieves code clinic available slots
def get_code_clinic_calender():

    now = convert_to_RFC_datetime(2022,2,7,0,0)
    results = service.events().list(calendarId= 'codeclinics@wethinkcode.co.za', timein=now,
                                                maxResults = 7, singleEvents=True,
                                                orderBy= 'startTime').execute()

    events = results.get('items',[])

    #takes the start time and name of the next 7 events 

    Calendars= [['Date','summary','status']]
    for event in events:
        start=event['start'].get('dateTime',event['start'].get('date'))
        tmfmt = '%d %B, %H:%M %p'
        stime = dt.strftime(dtparse(start),format=tmfmt)
        booked = len(event['attendees'])
        if booked > 1:
            calendars.append([stime, event['summary'],"BOOKED"])
        else:
            Calendars.append([stime,event['summary'], "Available slot"])
    print(tabulate(Calendars,headers='firstrow'))

#retirieves user calendar
def get_user_calendar():

    now = convert_to_RFC_datetime(2022,2,7,0,0)
    results = service.events().list(calendarId= 'codeclinics@wethinkcode.co.za', timein=now,
                                                maxResults = 7, singleEvents=True,
                                                orderBy= 'startTime').execute()

    events = results.get('items',[])
    #takes the start time and name of the next 7 events

    calendars=[]
    for event in events:
        start=event['start'].get('dateTime',event['start'].get('date'))
        calendars.append((start,event['summary']))
    return calendars