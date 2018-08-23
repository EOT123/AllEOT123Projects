import pyttsx
k = pyttsx.init()


def say(text):
    k.say(text)
    k.runAndWait()


say('Hello')
