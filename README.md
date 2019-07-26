# train-diseases

This repository is for training models related to disease prediction. This summarizes our lab's work in this area and makes it accessible to the public. If you'd like to contribute to this repo, please let us know! 

Take a second to watch this video below on why we started our company and why we think this research is impactful. 

[![NeuroLex intro video](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/website.png)](https://www.youtube.com/embed/QRdjBK6Ask0 "NeuroLex intro video")

## how to collaborate 

### the TRIBE Model

We created the TRIBE model to work with outstanding individuals to help accomplish our mission to build a universal voice test to refer patients to specialists faster. Fellows come from many different backgrounds - undergraduates, graduate students, faculty members, physicians, engineers, computer scientists, and other professionals. 

Fellows contribute to this repo by pursuing a data science project to model existing datasets or a research-related project to collect more data around an existing or new use case. Research demos are important for us since many of our datasets have a very small number of samples, we're very focused on curating a larger dataset and have it open-sourced to advance this work into the world.

If you're interested, definitely apply to the next TRIBE [here](http://innovate.neurolex.co). You can read [this FAQ](https://drive.google.com/open?id=1BhGxQyvcO1YZKl-Yic0MDx8IZzqNjw6m) and watch a previous demo day below to get a better feel for the program. If you have any additional questions, please reach out to Jim Schwoebel @ js@neurolex.co. 

[![TRIBE 2 Demo Day](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/TRIBE2_demo_day.png)](https://drive.google.com/file/d/1hO184La1-66DzkAt2L0u6TDbTXXthrNG/view)

## how to engineer new datasets

### why youtube?

We have found that Youtube is a reliable place to get labeled speech data if you know what to search for. For example, if we were using Parkinson’s disease as an example to find data, you could search something like [“Parkinson’s disease: my story”](https://www.youtube.com/results?search_query=parkinson%27s+disease+my+story). You’ll quickly find many people who have shared their stories of living with Parkinson’s disease. You can then manually annotate these videos to cut them around voice segments of patients and use this data to train machine learning models without any formal [IRB](https://en.wikipedia.org/wiki/Institutional_review_board).

### getting started 

This repository makes it seamless to build custom voice-based disease datasets using Youtube. 

To get started, clone this repository:

    git clone git@github.com:NeuroLexDiagnostics/train-diseases.git
    cd train-diseases 
    open template.xlsx
    
Now fill out the spreadsheet (template.xlsx) in the current directory. [This template](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/template.xlsx) (template.xlsx in this directory) allows you to quickly label 20 second segments with labels of voice data along with age (e.g. twenties), gender (e.g. male), accent (e.g. British), audio quality (e.g. good/bad), and location (indoor vs. outdoor). Note that you can make a new spreadsheet or expand upon an existing spreadsheet in this repository (in the spreadsheets directory):

* addiction.xlsx
* adhd.xlsx
* als.xlsx
* anxiety.xlsx
* autism.xlsx
* cold.xlsx
* controls.xlsx
* depression.xlsx
* depression_labels.xlsx
* dyslexia.xlsx
* glioblastoma.xlsx
* gravesdisease.xlsx
* multiple_sclerosis.xlsx
* parkinsons.xlsx
* postpartum_depression.xlsx
* schizophrenia.xlsx
* sleep_apnea.xlsx
* stressed.xlsx

Once you fill out this spreadsheet and save it to the cloned directory's spreadsheets folder, type this into the terminal:

    python3 setup.py
    python3 yscrape.py

After this, the video should start downloading and they will be converted to audio files in a folder named after the excel sheet you type in (e.g. glioblastoma.xlsx will be put into the folder glioblastoma). 

If you get stuck, you can watch a quick tutorial on how this process works in the video below.

[![](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/tutorial.png)](https://drive.google.com/file/d/1KuXq73sRw99cFq4zen3ISiTXGFjIwt87/view)

### IRB-related studies

We also have options to collect to datasets through drafting an IRB-approved study. If you are interested in doing this, please contact Reza Hosseini Ghomi (MD/MSE), our Chief Medical Officer, @ reza@neurolex.co to see if your project idea is feasible.

## references

### TRIBE program
* [TRIBE program FAQ](https://drive.google.com/open?id=1BhGxQyvcO1YZKl-Yic0MDx8IZzqNjw6m)
* [TRIBE program application link](http://innovate.neurolex.co)
* [TRIBE 2 demo day video](https://drive.google.com/open?id=1hO184La1-66DzkAt2L0u6TDbTXXthrNG)
* [TRIBE 1 demo day video](https://drive.google.com/open?id=0B2lWd9np0dsnbktLQThmMHlEdDQ)

### Ongoing studies
* [Voiceome Study](https://voiceome.org)

### Research papers (ongoing)
* [list of relevant research papers](https://drive.google.com/open?id=0B2lWd9np0dsnM0ZobjE1WWZmQ0E)
* [voice computing book](https://neurolex.ai/voicebook)

