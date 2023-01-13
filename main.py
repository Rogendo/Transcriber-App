import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
import speech_recognition as sr

#Window.size=(340,640)
# importing the .kv file
Builder.load_file('my.kv')

class MyLayout(Widget):
	def transcriber_click(self):
		r=sr.Recognizer()
		mic=sr.Microphone()
		with mic as source:
			r.adjust_for_ambient_noise(source)
			message=r.listen(source)
			message=r.recognize_google(message)
			self.ids.lebal_1.text=message
			print("transcribe button is clicked")





class TranscriberApp(App):
	def build(self):
		Window.clearcolor=("lightblue")
		return MyLayout()



if __name__ == '__main__':
	TranscriberApp().run()
