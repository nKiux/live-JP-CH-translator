#import translate
from deep_translator import GoogleTranslator
queue = []

translator = GoogleTranslator(source='ja', target='zh-TW')

lasttrans = "none"

while(True):
        queue = open("srcipt.txt", "r", encoding="utf-8").read().split('\n')
        if len(queue) > 1:
            trans = queue[-2]
            if lasttrans != trans:
                trans = translator.translate(queue[-2])
                print(trans)
                lasttrans = queue[-2]
