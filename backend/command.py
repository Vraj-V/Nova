from backend.utils import speak   # ✅ now safe
import speech_recognition as sr
import webbrowser
import time
import eel


speak("Welcome to AI Master, How you are doing?")

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")  # This will now call JS properly
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")  # This will now call JS properly
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
    except Exception as e:
        print(e)
        print("Sorry, I didn't catch that.")
        return None
    return query.lower()

# text1= takeCommand()
# speak(text1)
@eel.expose
def takeAllCommand():
    query = takeCommand()
    print(query)
    if "open" in query:
        from backend.feature import openCommand
        openCommand(query)
    elif "youtube" in query:
        from backend.feature import PlayYoutube
        PlayYoutube(query)
    else:
        print(" nothing opening")
    eel.showHood()