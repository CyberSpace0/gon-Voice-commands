import speech_recognition as sr
import pyaudio
from pocketsphinx import pocketsphinx
import os

#----------
twitch = open(R'filter\twitch.txt','r')
twitch__ = twitch.read()
#-----------------
shutdown = open(R'filter\shutdown.txt','r')
shutdown__ = shutdown.read()
#------------------
cod17 = open(R'filter\cold war.txt','r')
cod17__ = cod17.read()
#------------------
youtube = open(R'filter\youtube.txt','r')
youtube__ = youtube.read()
#------------------
Discord = open(R'filter\Discord.txt')
Discord__ = Discord.read()
#------------------
r = sr.Recognizer()
with sr.Microphone()as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    text = r.recognize_sphinx(audio)
    print(text)
if text == 'twitch' or text in twitch__:
    print('twitch is good')
    os.system(R'"E:\progrem file\TWITCH\Twitch\Bin\Twitch.exe"')
elif text == 'shutdown' or text in shutdown__:
    print('shutdown is good')
    os.system('shutdown /s')
elif text == 'cold war' or text in cod17__:
    print("cod 17 is good")
    os.system(R'"E:\progrel file\Battle.net\Call of Duty Black Ops Cold War\Black Ops Cold War Launcher.exe"')
elif text == 'youtube' or text in youtube__:
    print('youtube is good')
    os.system(R'"C:\Users\Dutym\Desktop\YouTube.lnk"')
elif text == 'Discord' or text in Discord__:
    print('Discord is good')
    os.system(R'"C:\Users\Dutym\Desktop\Discord.lnk"')