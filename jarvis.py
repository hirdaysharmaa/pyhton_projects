import speech_recognition as sr
import pyttsx3
# import pyjokes
import webbrowser
import datetime
# import os
import time 
#initialize recognizer
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.5

def Listen():
    # use default microphone as the source
    with sr.Microphone() as source:
        print("Speak anything ...")
    
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen to the user's input
        audio_data = recognizer.listen(source)
    
        try:
            print("Recognizing...")
        
            # Recognize speech using Google Speech Rcognition
            text = recognizer.recognize_google(audio_data)
            print(f"Speech recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not undrstand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

# Listen()               
def sptxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate= engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()
# speechtxt('hello welcome to hirday sharma profile ')
if __name__ =='__main__':
    # if "hey jarvis" in sptxt().lower():
    # while True:
        text1=Listen().lower()
# extra Code gemini write  by gemini 
        # text1 = Listen()
        # if text1 is not None:
        #     text1 = text1.lower()
        # else:
        #     # Handle the case where text1 is None (e.g., print a message)
        #     print("Could not understand the audio. Please try again.")
#  extracode gemini
        if "your name " in text1:
            name= "my name is hirday sharma "
            sptxt(name)
        elif "old are you " in text1:
            age="i am two years old "
            sptxt(age)
        elif 'what  is  time' in text1:
            time= datetime.datetime.now().strftime("%I%M%p")
            sptxt(time)
        elif 'google' in text1:
            webbrowser.open("https://www.google.co.in/")
        elif 'apna college' in text1:
            webbrowser.open("https://www.youtube.com/@ApnaCollegeOfficial")
        elif 'github ' in text1:
            webbrowser.open("https://github.com/hirdaysharmaa")
            

        # elif 'joke' in text1:
        #     joke_1=pyjokes.get_joke(language="en",category="neutral")
        #     print(joke_1)
        #     sptxt(joke_1)
        # elif 'open image ' in text1:
        #     add="Downloads"
        #     listsong= os.listdir(add) 
        #     print(listsong)
        #     os.startfile(os.path.join(add,listsong[0]))
        # elif "exit " in text1:
        #     sptxt("thankyou")
        #     break
        
        else:
            print("thankyou")
        





























