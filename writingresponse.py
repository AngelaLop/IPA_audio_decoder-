import os
import ffmpeg
import numpy as np
from pydub import AudioSegment
import pandas as pd
from dtmf import main


path = '/Users/jony/WAV_Files'
os.chdir(path)
audio_files = sorted(os.listdir(path), key=lambda x: int(x.split(".")[0])) 
audio_responses = []

for file in audio_files: 
    audio_responses.append(main(file, '-t 10', '-i 1')) 

with open('audios.txt', 'w') as f:
    for item in audio_responses:
        f.write("%s\n" % item)
f.close()
