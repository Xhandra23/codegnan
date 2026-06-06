import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

#initialize voice engine
engine=pyttsx3.init()
def speak (hii):
    engine.say(hii)
    engine.runAndWait()
speak( "hii chandra i am your virtual assistant")

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recongnizing..")
        command = recognizer.recognize_google(audio)
        print("you said:",command)
        return command.lower()
    
    except Exception:
        print("sorry,please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour<12:
        speak("happy morning")

    elif hour<18:
        speak("good morning")

    else:
        speak("good evening")

    speak(" i am your virtual assistant")
wish_user()

while True:
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        speak(F"THE TIME IS {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtude.com")

    elif "who is " in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)

    elif "exit" in command :

        speak("goodbye")
        break

