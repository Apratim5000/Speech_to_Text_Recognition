'''Speech-to-text recognition'''

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Something Please!!')
    audio = r.listen(source)

try:
    print('Hmm. Seems like you said :\n',r.recognize_google(audio))

except:
    print("Umm. Oops! Can't recognize what you said.")
