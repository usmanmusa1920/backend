"""
    before you run this program make sure you install the following from pypi.org:
        playsound
        gtts
        speech_recognition
"""


import os
import time
import random
import playsound
import webbrowser

from gtts import gTTS
from time import ctime
import speech_recognition as sr



r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            man_speech(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            man_speech("voice_data")
        except sr.UnknownValueError:
            man_speech('Sorry, I did not get that')
        except sr.RequestError:
            man_speech('Sorry, my speech service is down')
        return voice_data
    
def man_speech(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def respond():
    if 'What is your name' in voice_data:
        man_speech('My name is Usman')
    if 'What is the time' in voice_data:
        man_speech('The time is', ctime())
    if 'Search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        man_speech('This is what I found for ' + search)
    if 'location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place=' + location + '/&amp;'
        webbrowser.get().open(url)
        man_speech('This is the location of ' + location)
    if 'exit' in voice_data:
        exit()
    
time.sleep(1)
man_speech('How can I help you?')
while 1:
    print('Please how can I help you?')
    voice_data = record_audio()
    respond(voice_data)
