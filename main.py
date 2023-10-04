import time

from utils import *
from text2speech_api import *


def main(text_file, out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    # Load text từ file
    text_lines = load_text(text_file)
    # Xử lý text to speech với từ dòng text
    for i, text in enumerate(text_lines):
        path = os.path.join(out_dir, str(i) + '.mp3')
        start_time = time.time()
        text2speech(text, path)
        print('Run time text2speech:', time.time() - start_time)
    # Play sound files
    play_speech(out_dir)


if __name__ == "__main__":
    main('input_text/input_text.txt', 'speech_dir')
