INTRODUCTION:

This is a Python script to extract feed from Facebook account and store it in a txt file.
Python 2.7 and PowerShell to execute it.

NOTE: 
original request was to get the feeds from Expedia's Facebook page but Facebook reuires a APP review process to read from public pages, hence i couldn’t achieve it. Instead this Code retirves feed from one's own Facebook account.
Facebook App Review process :  https://developers.facebook.com/docs/apps/review/




SOLUTION EXPLANATION:
1) Code attempts to call the Facebook graph api to get the list of feeds. The parameter "feed.limit(8)" will give me last 8 Facebook posts.

2) An access token is required to access the graph-api which is set as environment variable(fb_access_token)

3) Once I received the json, opened a txt file and dump the created_Time and message into it.

4)This code on execution generates a fb_feed.txt file in the same directory.



HOW TO EXECUTE IT:

1) Create an 'APP' in Facebook to genterate access token.
  https://developers.facebook.com/tools/explorer/

2) set the access token as an env variableon your mmachine
   open Powershell: Execute $env:fb_access_token="<access_token>"

3) run the command to execute the code:
   python fb_feed.py

4) File(fb_feed.txt) will be generated in the present working directory.



DEMO VIDEO
Demo and Code walkthrough video : Q1 Demo Video.mp4
