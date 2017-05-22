import csv
import os

f = open("twitter_davis_followers.csv", 'rb') 
reader = csv.reader(f)
usernames = list(reader) #load data in a list of lists

for i in usernames:
	handle = i[0]
	command = 'python twitteranalyzer.py ' + handle
	os.system(command)

