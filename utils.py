import os
import playsound


# Load các dòng text từ file
def load_text(text_file):
    with open(text_file, 'r', encoding='utf8') as f:
        lines = f.readlines()

    return lines


# Play các file âm thanh
def play_speech(sound_dir):
    for file in os.listdir(sound_dir):
        playsound.playsound(os.path.join(sound_dir, file))
