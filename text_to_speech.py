
# from gtts import gTTS
# import pygame
# mytext = 'hi, this is testing text to speech for crypto stuff. i am ramu, an average indian crypto enthusiast who thinks only about making money, biiitch'
# language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save("welcome.mp3")
# pygame.mixer.init()
# pygame.mixer.music.load("welcome.mp3")
# pygame.mixer.music.play()


import pyttsx3
from pygame import mixer

def speak_and_save(text, filename):
  engine = pyttsx3.init()

  # Set the voice to a male voice
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)  # Adjust the index as needed

  # Set other properties (optional)
  engine.setProperty('rate', 150)  # Adjust the speech rate
  engine.setProperty('volume', 1.0)  # Adjust the volume

  engine.say(text)
  engine.save_to_file(filename = filename, text = text)
  engine.runAndWait()

# Example usage:
text = 'hi, this is testing text to speech for crypto stuff. i am ramu, an average indian crypto enthusiast who thinks only about making money, biiitch'
filename = "welcome.mp3"
speak_and_save(text, filename)