from datetime import datetime
import json
import os
import sys
import webbrowser as browser

from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import requests
import speech_recognition as sr


def create_audio(audio, message):
    tts = gTTS(message, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

 
create_audio(audio = os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "welcome.mp3", message="Olá, sou Aurora, sua assistente virtual")
 
def monitoring_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga algo")
            audio = recon.listen(source)
            print(audio)
            try:
                message = recon.recognize_google(audio, language="pt-br")
                message = str(message).lower()
                print(f"Você disse: {message}")
                # create_audio(audio, message=message)
                execute_commands(message)
                break
            except sr.UnknownValueError as e:
                print(e)
                pass
            except sr.RequestError as e:
                print(e)
                pass
        return message


def execute_commands(message):
    if 'fechar assistente' in message:
        sys.exit()
    elif 'horas' in message:
        hour = datetime.now().strftime("%H:%M")
        phrase = f"Agora são {hour}"
        create_audio(audio=os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "message.mp3", message=phrase)
    elif 'desligar computador' and 'uma hora' in message:
        os.system("shutdown -s -t 3600")
    elif "desligar computador" and 'meia hora' in message:
        os.system("shutdown -s -t 1800")
    elif "cancelar desligamento" in message:
        os.system("shutdown -a")
    elif "toca" and "corinthians" in message:
        playlists("corinthians")
    elif "toca" and "take on me" in message:
        playlists("take on me")
    elif "notícias" in message:
        last_news()
    elif "cotação" and 'dólar' in message:
        cotacao_moeda("dólar")
    elif "cotação" and 'euro' in message:
        cotacao_moeda("euro")
    elif "cotação" and 'bitcoin' in message:
        cotacao_moeda("bitcoin")
        

def last_news():
    site = requests.get("https://news.google.com/news/rss?ned=pt_br&g1=BR&hl=pt")
    news = BeautifulSoup(site.text, 'html.parser')
    
    # print(news.tagStack)
    for item in news.find_all("item")[:7]:
        message = item.title.text
        print(message)
        create_audio(audio=os.getcwd() + os.sep + "section_4" + os.sep + "audio" + os.sep + "message.mp3", message=message)


def cotacao_moeda(moeda):
    if moeda == "dólar":
        r = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
        cotacao = r.json()
        nome = cotacao['USD']['name']
        data = cotacao['USD']['create_date']
        valor = cotacao['USD']['bid']
        message = f'Cotação do {nome} em {data} é {valor} reais'
        create_audio(message)
        
    elif moeda == "euro":
        r = requests.get("https://economia.awesomeapi.com.br/all/EUR-BRL")
        cotacao = r.json()
        nome = cotacao['EUR']['name']
        data = cotacao['EUR']['create_date']
        valor = cotacao['EUR']['bid']
        message = f'Cotação do {nome} em {data} é {valor} reais'
        create_audio(message)
        
    elif moeda == "bitcoin":
        r = requests.get("https://economia.awesomeapi.com.br/all/BTC-BRL")
        cotacao = r.json()
        nome = cotacao['BTC']['name']
        data = cotacao['BTC']['create_date']
        valor = cotacao['BTC']['bid']
        message = f'Cotação do {nome} em {data} é {valor} reais'
        create_audio(message)
        

def playlists(song):
    if song == "corinthians":
        browser.open("https://open.spotify.com/track/4uDa7Ga41Vehc7mHDotQMt?si=4567982bfdf347ef")
    elif song == "take on me":
        browser.open("https://open.spotify.com/track/2WfaOiMkCvy7F5fcp2zZ8L?si=a78c6fd2bb3f464c")


def main():
    while True:
        monitoring_audio()
        

main()
# last_news()
    