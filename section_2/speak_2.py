import pyttsx3


engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

phrase = input("Digite a frase a ser falada\n")
engine.say(phrase)

engine.runAndWait()
