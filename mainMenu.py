'''	Little GNU/Linux Assistant
	****************************
	This is the main menu of our assistant.
	From here, you can select how you'd like to interact with it. 
	Some of the functions come from libs we made, like News and Weather. 
	Currently, the Little Linux Assistant can: 
		- Pull up the news from you from a choice of a few different sources.
		- Pull up the weather for you by your location. 
	Soon, I would like to add more functionality, such as mini-games, RSS reading, and more. ''' 
import os as sh 	# shell 
from datetime import datetime	# for displaying time
from sources import * 	# import our global vars
from library.news import getNews_links2	# import the getNews_links2 function from news library
from library.weather import getWeather	# import the weather library
''' This is the main menu. 
	The user will be able to select:
	- opening up the weather
	- opening up the news
	- and more
---Variables---'''
title = f'cowsay "{asstName} GNU/Linux Assistant"' 
u1 = f'Hi, {userName}!'
u2 = "What would you like to do today?"
u3 = "Here are your options:"
options = ["1 - Read News", "2 - Get Local Weather", "3 - Exit"]
u_c = "Please type in the number corresponding to the choice you'd like to make."
c_c = "Make your selection below:\n"
#---Functions---
def sleepy():	# sleeps sys 1 sec
	sleepy1 = "sleep 1"
	sh.system(sleepy1)
def cX():		# cleans up, exits 
	cx1 = "Cleaning up and exiting."
	print(cx1)  
	sh.system('clear && cd')
	sh.system('notify-send "Helper" "Exiting the program."')
	exit()
def cowTitle():	# uses cowsay to display a title 
	sh.system(title)
def currTime():	# displays the current time
	now = datetime.now()
	timeNow = now.strftime("%H:%M:%S")
	current = f'The current time is {timeNow}.'
	print(current)
# program begins here
cowTitle()
sleepy()
currTime() 
sleepy()
print(u1)
sleepy()
print(u2)
sleepy()
print(u3)
sleepy()
for option in options:
	print(option)
# we're going to make the options array correspond to values (ints) that can be selected
options[0], options[1], options[2] = 1, 2, 3
# and now, we cast them to strings for interpretation in the conditional
options[0], options[1], options[2] = str(options[0]), str(options[1]), str(options[2])
sleepy()
print(u_c)
selection = input(c_c)
# conditional based on option selected
if (selection == options[0]):
	opt = "Fetching the news now..."
	print(opt)
	sleepy()
	getNews_links2() # from our imported lib, shows news in a minimal browser
elif (selection == options[1]):
	opt1 = "Fetching your local weather..."
	print(opt1)
	sleepy()
	getWeather() # from our imported lib
elif (selection == options[2]):
	opt2 = "You got it! Cleaning up and exiting." 
	print(opt2)
	cX() 
else:
	err = "Invalid option selected. Exiting." 
	print(err) 
	exit()

