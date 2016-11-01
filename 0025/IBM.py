# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 14:28:25 2016

@author: MagicWang
"""
import speech_recognition as sr

#AUDIO_FILE = '20161101_1432.wav'
def speech2Text(AUDIO_FILE):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file

    # recognize speech using IBM Speech to Text
    IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        text =r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN', show_all=False)
        noBlocktext = text.replace(' ','')
        print("IBM Speech to Text thinks you said " + noBlocktext)
        return noBlocktext
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))
