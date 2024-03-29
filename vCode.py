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
def search_web(input):

    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

        return


# function used to open application
# present inside the system.
def open_application(input):

    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:

        assistant_speaks("Application not available")
        return
def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Person. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Sheetansh Kumar."
            assistant_speaks(speak)
            return

        elif "geeksforgeeks" in input:# just
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            assistant_speaks(speak)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except :

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
#still going on
