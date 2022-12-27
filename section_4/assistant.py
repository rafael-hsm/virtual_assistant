import os

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


def create_audio(audio, message):
    tts = gTTS(message, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    
    
def monitoring_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga algo")
            audio = recon.listen(source)
            try:
                message = recon.recognize_google(audio, language="pt-br").lower()
                print(f"Você disse {message}")
                create_audio(audio= os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "teste.mp3", message=message)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return message
    
    
def main():
    while True:
        monitoring_audio()
        

if __name__ == '__main__':
    main()
    