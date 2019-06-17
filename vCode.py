import os
import time
import speech_recognition as sr
import fuzzywuzzy
import pyttsx3
import datetime
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer,audio):
    try:
        voice=recognizer.recognize_google(audio,language='en-US').lower()
        print('[log] You: '+voice)
        if voice.startswith(opts['alias']):
            cmd=voice
            for x in opts['alias']:
                cmd=cmd.replace(x,'').strip()
            for x in opts['tbs']:
                cmd=cmd.replace(x,'').strip()
        cmd=recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])
    except sr.UnknownValueError:
        print('[log] Cant understand the voice!)')
    except sr.RequestError as e:
        print('[log] Unknown Error')
def recognize_cmd(cmd):
    RC={cmd:'','percent':0}
    for c,v in opts['cmd'].items():
        for x in v:
            vert=fuzz.ratio(cmd,x)
            if vrt>RC['percent']:
                RC[cmd]=c
                RC['percent']=vrt
    return RC
def execute_cmd(cmd):
    if cmd=='ctime':
        now=datetime.datetime.now()
        speak('It is:'+str(now.hour)+':'+str(now.minute))
opts={'alias':('v','vi','ve','ve','vi'),'tbs':('show','open','what'),
      'cmd':{'ctime':('time','what time is it','tell me the time'),
            'radio':('turn on the music','music')} }
r=sr.Recognizer()
m=sr.Microphone(device_index=1)
with m as source:
    r.adjust_for_ambient_noise(source)
speak_engine=pyttsx3.init()
voices=speak_engine.getProperty('voices')
speak_engine.setProperty('voice',voices[1].id)
speak('Hello Matvey, I am ready to serve you')
stop_listening=r.listen_in_background(m,callback)
while True:time.sleep(0.1)
