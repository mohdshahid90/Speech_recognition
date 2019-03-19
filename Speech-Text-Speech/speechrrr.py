# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:03:59 2019

@author: DELL
"""

import speech_recognition as sr
import speak


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something...")
    audio = r.listen(source)
    print("TIME OVER!")
    
try:
    text = r.recognize_google(audio,language = 'hi-IN')
    print("TEXT : "+text);
    lang = 'hi'
    
    speak.tts(text,lang)
except:
    pass;