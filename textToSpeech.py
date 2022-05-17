import pyttsx3

#engine= pyttsx3.init()
#voices=engine.getProperty('voices')
#for voice in voices:
#    print(voice, voice.id)
#    engine.setProperty('voice', voice.id)
#    engine.say("Hello World!")
#    engine.runAndWait()
#    engine.stop()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#engine.setProperty('rate', 150)
#engine.say("Whatever you want")
#engine.runAndWait()

while True:
    answer = input("Enter word: ")
    engine.say(answer)

    engine.runAndWait()