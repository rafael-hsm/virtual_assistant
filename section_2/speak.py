import pyttsx3


engine = pyttsx3.init()

engine.setProperty("voice", "brazil")
engine.say("Rafael Henrique de Sousa Meireles, é um jovem programador Python")

engine.runAndWait()
