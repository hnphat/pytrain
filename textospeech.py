import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
engine.say("Xin chào các bạn")
engine.runAndWait()

# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#     print(voice)