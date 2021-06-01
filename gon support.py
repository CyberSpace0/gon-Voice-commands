import speech_recognition as sr
import pyaudio
from pocketsphinx import pocketsphinx
import os
from playsound import playsound

x =  open(R'C:\Users\Dutym\Desktop\gon\filter\gon.txt','r')
xx = x.read()

r = sr.Recognizer()

while True or False:
    with sr.Microphone()as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        text = r.recognize_sphinx(audio)
        print(text)
    if text == 'gon' or text in xx:
        playsound(R'E:\music\as.mp3')
        os.chdir(R'C:\Users\Dutym\Desktop\gon')
        print(os.getcwd())
        os.system('python gon.py')
