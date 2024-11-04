# .............AI Voice Assistant V1.0.............

# Additional Libraries used --> 
#                - pyttsx3
#                - Speech Recognition
#                - datetime

# Contact { 
            #instagram : _.abh.i_.x
            #gmail : abhinavsanthosh3699@gmail.com

# ! The Code Is In Initional Stage .....
                # Future updates Soon >> :)

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio  = r.listen(source,0,4)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio,language='en-in')
        print(f"You Said : {queri}")

    except Exception as e:
        return "None"
    
    return queri

current_time  = datetime.datetime.now()
hour = current_time.hour
min = current_time.minute
finaltime = (hour, min)

def greet_me():
    if hour>=0 and hour<12 :
        speak(f"Good morning sir, its {finaltime}A,M, how can i assist you")

    elif hour>=12 and hour<16:
        speak(f"Good afternoon sir, its {finaltime}P,M, how can i assist you")

    elif hour>=16 and hour<18:
        speak(f"Good evening sir, its {finaltime}P,M, how can i assist you")

    else :
        speak(f"Welcome back sir, its {finaltime}P,M, how can i assist you")

    return 

query = command().lower()

if __name__ == "__main__":
    
    greet_me()

    # ! Only Limited conversation, you can add more ! 

    while True:
        query = command().lower()
        if "how are you" in query:
            speak("i am fine sir, how are you")

        elif "i am fine" in query:
            speak("great, glad to hear that")

        elif "google" in query:
            pass
        
        
        
        elif "exit" in query:
            speak("i hope it helped ")
            break
                
        elif "go to sleep" in query:
            speak("i hope it helped")
            break



