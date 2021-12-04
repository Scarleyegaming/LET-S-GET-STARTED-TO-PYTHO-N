# CAMMAND TO INSTALL LIBRERIES
# pip install pyttsx3
# pip install speech_recognition
# pip install webbrowser
# pip install pyaudio
# IF YOU HAVE ANY PROBLEM TO INSTALL PYAUDIO PLEASE SEND A EMAIL TO THE GMAIL BELOW
# mail -  scarleyegaming@gmail.com
# CAMMANDS ARE IN COLUMN NUMBER 42 TO 52
import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init("sapi5", False)
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def speak(audio):
    print("   ")
    engine.say(audio)
    print("J.A.R.V.I.S "f": {audio}")
    print("   ")
    engine.runAndWait()

def tackcommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("reconizing.....")
            qury = command.recognize_google(audio, language="en-in")
            print(f"You Said : {qury}")
        except Exception as Error:
            return "none"
        
        return qury.lower()

def taskexe():
# 1 - jarvis this cammand give introduction of J.A.R.V.I.S
# 2 - how are you this cammand is give you a good answer
# 3 - youtube search this cammand searches in youtube just like you learning python in youtube and searche in youtube how to make J.A.R.V.I.S it also work like that 
# 4 - web this cammand open all website like amazon and also youtube
# 5 - google this cammand open google products like classroom but it can't open youtube
# 6 - bye this cammand stop running J.A.R.V.I.S program
# 7 - search this cammand searches on google just like you serche how to make jarvis in python it also work like that
# 8 - addition this cammand plus your numbers like 5 + 5 = 10 it work like addition calculator
# 9 - subtract this cammand subtract your number like 5 - 5 = 0  it also work like calculator
# 10 - multiply this cammmand multiply your number like 5 x 5 = 25 it also work like calculator
# 11 - divide this cammand divide your number like 5 ➗ 5 = 1 but it only give answer not remender
    while True:
        qury = tackcommand()

        if "jarvis" in qury:
            speak("hello sir , i am jarvis")
            speak("yes sir")
        elif "how are you" in qury:
            speak("i am ok sir")
            speak("i hope your also ok")

        elif "youtube search" in qury:
            qury =  qury.replace("jarvis", "")
            qury = qury.replace("youtube search", "")
            speak("sir whats the topic")
            name3 = tackcommand()
            web  = "https://www.youtube.com/results?search_query=" + name3
            webbrowser.open(web)
            speak("done sir")
        elif "web" in qury:
            speak("sir website name")
            name = tackcommand()
            qury = qury.replace("jarvis", "")
            qury = qury.replace("open", "")
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            speak("done sir")
        elif "google" in qury:
            speak("ok sir")
            name1 = tackcommand()
            web1 = "https://" + name1 + ".google.com"
            webbrowser.open(web1)
            speak("done sir")
        elif "bye" in qury:
            speak("ok sir bye sir")
            break
        elif "search" in qury:
            speak("sir what thing you want to search")
            name2 = tackcommand()
            web2 = "https://www.google.com/search?q=" + name2
            webbrowser.open(web2)
            speak("done sir")
        elif "addition" in qury:
           
            speak("sir please tell the first number")
            name4 = int(tackcommand())
            speak("sir please tell the second number")
            name5 = int(tackcommand())
            cal1 = speak(name4 + name5)
            speak("sir the calculation completed")

        elif "subtract" in qury:
           
            speak("sir please tell the first number")
            name6 = int(tackcommand())
            speak("sir please tell the second number")
            name7 = int(tackcommand())
            cal2 = speak(name6 - name7)
            speak("sir the calculation completed")

        elif "multiply" in qury:
           
            speak("sir please tell the first number")
            name8 = int(tackcommand())
            speak("sir please tell the second number")
            name9 = int(tackcommand())
            cal3 = speak(name8 * name9)
            speak("sir the calculation completed")
        
        elif "divide" in qury:
           
            speak("sir please tell the first number")
            name10 = int(tackcommand())
            speak("sir please tell the second number")
            name11 = int(tackcommand())
            cal4 = speak(name10 / name11)
            speak("sir the calculation completed")

taskexe()
