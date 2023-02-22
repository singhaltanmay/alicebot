import speech_recognition as sr
import pyaudio
import _portaudio
import os

def init(recognize='onetime'):
    if recognize=='onetime':
        curdir=os.path.dirname(os.path.abspath(__file__))
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
        try:
            cmd_google=r.recognize_google(audio, language="en-in",show_all=False)
            return cmd_google
        except sr.RequestError as e:
            return "Error 501! Could not request results from Google Speech Recognition Services"
        except sr.UnknownValueError:
            return "Error 502! Cannot understant what you said"
    elif recognize=='continuous':
        repeat=True
        while repeat==True:
            curdir=os.path.dirname(os.path.abspath(__file__))
            r=sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            try:
                cmd_google=r.recognize_google(audio, language="en-in",show_all=False)
                return cmd_google
            except sr.RequestError as e:
                return "Error 501! Could not request results from Google Speech Recognition Services"
            except sr.UnknownValueError:
                pass
