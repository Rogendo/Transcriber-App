import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

# importing the .kv file
Builder.load_file('my.kv')

class MyLayout(Widget):
	pass


class TranscriberApp(App):
	def build(self):
		Window.clearcolor=("lightblue")
		return MyLayout()



if __name__ == '__main__':
	TranscriberApp().run()
