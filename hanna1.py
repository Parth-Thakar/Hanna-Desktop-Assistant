import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import wolframalpha
import os
import random
import requests
import json
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():  
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else: 
            speak("good evening sir ")
speak(" hello sir i am jarvis i am now  online you can command me ")

def takeCommand():
  #It takes microphone input from the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

  try:
      print("Recognizing...")    
      query = r.recognize_google(audio)
      print("User said: {}\n",format(query))

  except Exception as e:
      # print(e)    
      print("Say that again please...")  
      return "None"
  return query

if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
            query = takeCommand().lower()
    
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open sms website' in query:
                webbrowser.open("smsvaranasi.com")
            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
            elif 'open sarkari results' in query:
                webbrowser.open("sarkariresults.com")
            elif 'open mgkvp website' in query:
                webbrowser.open("mgkvp.ac.in")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\Tanay Guru\\Desktop\\ek-villain'
                random_music = music_dir + random.choice(music_dir) + '.mp3'
                os.system(random_music)
            elif 'open lightroom' in query:
                lightpath = '"C:\\Program Files\\Adobe\\Adobe Photoshop Lightroom 5.3\\lightroom.exe"'
                os.startfile(lightpath)
            elif 'full virus scan' in query:
                scan = "C:\\Program Files\\Quick Heal\\Guardian NetSecure\\scanner.exe"
                os.startfile(scan)
            elif 'open chrome' in query:
                chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome)
            elif 'tum kon ho ' in query:
                speak("i am an AI asistant my name is hanna and i am dveloped by parth thakar")
            elif 'what\'s up' in query or 'how are you' in query:
                speak(" Just doing my thing!' 'I am fine!")
            elif 'kaisi ho hanna' in query:
                speak("main theek hoon aap batao kya haal chaal ")
            elif 'what is love'  in query:
                speak("pyaar ik dhokha hai padh le beta abhi mauka hai")

            elif 'hello' in query:
                speak("hello sir")
            elif 'bye' in query:
                speak("good bye sir")   
                sys.exit()
            elif 'who are you' in query:
                speak("i am an A.I assistant hanna developed by PARTH THAKAR ")
            elif 'open turbo' in query:
                os.startfile("C:\\TurboC++\\TC_DOS.exe")