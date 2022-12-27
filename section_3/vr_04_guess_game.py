from random import randint

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def create_audio(audio, message, option_language: int):
    language = ["pt-br", "en-US"]
    tts = gTTS(message, lang=language[option_language])
    tts.save(audio)
    playsound(audio)
    

create_audio("welcome.mp3", "Choice a number between 1 and 5!", 1)

vr = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo")
    audio = vr.listen(source)
    
number = vr.recognize_google(audio, language="en-US")

number = int(number)

result = randint(1, 10)

if number == result:
    create_audio("result.mp3", "Great, you Win", 1)
else:
    create_audio("result.mp3", f"You missed, the number drawn was {result}, try again", 1)
