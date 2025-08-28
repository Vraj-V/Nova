import pyttsx3
import eel
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    display_message(text)  # call the new function

    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def display_message(text):
    # code to display the message in JavaScript
    pass