import numpy as np
import os
import pandas as pd

#make specific folder for the 2nd arm recordings

audio_folder = os.path.join('/Users/jony/2nd_arm_recordings/')
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

#open dta file and create dataframe with required variables    
dtafile = '/Users/jony/clean_data_empowerment.dta'
df = pd.read_stata(dtafile)
tone_audio = df[df["empo_treatment"] == 2]
caseid_audio = tone_audio[["caseid", "empo_treatment", "file_audio_empowerment"]]

#change the path and then rename the audio recordings to its case ID
os.chdir("/Users/jony/Survey_experiment_recordings")
names_dict = dict(zip(caseid_audio['caseid'], caseid_audio['file_audio_empowerment']))

for new_name, old_name in names_dict.items():
    try:
        os.rename(old_name, new_name+".m4a")
    except OSError:
        print("Audio File is missing for this subject: " + new_name)


#move the renamed audio files to another folder that only keeps the 2nd arm audios
path = "/Users/jony/Survey_experiment_recordings/"
audio_files = os.listdir()
for file in audio_files:
    name, ext = os.path.splitext(file) 
    if name == int: 
        os.rename(path + file, audio_folder + file)
