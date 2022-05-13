import os
import ffmpeg
import numpy as np
from pydub import AudioSegment
import pandas as pd
from dtmf import main


#test
ffmpeg_path = "/usr/local/bin"   
os.environ["PATH"] += os.pathsep + ffmpeg_path
# prueba 


folder = os.path.join('C:/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/WAV_Files/')
if not os.path.exists(folder):
    os.makedirs(folder)

path = '/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/Audios/'
os.chdir(path)

audio_files = os.listdir() 


for file in audio_files:
    name, ext = os.path.splitext(file) 
    if ext == ".mp3":
        mp3_sound = AudioSegment.from_mp3(file)
        mp3_sound.export("{0}.wav".format(name), format="wav")

for file in audio_files:
    name, ext = os.path.splitext(file) 
    if ext == '.wav': 
        os.rename(path + file, folder + file)

audio_responses = []
path = '/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/WAV_Files'
os.chdir(path)
audio_files = os.listdir()
for file in audio_files: 
    audio_responses.append(main(file, '-t 6', '-i 0.1')) 
print(audio_responses)

dtafile = '/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/Data/empowerment_experiment_demo.dta'
df = pd.read_stata(dtafile)
df["empowerment_1a"] = np.nan 
df["empowerment_2a"] = np.nan 


IDs = [item[0] for item in audio_responses] 
q1_response = [item[1] for item in audio_responses] 
q2_response = [item[2] for item in audio_responses] 
q1_dict={x:y for x,y in zip(IDs,q1_response)} 
q2_dict={x:y for x,y in zip(IDs,q2_response)} 
df['empowerment_1a'] = df['caseid'].map(q1_dict) 
df['empowerment_2a'] = df['caseid'].map(q2_dict) 

df.to_stata('/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/Data/empowerment_experiment_demo_with_audio responses.dta')
