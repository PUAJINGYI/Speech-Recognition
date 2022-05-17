import speech_recognition as sr
#from gtts import gTTS
#import os
import pyttsx3
import datetime

#myText = "Text to speech converter using python"
#fh=open("test.txt", "r")
#myText = fh.read().replace("\n"," ")

#language = 'en'

#output = gTTS(text=myText, lang=language, slow=False)

#output.save("output.mp3")
#fh.close()
#os.system("start output.mp3")
def speech():
    listener = sr.Recognizer()

    with sr.Microphone() as input_source:
        print("I am Listenning....")
        voice_input = listener.listen(input_source)
        text = listener.recognize_google(voice_input)
        print(text)
        if(text.__contains__("date")):
            x=datetime.datetime.now()
            print(x.day)

while True:
    speech()

