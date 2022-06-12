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
import urllib.request
import urllib.request
import urllib.parse
import smtplib
import  requests
import json


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voices',voices[-1].id)
client = wolframalpha.Client('EE34V8-YXHA996H3R') 

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

speak(" hello! how was your day sir ! ")


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
def takeCommand1():
  #It takes microphone input from the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

  try:
      print("Recognizing...")    
      re = r.recognize_google(audio)
      print("User said: {}\n",format(re))

  except Exception as e:
      # print(e)    
      print("Say that again please...")  
      return "None"
  return re

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvisjarvis689@gmail.com', 'jarvis2019')
    server.sendmail('jarvisjarvis689@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
            # if the net connection is slow we can use the text to give the command
            #query=input()
            query = takeCommand().lower()
            
            
    
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'are you up' in query:
                speak("alwyas for you sir")
            elif 'pretty fine' in query:
                speak("woderfull! sir")
            elif 'not good' in query:
                speak("oh! dont worry i can figure this out for you sir! would you like to listen your favraite song")
                #mood =takeCommand().lower()
                mood=input()
                if 'yes' in mood:
                    webbrowser.open('https://www.youtube.com/watch?v=9R4cI_MGS2I&list=RDy2tEPmwWEiI&index=3')
                elif 'no' in mood:
                    speak("ok sir! can i tell you a joke ")
                    mood =takeCommand().lower()  
                    if 'yes' in  mood:
                        speak("A: I have the perfect son. B: Does he smoke? A: No, he doesn't. B: Does he drink whiskey? A: No, he doesn't. B: Does he ever come home late?A: No, he doesn't. B: I guess you really do have the perfect son. How old is he? A: He will be six months old next Wednesday.")
                        speak("i am telling you a joke sir ! but you should be working on your new project and something new cause you can not stay with your past get up change it ")
                    elif 'no' in mood:
                        speak(" you should be working on your new project and something new cause you can not stay with your past get up change it ")
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("opening youtube for you ! anything else sir:")
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
                speak("opening facebook for you ! anything else sir:")
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("opening google for you ! anything else sir:")
            elif 'open sms website' in query:
                webbrowser.open("smsvaranasi.com")
                speak("opening your college website for you ! anything else sir:")
            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
                speak("opening instagram for you ! anything else sir:")
            elif 'open sarkari results' in query:
                webbrowser.open("sarkariresults.com")
                speak("opening your demanding site sir for you ! anything else sir:")
            elif 'open mgkvp website' in query:
                webbrowser.open("mgkvp.ac.in")
                speak("doing sir ...!")
            elif 'play music' in query:
                os.startfile('%ProgramFiles%\\Windows Media Player\\wmplayer.exe')
            elif 'open lightroom' in query:
                lightpath = '"C:\\Program Files\\Adobe\\Adobe Photoshop Lightroom 5.3\\lightroom.exe"'
                os.startfile(lightpath)
                speak("opening lightroom cc")
            elif 'full virus scan' in query:
                scan = "C:\\Program Files\\Quick Heal\\Guardian NetSecure\\scanner.exe"
                os.startfile(scan)
                speak("scaning your whole  system sir enter yes to start it will take some time ")
            elif 'open chrome' in query:
                chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome)
                speak("opening google chrome sir")
            elif 'tum kon ho ' in query:
                speak("i am an AI asistant my name is hanna and i am dveloped by parth thakar")
            elif 'what\'s up' in query or 'how are you' in query:
                speak(" Just doing my thing!' 'I am fine!")
            

            elif 'hello' in query:
                speak("hello sir")
            elif 'bye' in query:
                speak("good bye!  sir")   
                sys.exit()
            elif 'who are you' in query:
                speak("i am an A.I assistant jarvis developed by PARTH THAKAR ")
            elif 'open turbo' in query:
                os.startfile("C:\\TurboC++\\TC_DOS.exe")
                speak("opening turbo c++")
            elif 'play a trap song' in query:
                webbrowser.open("youtube.com/watch?v=Mq4r_J-JGyg")
            elif 'joke' in query:
                speak("Girl: You would be a good dancer except for two things. Boy: What are the two things? Girl: Your feet.")
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            elif 'i am giving you to my mam' in query:
                speak("hey mam i hope you are fine how can i help you")    
            elif ' net speed' in query:
                speak("ok sir i am doing ")
                webbrowser.open('https://fast.com/')
            

            elif 'repeat protocol' in query:
                speak("activating repeat protocol!")
                re=takeCommand().lower()
                #re=input()
                speak(re)
                
            elif 'activate multitasking' in query:
                speak("speak only what you want to serach! sir")
                while True:
                    new = takeCommand().lower()
                    if 'exit' in new:
                        sys.exit()
                    else:
                        res=client.query(new)
                        out=next(res.results).text
                        print(out)
                        speak(out)
                    
            elif 'activate google search' in query:
                ad='https://www.google.com/search?sxsrf=ACYBGNSUpA_2R-cpzoh-zbgtl1IgiwSlZw%3A1569990618046&source=hp&ei=2SeUXbj_O9H5rQGjobfIDw&q='
                speak("ready! say only what you want to search")
                word=takeCommand().lower()      
                newword=ad+word
                speak("showing all your ")
                speak(word)
                speak("search result on your browser sir")
                webbrowser.open(newword)
                speak("anything else sir !")
            
            elif 'activate youtube search' in query:
                li='https://www.youtube.com/results?search_query='
                speak("ready sir speak only what you want to search on youtube")
                se=takeCommand().lower()
                nli=li+se
                speak("showing all youtube search result on your browser")     
                webbrowser.open(nli)
            
            if 'send email to me' in query:
             try:
                speak("What should I say?")
                content = takeCommand()
                to = "parththakar59@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
             except Exception as e:
                print(e)
                speak("Sorry my friend parth bhai. I am not able to send this email")    
      
           

            
            
            #else:
                #speak('Searching Wikipedia...')
                #query = query.replace("wikipedia", "")
                #results = wikipedia.summary(query, sentences=2)
                #speak("According to Wikipedia")
                #print(results)
                #speak(results)
