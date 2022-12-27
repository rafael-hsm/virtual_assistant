import os

from gtts import gTTS
from playsound import playsound


def create_save_audio(message):
    tts = gTTS (message, lang="pt-br")
    tts.save("hello.mp3")
    playsound("hello.mp3")
    
    
if __name__ == '__main__':
    # Utilização simples
    # create_save_audio("Olá mundo. Testando uma função com Python")
    
    # Utilização via entrada de dados
    # phrase = input("Digite a frase a ser falada \n")
    # create_save_audio(phrase)
    
    # Lendo arquivos
    path = os.getcwd() + os.sep + "section_2" + os.sep + "teste.txt"
    file = open(path, "r", encoding="utf-8")
    content = file.read()
    create_save_audio(content)
    file.close()
    