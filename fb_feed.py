import json
import os
import requests

access_token=os.environ['fb_access_token']

params = (
    ('fields', 'feed.limit(8)'),
    ('access_token', access_token),
)

data = 'Content'

response = requests.post('https://graph.facebook.com/v2.5/me', params=params, data=data)
feed=json.loads(response.content)['feed']['data']

f = open('fb_feed.txt','w')
for data in feed:
	if 'message' in data:
		create_date=json.dumps(data['created_time']).strip('"')
		message=json.dumps(data['message']).strip('"')
		f.write('Created time:'+create_date +'\n')
		f.write('message:'+ message +'\n\n')
	
f.close()		