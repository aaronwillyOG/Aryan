# Please Check the Readme file to know the Commands that you can give to Aryan

import os
import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as kit
import datetime
from AppOpener import *
import wikipedia as wp


listener = sr.Recognizer()

machine = tts.init()
voices = machine.getProperty('voices')


def talk(text):
    machine.setProperty('voice', voices[0].id)
    machine.say(text)
    machine.runAndWait()

talk("hi i am aryan. How can i help you?")

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech  = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "aryan" in instruction:
                instruction = instruction.replace('aryan', '')
                print(instruction)
            

    except:
        talk("it seems like you have said nothing")

    return instruction  

def play_Aryan():

    instruction = input_instruction()
    print(instruction)
    if "open" in instruction:
        app = instruction.replace('open', " ")
        app = app.replace(" ","")
        talk("opening" + app)
        open(app, match_closest=True)

    elif "close" in instruction:
        app = instruction.replace('close', " ")
        app = app.replace(" ","")
        talk("closing" + app)
        close(app, match_closest=True)
    
    elif "play" in instruction:
        song = instruction.replace('play', " ")
        talk("playing" + song)
        kit.playonyt(song)

    elif ("what is" in instruction) or ("who is" in instruction) or ("provide info on" in instruction) or ("provide info about" in instruction) or ("provide information on") or ("provide information about"):
        if "what is" in instruction:
            article = instruction.replace("what is", "")
            talk("collecting info from the web about" + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)
        
        elif "who is" in instruction:
            article = instruction.replace("who is", "")
            talk("collecting info from the web regarding" + article)
            info = wp.summary(article, 1)
            print(info)
            talk(info)

        elif "provide info on" in instruction:
            article = instruction.replace('provide info on', " ")
            talk("getting that from the web " + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)

        elif "provide info about" in instruction:
            article = instruction.replace('provide info about', " ")
            talk("here is what i found " + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)

        elif "provide information on" in instruction:
            article = instruction.replace('provide information on', " ")
            talk("here is what i found about " + article +", from the web")
            info = wp.summary(article, 20)
            print(info)
            talk(info)

        else:
            article = instruction.replace('provide information about', " ")
            talk("collecting information regarding " + article + ", here is what i found")
            info = wp.summary(article, 20)
            print(info)
            talk(info)

    elif ("search" in instruction) or ("google" in instruction):
        if "search" in instruction:
            article = instruction.replace('search', " ")
            talk("searching " + article)
            kit.search(article)

        elif "google" in instruction:
            article = instruction.replace('google', " ")
            talk("searching for " + article + " on google")
            kit.search(article)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I %M%p')
        talk('Current time' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d %m %Y')
        talk("Today is" + date)

    elif 'how are you' in instruction:
        talk('I am Fine, thank you')
    
    elif 'what is your name' in instruction:
        talk('I am Aryan, what can i do for you')

    else:
        talk("Please repeat")

play_Aryan()
