from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SpeedTestUi import Ui_SpeedTest
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)

def speak(text, rate = 180): # Function to speak any text using the voice and rate provided
	engine.setProperty('rate', rate)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)\
	
	print(text)
	engine.say(text)
	engine.runAndWait()

def run_uit():
	speak("Checking speed...")

	import speedtest

	speed = speedtest.Speedtest()
	
	upload = speed.upload()
	correct_Up = int(int(upload) / 800000)

	speak("Please wait...")

	download = speed.download()
	correct_Down = int(int(download) / 800000)

	speak(f"Download speed is {correct_Down} Megabits per second")
	speak(f"Upload speed is {correct_Up} Megabits per second")

	speak("Sir, I could not close the window, you may have to close it yourself.")

class MainThread(QThread):
	def __init__(self):
		super(MainThread, self).__init__()

	def run(self):
		run_uit()
		sys.exit()

StartExe = MainThread()

class StartExecution(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = Ui_SpeedTest()
		self.ui.setupUi(self)
		self.ui.label = QMovie("C:\\Users\\techy\\OneDrive\\Desktop\\Applications\\Coding\\Automation\\JARVIS\\GUI elements\\speed test.gif")
		self.ui.gif.setMovie(self.ui.label)
		self.ui.label.start()

		StartExe.start()

App = QApplication(sys.argv)
speedtest = StartExecution()
speedtest.show()
exit(App.exec_())