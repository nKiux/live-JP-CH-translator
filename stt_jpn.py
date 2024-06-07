import os

from threading import Thread
from queue import Queue

import speech_recognition as sr
import asyncio

# Initialize the recognizer
r = sr.Recognizer()
r.energy_threshold = 280
r.dynamic_energy_ratio = 2

global audio_q
audio_q = Queue()

def collect():
    #print("__偵測: [啟動中...]")
    try:
        while True:
            with sr.Microphone(device_index=2) as source:
                r.adjust_for_ambient_noise(source, duration = 0.5)
                audio_q.put(r.listen(source, phrase_time_limit = 15))
                print('saved...')
    except KeyboardInterrupt:
        print('Quit')
        exit()

    except sr.exceptions.WaitTimeoutError:
        print('skipped a timeout')

def recognizer():
    while True:
        audio = audio_q.get()
        if audio is None: 
            print('None')
            break
        try:
            #r.adjust_for_ambient_noise(audio, duration = 0.5)
            #audio = r.listen(audio, phrase_time_limit = 15, timeout=1)
            #print('understanding...')
            MyText = r.recognize_google(audio, language='ja-JP')
            print("Detector:", MyText)
            open("srcipt.txt", "a", encoding="utf-8").write(f"{MyText} \n")
        except sr.RequestError as e:
            print("**處理錯誤**; {0}".format(e))

        except sr.UnknownValueError:
            print("**無法識別**")
        print('done...')
        audio_q.task_done()

def main():
    global rec_thread
    rec_thread = Thread(target=recognizer)
    rec_thread.daemon = True
    rec_thread.start()
    #print('collecting...')
    collect()
    #print('exit collect')
    audio_q.join()
    audio_q.put(None)
    rec_thread.join()
    print('finished')

wrt = open("srcipt.txt", "w", encoding="utf-8")
wrt.write("")


main()
