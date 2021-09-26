from kivy.app import App
from kivy.uix.label import Label

class Label1(App):
	def build(self):
		x = Label(text='Hello')


		return x
if __name__ == '__main__':
	app = Label1()
	app.run()
		