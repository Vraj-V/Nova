# from playsound import playsound 
# import eel

# @eel.expose
# def playAssistantSound():
#     music_dir = "front-end//assets//audio//start_sound.mp3"
#     playsound(music_dir)

import re
import webbrowser
import eel
import pygame
import os
import pywhatkit as kit
from backend.config import ASSISTANT_NAME
from backend.utils import speak   # ✅ now safe
# from backend.command import takeAllCommand --- IGNORE ---
import sqlite3

conn = sqlite3.connect("nova.db")
cursor = conn.cursor()

pygame.mixer.init()
@eel.expose
def playAssistantSound():
    music_dir = "front-end//assets//audio//start_sound.mp3"
    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open","")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute( 
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
    else:
        speak("I dont understand anything.")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing" +search_term+ "on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None