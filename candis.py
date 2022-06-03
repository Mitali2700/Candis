import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')  # Microsoft Speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 1-Hazel 0-Zira


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Candis ma'am. Please tell me how may I help you?")

def takeCommand():
    '''
        It take
    '''

if __name__ == "__main__":
    wishMe()