import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Mời bạn nói: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio,language="vi-VI")
    print("Bạn -->: {}".format(text))
except:
    print("Xin lỗi! tôi không nhận được voice!")
    text = "Tôi không nhận được âm thanh"


engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
engine.say(text)
engine.runAndWait()
