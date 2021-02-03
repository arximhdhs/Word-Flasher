import requests
import os
import sys
from pydub import AudioSegment
from pydub.playback import play


dir_name = '/home/rodia/Documents/operation/english/audio'

f = open("/home/rodia/Documents/operation/words", "r")

f_tester=f.readline()
synolo1=[]
synolo1.append(f_tester.split(" "))
print(synolo1[0][0])
url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q="+synolo1[0][0]+"&tl=en&total=1&idx=0&textlen=" + str(len(synolo1[0][0]))
mp3_name2 = dir_name + '/' + synolo1[0][0] + ".mp3"
r2 = requests.get(url, allow_redirects=True)
open(mp3_name2, 'wb').write(r2.content)
# song = AudioSegment.from_mp3(mp3_name)

while f_tester!='':
    # song = AudioSegment.from_mp3(mp3_name)
    ##greek
    helper=f.readline() 
    synolo=[]
    synolo.append(helper.split("\n"))
    url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q="+synolo[0][0]+"&tl=el&total=1&idx=0&textlen=" + str(len(synolo[0][0]))
    mp3_name1 = dir_name + '/' + synolo[0][0] + ".mp3"
    r1 = requests.get(url, allow_redirects=True)
    open(mp3_name1, 'wb').write(r1.content)
    ##greek

    ##merged audio
    sound = AudioSegment.from_mp3(mp3_name2) +  AudioSegment.from_mp3(mp3_name1) 
    sound.export(dir_name + '/' + synolo1[0][0] + ".mp3", format="mp3")
    ##merged audio

    ##english
    f_tester=f.readline()
    synolo1=[]
    synolo1.append(f_tester.split("="))
    url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q="+synolo1[0][0]+"&tl=en&total=1&idx=0&textlen=" + str(len(synolo1[0][0]))
    mp3_name2 = dir_name + '/' + synolo1[0][0] + ".mp3"
    r2 = requests.get(url, allow_redirects=True)
    open(mp3_name2, 'wb').write(r2.content)
    ##enlgish
