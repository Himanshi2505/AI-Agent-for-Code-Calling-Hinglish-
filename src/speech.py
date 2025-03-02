# import speech_recognition as sr
# import pyttsx3

# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio, language="hi-En")
#         return text
#     except sr.UnknownValueError:
#         return "Sorry, I couldn't understand."

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
import speech_recognition as sr
from gtts import gTTS
import os
import pygame

class AudioHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        pygame.mixer.init()

    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing speech...")
                text = self.recognizer.recognize_google(audio, language="hi-IN")
                print(f"Recognized: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected. Please try again.")
                return None
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def text_to_speech(self, text):
        try:
            tts = gTTS(text=text, lang='hi', slow=False)
            tts.save("response.mp3")
            pygame.mixer.music.load("response.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            os.remove("response.mp3")
        except Exception as e:
            print(f"An error occurred during text-to-speech: {e}")
            print(f"Bot would say: {text}")

audio_handler = AudioHandler()
