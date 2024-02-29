import os
import speech_recognition as sr
import greeting as gr
import smtplib
import pyttsx3 as tts
import pywhatkit as kit
from datetime import *
from AppOpener import *
import wikipedia as wp
import calendar


listener = sr.Recognizer()

machine = tts.init()
voices = machine.getProperty('voices')


def talk(text):
    machine.setProperty('voice', voices[1].id)
    machine.say(text)
    machine.runAndWait()

def wake_word():
    try:
        with sr.Microphone() as origin:
            print("To Start Say Hey Aryan")
            speech  = listener.listen(origin)
            word = listener.recognize_google(speech)
            word = word.lower()

    except sr.UnknownValueError:
        word = ""
        print("Sorry,Wake Work not Found\n")

    except sr.RequestError as e:
        word = ""
        print("Error; {0}".format(e))
    return word        

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

    except sr.UnknownValueError:
        instruction = ""
        talk("Sorry, I didn't understand that.\n")

    except sr.RequestError as e:
        instruction = ""
        print("Error; {0}".format(e))

    if instruction != "":
        return instruction        
