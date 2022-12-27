import speech_recognition as sr


# Voice recognition = vr
vr = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo")
    audio = vr.listen(source)
    
print(vr.recognize_google(audio, language="pt"))
