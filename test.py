import os
import time
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import speech_recognition as sr

os.system("cls")

engine = pyttsx3.init()

# Function to have JARVIS speak
def speak(text):
	engine.say(text)
	engine.runAndWait()

# Function to tell the time
def sayTime(preludingText):
	Time = datetime.datetime.now().strftime("%I:%M %p on %B %d")
	speak((preludingText) + Time)

# Function to welcome the user
def welcome():
	hour = datetime.datetime.now().hour
	timeGreeting = ""

	if hour < 12:
		timeGreeting = "Morning"
	elif hour < 18:
		timeGreeting = "Afternoon"
	else:
		timeGreeting = "Evening"

	speak("Good " + timeGreeting + " sir, I am online and ready")

# Function to open browser and go to a specific page
def browser(link):
	webbrowser.get("C:/Program Files (x86)/Slimjet/slimjet.exe %s").open(link)

# Function to listen for commands and execute them
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en')
		query = query.lower()

		if "jarvis" not in query: # If user does not specify "JARVIS" then JARVIS will not respond
			pass

		if "tell" in query and "time" in query or "what" in query and "time" in query: # If user specifies "tell" and "time" then JARVIS will say the time
			sayTime("The time is ")

		if "search google" in query: # If user says "search google" then JARVIS will open browser and search google
			speak("Opening Google...")
			browser("https://www.google.com/search?q=" + query.split("google")[1])

		if "search youtube" in query: # If user says "search youtube" then JARVIS will open browser and search youtube
			speak("Opening Youtube...")
			browser("https://youtube.com/results?search_query=" + query.split("youtube")[1])

		if "play song" in query:
			song_request = query.split("song")[1]
			speak("Searching for " + song_request)
			pywhatkit.playonyt(song_request)
	except Exception as e:
		pass # Stops script from crashing if there is no sound

welcome() # Welcomes user on startup

while True:
	takeCommand() # Listens for commands
	time.sleep(.01) # Prevents JARVIS from crashing