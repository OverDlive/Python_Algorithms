from gtts import gTTS
from playsound import playsound

# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# Korean
# text = '아이고 윾승아'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name) # mp3 파일 재생

# 긴 문장
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) # mp3 파일 재생