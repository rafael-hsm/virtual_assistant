from datetime import datetime
import os
import sys

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


def create_audio(audio, message):
    tts = gTTS(message, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


create_audio(audio= os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "welcome.mp3", message="Olá, sou Aurora, sua assistente virtual")
    
def monitoring_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga algo")
            audio = recon.listen(source)
            try:
                message = recon.recognize_google(audio, language="pt-br")
                message = message.lower()
                print(f"Você disse: {message}")
                create_audio(audio= os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "teste.mp3", message=message)
                execute_commands(message)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return message


def execute_commands(message):
    audio = os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "message.mp3"
    if 'fechar assistente' in message:
        sys.exit()
    elif 'horas' in message:
        hour = datetime.now().strftime("%H:%M")
        phrase = f"Agora são {hour}"
        create_audio(audio=audio, message=phrase)
    elif 'desligar computador' and 'uma hora' in message:
        os.system("shutdown -s -t 3600")
    elif "desligar computador" and 'meia hora' in message:
        os.system("shutdown -s -t 1800")
    elif "cancelar desligamento" in message:
        os.system("shutdown -a")
        
    
    
def main():
    while True:
        monitoring_audio()
        

main()
    