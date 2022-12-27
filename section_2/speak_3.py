import os
import pyttsx3


# Start pyttsx3 and setting voice to Brazil
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

# Search and open the file
path = os.getcwd() + os.sep + "section_2" + os.sep + "teste.txt"
file = open(path, "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# Say the text in file
engine.say(content)

engine.runAndWait()
