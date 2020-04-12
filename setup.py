'''
Script: setup.py
Author: Jim Schwoebel
License: Apache 2.0 license
Repository: train-diseases
Repo link: https://github.com/NeuroLexDiagnostics/train-diseases

This script helps to install all required dependencies for the yscrape.py script. 

This assumes you have python3 installed on your machine.
'''

import os, platform

def pip3_install(modules):
  for i in range(len(modules)):
    os.system('pip3 install %s'%(modules[i]))
    
def brew_install(modules):
  for i in range(len(modules)):
    os.system('brew install %s'%(modules[i]))

brew_modules=['ffmpeg','youtube-dl']
pip3_modules=['pandas','ffmpy','tqdm', 'pandas', 'soundfile']

brew_install(brew_modules)
pip3_install(pip3_modules)

