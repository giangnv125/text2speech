from gtts import gTTS


# Sử lý text to speech với 1 dòng text
def text2speech(text, output_path):
    output = gTTS(text, lang="vi", slow=False)
    output.save(output_path)
