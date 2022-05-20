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
    if ext == ".m4a":
        m4a_sound = AudioSegment.from_file(file, format='m4a')
        m4a_sound.export("{0}.wav".format(name), format="wav")

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

tone_audio = df[df["empo_treatment"] == 2]
caseid_audio = tone_audio[["caseid", "empo_treatment", "file_audio_empowerment"]
                          ]
df["empowerment_1m"] = np.nan 
df["empowerment_2m"] = np.nan
df["empowerment_3m"] = np.nan
df["empowerment_4m"] = np.nan
df["empowerment_5m"] = np.nan
df["empowerment_6m"] = np.nan

IDs = [item[0] for item in audio_responses] 
q1_response = [item[1] for item in audio_responses] 
q2_response = [item[2] for item in audio_responses]
q3_response = [item[3] for item in audio_responses]
q4_response = [item[4] for item in audio_responses]
q5_response = [item[5] for item in audio_responses]
q6_response = [item[6] for item in audio_responses]

q1_dict={x:y for x,y in zip(IDs,q1_response)} 
q2_dict={x:y for x,y in zip(IDs,q2_response)}
q3_dict={x:y for x,y in zip(IDs,q3_response)}
q4_dict={x:y for x,y in zip(IDs,q4_response)}
q5_dict={x:y for x,y in zip(IDs,q5_response)}
q6_dict={x:y for x,y in zip(IDs,q6_response)}


df['empowerment_1m'] = df['caseid'].map(q1_dict) 
df['empowerment_2m'] = df['caseid'].map(q2_dict)
df["empowerment_3m"] = df['caseid'].map(q3_dict)
df["empowerment_4m"] = df['caseid'].map(q4_dict)
df["empowerment_5m"] = df['caseid'].map(q5_dict)
df["empowerment_6m"] = df['caseid'].map(q6_dict)

df.to_stata('/Users/WB585318/OneDrive - Universidad de los Andes/WB/Git_repositories/IPA_empirical_excercise/Data/empowerment_experiment_demo_with_audio responses.dta')
