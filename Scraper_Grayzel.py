#scraper2
from HTMLParser import HTMLParser
import urllib2
import time
from datetime import date
#from datetime import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

#initialize variables
start_tags_before = 0
all_data_before = ""
start_tags_after = 0
all_data_after = ""
data_change = False
tags_change = False
time_input_works = False

#Twilio
account_sid = 'Oh'
auth_token = 'Youre'
twilio_phone_number = 'Talking about'
my_phone_number = 'Wermhat'

#create parser function
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global start_tags_after
		start_tags_after += 1 #record number of tags on page
		
	def handle_data(self, data):
		global all_data_after
		all_data_after = all_data_after + data #create one mega string of the data
parser = MyHTMLParser()

#get user inputs
user_url = input("What url would you like to scrape? (please enter with quotes surrounding)")

while time_input_works == False:
    delay = raw_input("Input time interval you want (input a number greater than 1)")
    try:
        delay = float(delay)
        if(delay > 1):
            print("Time interval has been accepted.")
            time_input_works = True
        else:
            print("Time interval that was inputted was too small.")
    except Exception:
        print("Input was not understood.")

text = raw_input("Would you like to get a text message if there was a change?")

#run once to establish initial values
response = urllib2.urlopen(user_url)
html = response.read()
parser.feed(html)
all_data_before = all_data_after
start_tags_before = start_tags_after
#reset 'after' values
start_tags_after = 0
all_data_after = ""




#main loop
while data_change == False and tags_change == False:
	global user_url
	global data_change
	global tags_change
	global delay
	response = urllib2.urlopen(user_url)
	html = response.read()	
	parser.feed(html)
	
	#print for debugging
	#print start_tags_after
	#print all_data_after
	
	if start_tags_after == start_tags_before:
		tags_change = False
	else:
		tags_change = True
	
	if all_data_after == all_data_before:
		data_change = False
	else:
		data_change = True
	
	#make current values previous
	all_data_before = all_data_after
	start_tags_before = start_tags_after
	
	#reset current values
	start_tags_after = 0
	all_data_after = ""
	

	
	#dont spam
	time.sleep(delay)


if data_change == True:
	print("The data has changed")
	if text.lower() == 'yes' or text.lower() == 'y':
		body = 'There was a change to the website!'
		client = Client(account_sid, auth_token)
        	client.messages.create(
        		body=body,
        		to=my_phone_number,
        		from_=twilio_phone_number)
		
if tags_change == True:
	print("The number of tags has changed")

print datetime.time(datetime.now())

