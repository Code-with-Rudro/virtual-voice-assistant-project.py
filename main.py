import speech_recognition as sr
import pyaudio 
import pyttsx3
import webbrowser
# pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()



def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("INITIALIZE siva.....")
    while True:
        #listen for the wake up word "siva"
        r = sr.Recognizer()


        print("processing...")
        #recognize speech using spinx
        try:
            with sr.Microphone() as source:
               print("listening.....")
               #listen(_) it takes = time out perameater phrase time limit perameater.
               audio = r.listen(source, timeout=3, phrase_time_limit=1)
            command = r.recognize_google(audio)
            print(command)
        
        except Exception as e:
            print("pass your thought...".format(e))

    
