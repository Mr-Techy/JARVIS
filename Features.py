import pyttsx3
import requests
import wolframalpha
from notifypy import Notify

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)

def speak(text, rate = 180): # Function to speak any text using the voice and rate provided
	engine.setProperty('rate', rate)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	
	print(text)
	engine.say(text)
	engine.runAndWait()

def Wolfram(query):
	api_key = "633HQW-K4EKPE6P8G"
	
	requester = wolframalpha.Client(api_key)
	requested = requester.query(query)
	
	try:
		Answer = next(requested.results).text

		return Answer
	except Exception as e:
		speak("Sorry sir, an error occurred")

def GetNews():
	url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=f015571d195543ccabc3623dd7cdec9d&category=business"
	news = requests.get(url).json()
	articles = news["articles"]

	for i in range(3):
		speak(f"Article {i+1}: " + articles[i]["title"], rate=140)

def Calculator(query):
	term = query.replace("calculator", "")
	term = term.replace("plus", "+")
	term = term.replace("minus", "-")
	term = term.replace("times", "*")
	term = term.replace("into", "*")
	term = term.replace("divided by", "/")
	term = term.replace("equals", "=")

	Final = str(term)

	try:
		result = Wolfram(Final)
		speak(f"{result}")
	except Exception as e:
		speak("Sorry sir, there was an error.")

def Temperature(where):
	Term = str(where)

	Term = Term.replace("temperature ", "")
	Term = Term.replace("in ", "")
	Term = Term.replace("what is the ", "")

	temp_query = str(Term)

	if 'outside' in temp_query:
		var1 = "temperature in greer, sc"
		answer = Wolfram(var1)

		speak(f"The {var1} is {answer}")
	else:
		var2 = "temperature in " + temp_query
		answ = Wolfram(var2)

		speak(f"The {var2} is {answ}")

def Notification(title, content):
	Noti = Notify()

	Noti.title = str(title)
	Noti.message = str(content)

	Noti.send()