# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:30:22 2019

@author: DELL
"""

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something...")
    audio = r.listen(source)
    print("TIME OVER!")
    
try:
    print("TEXT : "+r.recognize_google(audio,language = 'en-IN'));
except:
    pass;