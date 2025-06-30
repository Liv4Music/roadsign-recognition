import subprocess
import pyttsx3

def say_mac(text):
    subprocess.run(['say', text])

def test_sound():
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 150)
    engine.say("Testing speech with pyttsx3")
    engine.runAndWait()
    
def voicePlay(string):

    engine = pyttsx3.init()
    engine.say(f"{string}") 
    try:
        engine.runAndWait()
    except Exception as e:
        pass
    engine.runAndWait()

print("Trying macOS 'say' command:")
say_mac("Hello, this is a test")

print("Trying pyttsx3:")
test_sound()

print("Trying voicePlay:")
voicePlay("Hello, this is a test")
