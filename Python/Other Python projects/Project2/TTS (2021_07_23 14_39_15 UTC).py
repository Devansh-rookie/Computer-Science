import pyttsx3

i = input("1 or 0:")
if i == '1':
    TTS1 = pyttsx3.init()
    speak = input("What would you like me to say?")
    TTS1.say(speak)
    TTS1.runAndWait()
elif i == '0':
    pass


