'''
Script: yscrape.py
Author: Jim Schwoebel
Github repo: train-diseases 
Repo link: https://github.com/NeuroLexDiagnostics/train-diseases
License: Apache 2.0 

This script takes in a template excel sheet and downloads videos from youtube. 
After this, the videos are clipped to the desired ranges as annoted by the end user.
This is all done in the current directory that the script is executed. 

In this way, we can quickly build custom curated datasets around specific 
diseases based on self-reported video bloggers with various disease conditions.

For example, you could go onto youtube search and type in "depression: my story." 
There is then a list of videos you can parse through and use the template.xlsx provided
in the train-diseases repository to annotate these videos for things like age, gender,
ethnicity, audio quality, etc., as well as start and stop points in the video in a 20 
second segment. Then you can run this script to help extract all the audio files for modeling. 

Join us in building the largest open-source disease modeling dataset for voice!

- the NeuroLex team
'''

import os, json, pafy, time, wav, ffmpy, shutil, getpass
import pandas as pd
import soundfile as sf

filename=input('what is the file name? \n')
desktop=os.getcwd()+'/'
os.chdir(desktop)
foldername=filename[0:-5]
destfolder=desktop+foldername+'/'
try:
    os.mkdir(foldername)
    os.chdir(destfolder)
except:
    os.chdir(destfolder)

#move file to destfolder 
shutil.move(desktop+filename,destfolder+filename)

#load xls sheet
loadfile=pd.read_excel(filename)
link=loadfile.iloc[:,0]
length=loadfile.iloc[:,1]
times=loadfile.iloc[:,2]
label=loadfile.iloc[:,3]

#initialize lists 
links=list()
lengths=list()
start_times=list()
end_times=list()
labels=list()

#only make links that are in youtube processable 
for i in range(len(link)):
    if str(link[i]).find('youtube.com/watch') != -1:
        links.append(str(link[i]))
        lengths.append(str(length[i]))
        #find the dash for start/stop times
        time=str(times[i])
        index=time.find('-')
        start_time=time[0:index]
        #get start time in seconds 
        start_minutes=int(start_time[0])
        start_seconds=int(start_time[-2:])
        start_total=start_minutes*60+start_seconds
        #get end time in seconds 
        end_time=time[index+1:]
        end_minutes=int(end_time[0])
        end_seconds=int(end_time[-2:])
        end_total=end_minutes*60+end_seconds
        #update lists 
        start_times.append(start_total)
        end_times.append(end_total)
        #labels
        labels.append(str(label[i]))

files=list()
for i in range(len(links)):
    try: 
        video=pafy.new(links[i])
        bestaudio=video.getbestaudio()
        filename=bestaudio.download()
        start=start_times[i]
        end=end_times[i]
        extension=bestaudio.extension
        #get file extension and convert to .wav for processing later 
        os.rename(filename,'%s_start_%s_end_%s%s'%(str(i),start,end,extension))
        filename='%s_start_%s_end_%s%s'%(str(i),start,end,extension)
        if extension not in ['.wav']:
            xindex=filename.find(extension)
            filename=filename[0:xindex]
            ff=ffmpy.FFmpeg(
                inputs={filename+extension:None},
                outputs={filename+'.wav':None}
                )
            ff.run()
            os.remove(filename+extension)
        
        file=filename+'.wav'
        data,samplerate=sf.read(file)
        totalframes=len(data)
        totalseconds=totalframes/samplerate
        startsec=int(start_times[i])
        startframe=samplerate*startsec
        endsec=int(end_times[i])
        endframe=samplerate*endsec
        sf.write('snipped'+file, data[startframe:endframe], samplerate)
        os.remove(file)

        #can write json too 
        
        
    except:
        print('no urls')


