# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:03:53 2019

@author: DELL
"""

from gtts import gTTS

mytext = "Hello, Good Morning. Today is the nice day."

language = 'en-IN'
myobj = gTTS(text= mytext, lang = language, slow = False)

myobj.save('sample.mp3')
