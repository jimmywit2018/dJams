from __future__ import print_function
import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
import os
import pymongo
from pymongo import MongoClient
from pprint import pprint
import json
import re

client = pymongo.MongoClient("mongodb+srv://dannyzidelis:DJAMSdurga1!@djamscluster-u6bx0.mongodb.net/dJamsDB")

db = client.dJamsDB

coll = db.ScheduledTimes
with open(r'C:\Users\zidel\Documents\GitHub\dJams\templates\example.json') as infile:
     example = json.loads(infile.read())
email = example['email'][0]
# print(email)
#print(client.database_names())
#print(coll)

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    currentdatetime=datetime.datetime.now()

    currentdatetime= currentdatetime.isoformat()

    currentdate= currentdatetime[:-16]
    currenttime= currentdatetime[11:-7]
    # print(currentdatetime)
    # print(currentdate, currenttime)
    #print(dir_path)
    #files = [f for f in os.listdir(dir_path) if os.path.isfile(f)]
    #for f in files:
        #print(f)
    """Shows basic usage of the Google Calendar API.

    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 20 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=20, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        #start time of event, shown as: 2018-09-07T12:01:00-04:00
        start = event['start'].get('dateTime', event['start'].get('date'))
        startdate= start[:-15]
        starttime= start[11:-6]
        #end time of event, shown as: 2018-09-29T21:00:00-04:00
        end = event['end'].get('dateTime', event['end'].get('date'))
        enddate= end[:-15]
        endtime= end[11:-6]
        #prints out all the data
        # if(startdate==enddate):
        #     print(startdate, starttime, "-",endtime, event['summary'])
        # else:
        #     print(startdate,starttime,"-",enddate,endtime, event['summary'])

        #selects what goes into the database
        if event['summary'].upper() == "WORK":
            sched_rec = {"email": email, "name":event['summary'], "startdate": startdate, "enddate": enddate, "starttime":starttime,"endtime":endtime}
            rec_id = coll.insert_one(sched_rec)
            #print("Data inserted with record ids", rec_id)
        elif event['summary'].upper() == "WORK OUT":
            sched_rec = {"email": email, "name":event['summary'], "startdate": startdate, "enddate": enddate, "starttime":starttime,"endtime":endtime}
            rec_id = coll.insert_one(sched_rec)
            #print("Data inserted with record ids", rec_id)
        elif event['summary'].upper() == "GYM":
            sched_rec = {"email": email, "name":event['summary'], "startdate": startdate, "enddate": enddate, "starttime":starttime,"endtime":endtime}
            rec_id = coll.insert_one(sched_rec)
            #print("Data inserted with record ids", rec_id)
        elif event['summary'].upper() == "RELAX":
            sched_rec = {"email": email, "name":event['summary'], "startdate": startdate, "enddate": enddate, "starttime":starttime,"endtime":endtime}
            rec_id = coll.insert_one(sched_rec)
            #print("Data inserted with record ids", rec_id)
    # cursor = coll.find()
    # for record in cursor:
    #     print(record)
    # print(startdate, starttime)
    # print(enddate, endtime)



if __name__ == '__main__':
    main()
