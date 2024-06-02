import os
try:
    import speech_recognition as sr
    import translate
    import asyncio
except:
    os.system("pip install speechrecognition")
    os.system("pip install translate")

# Initialize the recognizer
r = sr.Recognizer()
r.energy_threshold = 350
r.dynamic_energy_ratio = 2

async def detecting():
    #print("__偵測: [啟動中...]")
    try:
        with sr.Microphone(device_index=2) as source2:
            #print("__偵測: [聆聽中...]")
            r.adjust_for_ambient_noise(source2, duration = 0.5)
            audio2 = r.listen(source2, phrase_time_limit = 15, timeout=1)
            print('understanding...')
            MyText = r.recognize_google(audio2, language='ja-JP')
            print("Detector:", MyText)
            await open("srcipt.txt", "a", encoding="utf-8").write(f"{MyText} \n")
            
    except sr.RequestError as e:
        #print("__偵測: [無法處理]; {0}".format(e))
        pass
    except:
        #print("Skip...", flush=True)
        pass

async def main():
    await detecting()

wrt = open("srcipt.txt", "w", encoding="utf-8")
wrt.write("")

while True:
    asyncio.run(main())
