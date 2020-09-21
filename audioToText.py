import speech_recognition as sr       
import numpy as np
from pydub import AudioSegment
import wavio
#import ffmpeg


def genTextFromAudio(audio_file):
    r = sr.Recognizer()
    a = sr.AudioFile(audio_file)
    with a as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    print("Text here:", text)   
    
    
import numpy as np
import wavio

rate = 22050  # samples per second
T = 3         # sample duration (seconds)
f = 440.0     # sound frequency (Hz)
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
wavio.write("audio_test8.wav", x, rate, sampwidth=3)

def mp4_to_wav(file):
    audio = AudioSegment.from_file(file, format="mp4")
    audio.export("audio_test3.wav", format="wav")
    return audio


mp4_to_wav("audio_test7.mp4")

genTextFromAudio("audio_test10.wav")