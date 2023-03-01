#! ./.venv/bin/python3

import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
    ]
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds =tools.run_flow(flow, store)

yesterday = datetime.date.today() - datetime.timedelta(days = 1)
day_start = yesterday.strftime('%Y/%m/%d')
day_end = datetime.date.today().strftime('%Y/%m/%d')
query = 'after:{} before:{}'.format(day_start, day_end)

results = service.users().messages().list(userId='me', q=query).execute()

if not results.get('resultSizeEstimate'):
    print('No messages yesterday.')
    exit()
print('Total mail messages: ' + str(results['resultSizeEstimate']))
for message in results['messages']:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    print('Message snippet: {}'.format(msg['snippet']))
