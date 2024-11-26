
from gtts import gTTS

import pygame

mytext = 'hi, this is testing text to speech for crypto stuff. i am ramu, an average indian crypto enthusiast who thinks only about making money, biiitch'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

pygame.mixer.init()

pygame.mixer.music.load("welcome.mp3")

pygame.mixer.music.play()