# install an external module and use it to perfrom an operation of your interest. (for example: you can install the module "playsound" and use it to play a music file in python)
import pyttsx3
engine = pyttsx3.init()
engine.say("I love raj")
engine.runAndWait()