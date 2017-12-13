# Web-Scraper
Ari Grayzel web scraper for IB CS using Python 2.7.x

Before you run the .py file you need to open up the .py file and replace all of the twilio variables (phone number, SID, etc. to be your values. Otherwise the program won't run and you wont get texted).

To use, simply download and run the .py file. You can put the .py inside a virtual environment if you want but this is not neccesary. When you run the program there are some error messages but you can ignore them as they don't actually affect the code.
Enter the url of the website you wish the scrape. Make sure you surround it in quotation marks so that the program recognizes it as a string. (e.g. "https://youtube.com", NOT just https://youtube.com)
Enter the time delay (in seconds) in between website requests. IMPORTANT: DO NOT MAKE THIS LESS THAN ONE!!!
The program will run until a change happens, it will then report on if it detected a change in data and/or the number of tags on the page and the time at which the change was detected.


This code uses snippets from Mr. Walker and reference from https://docs.python.org/2/library/htmlparser.html
