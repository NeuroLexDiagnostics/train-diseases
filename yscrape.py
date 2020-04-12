'''
Script: yscrape.py
Author: Jim Schwoebel

This script takes in a template excel sheet and downloads videos from youtube.

After this, the videos are clipped to the desired ranges as annoted by the end user.

This is all done in the current directory that the script is executed. 

In this way, we can quickly build custom curated datasets around specific 
use cases based on self-reported video bloggers.

Also, labels each output audio file with date, url, length, clipped points, 
label, age, gender, accent, and environment (if available in excel sheet).
'''

import os, json, time, wave, ffmpy, shutil, getpass, datetime, sys, time
from optparse import OptionParser
import pandas as pd
import soundfile as sf

# download audio with youtube-dl instead of pafy to prevent errors
def download_audio(link):
    listdir=os.listdir()
    os.system("youtube-dl -f 'bestaudio[ext=m4a]' '%s'"%(link))
    listdir2=os.listdir()
    filename=''
    for i in range(len(listdir2)):
        if listdir2[i] not in listdir and listdir2[i].endswith('.m4a'):
            filename=listdir2[i]
            break

    return filename

def load_colunns(loadfile):
    labels=list(loadfile)

# -------------------------- # 
# get all the curenti nfo in the terminal if its there
curdir=os.getcwd()

# add a very simple file parser here for CLI client
parser = OptionParser()
parser.add_option("-e", "--excel", dest="filename",
                  help="load in audiofile (.WAV format)", metavar="FILE")
parser.add_option("-f", "--folder", dest="folder",
                  help="specify the folder", metavar="FOLDER")
(options, args) = parser.parse_args()

# -------------------------- # 
# load terminal variables; if they aren't there prompt user for spreadsheets available / which to download 
try: 
    directory=options.folder
    filename=options.filename
    print(filename)
    print(directory)
    os.chdir(directory)
except:
    os.chdir('spreadsheets')
    listdir=os.listdir()
    excel_files=list()
    for i in range(len(listdir)):
        if listdir[i].endswith('.xlsx'):
            excel_files.append(listdir[i])

    excel_files.append('all')
    filename=input('what is the file name? \n\n options: %s \n\n'%(str(excel_files)))
    os.chdir(curdir)
    
# -------------------------- # 

if filename == 'all':

    # recursively call this script with proper variables if user wants all data
    for i in range(len(excel_files)):
        if excel_files[i] != 'all':
            # now iterate through all these 
            os.chdir(curdir)
            os.chdir('spreadsheets')
            filename=excel_files[i]
            desktop=os.getcwd()+'/'
            foldername=filename[0:-5]
            destfolder=desktop+foldername+'/'
            try:
                os.mkdir(foldername)
                os.chdir(destfolder)
            except:
                os.chdir(destfolder)

            #move file to destfolder 
            shutil.copy(desktop+filename,destfolder+filename)

            #load xls sheet (and get labels)
            loadfile=pd.read_excel(filename)
            link=loadfile.iloc[:,0]
            length=loadfile.iloc[:,1]
            times=loadfile.iloc[:,2]

            #initialize lists 
            links=list()
            lengths=list()
            start_times=list()
            end_times=list()
            labels=list()

            # headers - use these as the primary labels to put in the .JSON docs
            headers_=list(loadfile)
            headers=list()
            for i in range(len(headers_)):
                if i > 2:
                    headers.append(headers_[i])

            print('key labels: ')
            print(headers)
            #only make links that are in youtube processable 
            for i in range(len(link)):
                if str(link[i]).find('youtube.com/watch') != -1:
                    links.append(str(link[i]))
                    lengths.append(str(length[i]))
                    #find the dash for start/stop times
                    time_=str(times[i])
                    index=time_.find('-')
                    start_time=time_[0:index]
                    #get start time in seconds 
                    start_minutes=int(start_time[0])
                    start_seconds=int(start_time[-2:])
                    start_total=start_minutes*60+start_seconds
                    #get end time in seconds 
                    end_time=time_[index+1:]
                    end_minutes=int(end_time[0])
                    end_seconds=int(end_time[-2:])
                    end_total=end_minutes*60+end_seconds
                    #update lists 
                    start_times.append(start_total)
                    end_times.append(end_total)
                    #labels
                    labels.append(foldername)

            files=list()
            for i in range(len(links)):
                try: 
                    # use YouTube DL to download audio
                    filename=download_audio(links[i])
                    extension='.m4a'
                    start=start_times[i]
                    end=end_times[i]
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
                    newfilename='snipped'+file
                    
                    #can write json too 
                    nfile= dict()
                    nfile["Date"] = str(datetime.datetime.now())
                    nfile["URL"] = str(links[i])
                    nfile["Length"] = str(length[i])
                    nfile["Clipped points"] = str(times[i])
                    nfile["Indication"] = str(foldername) 

                    data=dict()
                    for j in range(len(headers)):
                        # find index
                        i1=headers_.index(headers[j])
                        try:
                            print(headers[j])
                            print(loadfile.iloc[:,i1][i])
                            data[headers[j]] = str(loadfile.iloc[:,i1][i])
                        except:
                            print('error loading header')
                    
                    nfile["labels"] = data

                    jsonfile=open(newfilename[0:-4]+'.json','w')
                    json.dump(nfile, jsonfile)
                    jsonfile.close()
                    os.remove(file)

                except:
                    print('error fetching video')

                # sleep 5 seconds to not overwhelm YouTube's servers
                # it's a good practice to be a good internet citizen!! :) 
                time.sleep(5)

else:

    os.chdir('spreadsheets')
    desktop=os.getcwd()+'/'
    foldername=filename[0:-5]
    destfolder=desktop+foldername+'/'
    try:
        os.mkdir(foldername)
        os.chdir(destfolder)
    except:
        os.chdir(destfolder)

    #move file to destfolder 
    shutil.copy(desktop+filename,destfolder+filename)

    #load xls sheet (and get labels)
    loadfile=pd.read_excel(filename)
    link=loadfile.iloc[:,0]
    length=loadfile.iloc[:,1]
    times=loadfile.iloc[:,2]

    #initialize lists 
    links=list()
    lengths=list()
    start_times=list()
    end_times=list()
    labels=list()

    # headers - use these as the primary labels to put in the .JSON docs
    headers_=list(loadfile)
    headers=list()
    for i in range(len(headers_)):
        if i > 2:
            headers.append(headers_[i])

    print('key labels: ')
    print(headers)
    #only make links that are in youtube processable 
    for i in range(len(link)):
        if str(link[i]).find('youtube.com/watch') != -1:
            links.append(str(link[i]))
            lengths.append(str(length[i]))
            #find the dash for start/stop times
            time_=str(times[i])
            index=time_.find('-')
            start_time=time_[0:index]
            #get start time in seconds 
            start_minutes=int(start_time[0])
            start_seconds=int(start_time[-2:])
            start_total=start_minutes*60+start_seconds
            #get end time in seconds 
            end_time=time_[index+1:]
            end_minutes=int(end_time[0])
            end_seconds=int(end_time[-2:])
            end_total=end_minutes*60+end_seconds
            #update lists 
            start_times.append(start_total)
            end_times.append(end_total)
            #labels
            labels.append(foldername)

    files=list()
    for i in range(len(links)):
        try: 
            # use YouTube DL to download audio
            filename=download_audio(links[i])
            extension='.m4a'
            start=start_times[i]
            end=end_times[i]
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
            newfilename='snipped'+file
            
            #can write json too 
            nfile= dict()
            nfile["Date"] = str(datetime.datetime.now())
            nfile["URL"] = str(links[i])
            nfile["Length"] = str(length[i])
            nfile["Clipped points"] = str(times[i])
            nfile["Indication"] = str(foldername) 

            data=dict()
            for j in range(len(headers)):
                # find index
                i1=headers_.index(headers[j])
                try:
                    print(headers[j])
                    print(loadfile.iloc[:,i1][i])
                    data[headers[j]] = str(loadfile.iloc[:,i1][i])
                except:
                    print('error loading header')
            
            nfile["labels"] = data

            jsonfile=open(newfilename[0:-4]+'.json','w')
            json.dump(nfile, jsonfile)
            jsonfile.close()
            os.remove(file)

        except:
            print('error fetching video')

        # sleep 5 seconds to not overwhelm YouTube's servers
        # it's a good practice to be a good internet citizen!! :) 
        time.sleep(5)