# Import all the necessary modules
import os
import sys
import random
import pyjokes
import pyttsx3
import datetime
import pywhatkit
import randfacts
import webbrowser
from requests import get
from quoters import Quote
import speech_recognition as sr

os.system("cls")

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
engine.setProperty('volume', 1000)

def speak(text, rate = 180): # Function to speak any text using the voice and rate provided
	engine.setProperty('rate', rate)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	
	engine.say(text)
	engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source: # Adjust to any background activity
	r.energy_threshold = 4000
	r.adjust_for_ambient_noise(source, duration=1.2)

def listen(): # Function to listen to any input in the microphone
	return_thing = ""

	with sr.Microphone() as source:
		print("listening...")
		r.energy_threshold = 4000
		r.adjust_for_ambient_noise(source, duration=1.2)
		r.pause_threshold = 1

		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		if query == "":
			return_thing = "this is random return text"
		return_thing = query.lower()
	except:
		return_thing = "this is random return text"

	return return_thing

# Function to welcome the user
def welcome():
	timeGreeting = ""
	hour = datetime.datetime.now().hour

	if hour < 12:
		timeGreeting = "Morning" # If user is in the morning then JARVIS will say "Good Morning"
	elif hour < 18:
		timeGreeting = "Afternoon" # If user is in the afternoon then JARVIS will say "Good Afternoon"
	else:
		timeGreeting = "Evening" # If user is in the evening then JARVIS will say "Good Evening"

	speak("Good " + timeGreeting + " sir, I am online")

# Function to open browser and go to a specific page
def browser(link):
	webbrowser.get("C:/Program Files (x86)/Slimjet/slimjet.exe %s").open(link)

def proceed(return_text):
	if "introduce" in return_text and "you" in return_text:
		speak("I am Jarvis, your personal assistant. I was created by Tony Stark, and re-created by Neil Dembla.")

	elif "search google" in return_text: # If user says "search google" then JARVIS will open browser and search google
		speak("Searching google for " + return_text.split("google")[1] + "...")
		browser("https://www.google.com/search?q=" + return_text.split("google")[1])

	elif "search youtube" in return_text: # If user says "search youtube" then JARVIS will open browser and search youtube
		speak("Searching Youtube for " + return_text.split("youtube")[1] + "...")
		browser("https://youtube.com/results?search_query=" + return_text.split("youtube")[1])

	elif "play song" in return_text or "play video" in return_text:
		song_request = return_text.split("song")[1]
		speak("Playing " + song_request + " on YouTube...")

		pywhatkit.playonyt(song_request)
	
	elif "tell" in return_text and "time" in return_text or "what" in return_text and "time" in return_text:
		Time = datetime.datetime.now().strftime("%I:%M %p on %B %d")
		speak("The time is " + Time)

	elif "open tab" in return_text:
		speak("Opening new tab...")

		browser("chrome://newtab")
		print("Opened new tab...")

	elif "repeat me" in return_text:
		speak(return_text.split("repeat me")[1])
		print('Repeating "' + return_text.split("repeat me")[1] + '"...')

	elif "shut" in return_text and "down" in return_text:
		print("Shutting down...")
		speak("Shutting down...")
		os.system('cls')
		sys.exit()
	
	elif "joke" in return_text:
		joke_to_tell = pyjokes.get_joke()
		
		print(joke_to_tell)
		speak(joke_to_tell)

	elif "quote" in return_text:
		return_quote = Quote.print()

		print(return_quote)
		speak(return_quote)
	
	elif "fact" in return_text:
		fact = randfacts.get_fact()
		print(f"Did you know that {fact}?")
		speak(f"Did you know that {fact}?")
	
	elif "open" in return_text and "messenger" in return_text:
		speak("Opening messenger...")
		os.startfile("C:/Users/techy/AppData/Local/Programs/Messenger/messenger.exe")

	elif "open" in return_text and "spotify" in return_text:
		speak("Opening Spotify...")
		os.startfile("C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.187.612.0_x86__zpdnekdrzrea0\\Spotify.exe")

	elif "open" in return_text and "browser" in return_text:
		speak("Opening browser...")
		os.startfile("C:/Program Files (x86)/Slimjet/slimjet.exe")
	
	elif "open" in return_text and "code" in return_text:
		speak("Opening code...")
		os.startfile("C:/Users/techy/AppData/Local/Programs/Microsoft VS Code/Code.exe")
	
	elif "open" in return_text and "whatsapp" in return_text:
		speak("Opening whatsapp...")
		os.startfile("C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2218.8.0_x64__cv1g1gvanyjgm/app/WhatsApp.exe")
	
	elif "open" in return_text and "command prompt" or "open" in return_text and "cmd" in return_text:
		speak("Opening command prompt...")
		os.startfile("C:/Windows/system32/cmd.exe")
	
	elif "ip" in return_text and "address" in return_text:
		ip = get("https://api.ipify.org").text
		print(f"IP is {ip}")
		speak(f"Your IP address is {ip}")
	
	elif "news" in return_text and "latest" in return_text or "current" in return_text and "news":
		from Features import GetNews
		GetNews()

	elif "speed" in return_text and "test" in return_text or "check" in return_text and "speed" in return_text:
		os.startfile("C:\\Users\\Owner\\Desktop\\Applications\\Coding\\Automation\\JARVIS\\GUI elements\\SpeedTestGui.py")

	elif "calculator" in return_text:
		from Features import Calculator
		Calculator(return_text)

	elif "temperature" in return_text or "temp" in return_text:
		from Features import Temperature
		Temperature(return_text.replace("tell me the ", ""))

	elif "notify" in return_text:
		from Features import Notification
		Notification("This is the title", "this is the content")

	else:
		speak("Could you repeat that sir?")
		new_input = listen()
		proceed(new_input)

welcome() # Welcomes user on startup

while True: # Infinite loop that listens for any input in microphone and then passes it to the proceed function
	data = listen() # Listens for any input in the microphone

	if "thank you" in data: # If user says "thank you" then JARVIS will say "You're welcome"
		list_of_responses = ["You're welcome sir!", "No problem sir!", "Anytime, sir!"]
		speak(random.choice(list_of_responses), "jarvis")
	elif ("jarvis" in data): # If user says "jarvis" then JARVIS will proceed
		speak("Yes sir?")
		input = listen()
		proceed(input)
	else: # If user doesn't say "jarvis" then JARVIS will listen again
		pass