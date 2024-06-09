import kivy
import random

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyRoot(BoxLayout):
    
    def __init__(self):
        super(MyRoot, self).__init__()
        
    def generate_number(self):
        self.random_label.text = str(random.randint(0, 100))

    def generate_random(self):
        import random
        self.random_label.text = str(random.randint(0, 100))

class NeuralRandom(App):
    def build(self):
	    return MyRoot()
			
	

NeuralRandom().run()