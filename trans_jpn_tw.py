#import translate
from deep_translator import GoogleTranslator, DeeplTranslator
queue = []

open(".env", "a", encoding="utf-8").close()
KeyRead = open(".env", "r", encoding="utf-8").read().split('\n')
Key = KeyRead[0]

TestPassed = True

if "#" not in Key:
    print(f"DeepL API Key: ", Key)
    try:
        translator = DeeplTranslator(api_key=Key, source="ja", target="zh", use_free_api=True)
        translator.translate("Test")
    except:
        TestPassed = False
        print('DeepL模式：API Key不正確或者不可使用，請檢查\n若您是DeepL付費用戶，請將use_free_api更改為False\n若不使用DeepL，請將.env內容修改為井字號(#)')
else:
    translator = GoogleTranslator(source='ja', target='zh-TW')

lasttrans = "none"

if TestPassed:
    while True:
        queue = open("srcipt.txt", "r", encoding="utf-8").read().split('\n')
        if len(queue) > 1:
            trans = queue[-2]
            if lasttrans != trans:
                trans = translator.translate(queue[-2])
                print(trans)
                lasttrans = queue[-2]
else:
    print('\n發生錯誤，待機中...\n請重新啟動程式')
    while(True):
        pass

     
