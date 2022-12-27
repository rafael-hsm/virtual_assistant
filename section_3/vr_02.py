from time import sleep

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# Reading what you say
def create_save_audio(file, message):
    tts = gTTS(message, lang="pt-br")
    tts.save(file)
    playsound(file)
    

def speak_message(message):
    tts = gTTS(message, lang="pt-br")
    tts.save("welcome.mp3")
    playsound("welcome.mp3")
    



if __name__ == '__main__':
    speak_message(message="Olá, meu nome é Aurora. Sou sua assistente virtual.")
    # Voice Recognizer = vr
    vr = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo")
        audio = vr.listen(source)
        
    phrase = vr.recognize_google(audio, language="pt-br")
    create_save_audio(file="audio.mp3", message=phrase)
    