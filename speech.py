import pyttsx

engine = pyttsx.init() # "espeak4" defines what engine program is running on
engine.say("Hello There , My name is santosh dahal")

engine.runAndWait()

engine.say("Hello There , My name is santosh dahal")
engine.runAndWait()