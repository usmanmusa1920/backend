# pip install gTTS
from gtts import gTTS

def create_audio_book(text_file, output_file):
    with open(text_file, "r", encoding="utf-8") as file:
        text = file.read()

    tts = gTTS(text=text, lang="en")

    tts.save(output_file)
    print(f"Audio book saved as {output_file}")

create_audio_book("text_file.txt", "output_file.mp3")
