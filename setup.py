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

if platform.system().lower() in ['darwin', 'linux']:

  os.system('pip3 install pafy')
  os.system('pip3 install wave')
  os.system('pip3 install ffmpy')
  os.system('pip3 install pandas')
  os.system('pip3 install soundfile')

elif platform.system().lower() == 'windows': 

  os.system('pip install -m pafy')
  os.system('pip install -m wave')
  os.system('pip install -m ffmpy')
  os.system('pip install -m pandas')
  os.system('pip install -m soundfile')
