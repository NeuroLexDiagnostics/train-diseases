# train-diseases

This repository is for training models related to disease prediction. This summarizes our lab's work in this area and makes it accessible to the public. If you'd like to contribute to this repo, please let us know! 

Take a second to watch this video below on why we started our company and why we think this research is impactful. 

[![NeuroLex intro video](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/website.png)](https://www.youtube.com/embed/QRdjBK6Ask0 "NeuroLex intro video")

## how to collaborate

We created the TRIBE model to work with outstanding individuals to help accomplish our mission to build a universal voice test to refer patients to specialists faster. Fellows come from many different backgrounds - undergraduates, graduate students, faculty members, physicians, engineers, computer scientists, and other professionals. 

Fellows contribute to this repo by pursuing a data science project to model existing data or doing a research-related project to collect more data for us to analyze. Since many of our datasets have a very small number of samples, we're very focused on curating a larger dataset and have it open-sourced to advance this work into the world. 

If you're interested to be a part of our lab, definitely apply to our Innovation Fellows program [here](http://innovate.neurolex.co)! 

You can read [this FAQ](https://drive.google.com/open?id=1BhGxQyvcO1YZKl-Yic0MDx8IZzqNjw6m) and watch a previous demo day (TRIBE 2) below to get a better feel for the program. If you have any additional questions, please reach out to Jim Schwoebel @ js@neurolex.co. 

[![TRIBE 2 Demo Day](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/TRIBE2_demo_day.png)](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/TRIBE2_demo_day.png)

## active collaborators 

### NeuroLex Team Members
* Jim Schwoebel (Chief Executive Officer)
* Reza Hosseini Ghomi, MD/MSE (Chief Medical Officer)
* Drew Morris (Chief Technology Officer)
* James Fairey (Chief Audio Officer)
* Marsal Gavalda PhD (Machine learning advisor)

### University of Washington Fellows
* Dave Atkins, PhD - Mental Health / various 

### IBM 
* Guillermo Cecchi, PhD - Psychosis / Schizophrenia 

### Emory University
* Ihab Hajjar, PhD - Alzheimer's disease 

### TRIBE 1 Fellows 
* Ryan Dunn (Georgia Tech) - Sleeping Disorders 
* Radhika Duvvuri (Georgia Tech) - Depression 
* Aditya Muralidhar (Georgia Tech) - Anxiety disorders 
* Peter Tang (Rice University) - Caffeine detection 
* Yahia Ali (Georgia Tech) - Hardware interfaces for voice data collection 
* Alice Romanov (Wake Forest University) - Parkinson's disease 
* Brittany Wheeler (Boston University) - Alzheimer's disease 
* Shadab Hassan (New York University) - Anxiety disorders 

### TRIBE 2 Fellows 
* Hannah Gersch (Georgia Tech) - Various 
* Larry Zhang (Intern, Nvidea) - Bipolar disorder / Feature embeddings 
* Timothy Wroge (University of Pittsburgh) - Parkinson's disease 
* Audrey Wagner (University of Pittsburgh) - Glioblastoma 
* Dylan Pitulski (University of Pittsburgh) - Schizophrenia 
* Wendy Nguyen (UC Irvine) - Depression
* Allison Pei (Cornell University) -  Common colds
* Alyssa Naritoku (University of Southern California) - Graves disease 
* Aditi Mylavarapu (The University of Michigan) - Autism spectrum disorders (ASDs)

## list of available datasets 

Here is a list of all datasets you can currently model in this repo (table below). 

We also have access to datasets are IRB-restricted and cannot be posted publicly. If you are interested to access these datasets, please contact Reza Hosseini Ghomi (MD/MSE), our Chief Medical Officer, @ reza@neurolex.co for access.

## Accuracies to beat 

### audio embedding models

We tested a few datasets here to see the performance of the audioclassify.py script. Here are the results:

| **Name**       | **Algorithm** | **Training Description** | **Accuracy**          |
| ------------- |-------------|-------------|-------------|
|depression|knn|N=12 train/test|88.7% (+/- 9.3%)|
|gender|hard voting|N=106 train/test|86.8% (+/- 6.1%)|
|glioblastoma|random forest|N=10 train/test|85.0% (+/- 20.0%)|
|bipolar|svm|N=19 train/test|81.4% (+/- 13.1%)|
|als|random forest|N=12 train/test|81.3% (+/- 16.5%)|
|cold|logistic regression|N=16 train/test|78.1% (+/- 7.6%)|
|schizophrenia|gradient boosting| N=19 train/test | 75.3% (+/- 13.5%)|
|anxiety|knn|N=9 train/test|73.3% (+/- 27.6%)|
|multiple sclerosis|gradient boosting|N=19 train/test|71.9% (+/- 9.5%)|
|parkinsons|knn| N=13 train/test | 70.0% (+/- 20.4%)|
|adhd|sk learn|N=16 train/test|69.2% (+/- 12.8%)| 
|dialect|gaussian-nb|N=21 train/test|64.8% (+/- 21.4%)|
|autism|gaussian-nb|N=14 train/test|63.3% (+/- 22.7%)|
|dyslexia|logistic regression|N=19 train/test|62.1% (+/- 17.2%)|
|addiction|sk learn|N=19 train/test|61.4% (+/- 2.1%)|

### text embedding

We tested a few datasets here to see the performance of the textclassify.py script. Here are the results:

| **Name**       | **Algorithm** | **Training Description** | **Accuracy**          |
| ------------- |-------------|-------------|-------------|
|als|svm|N=12 train/test|84.0% (+/- 14.9%)|
|bipolar|svm|N=19 train/test|81.4% (+/- 13.1%)|
|schizophrenia|svm| N=19 train/test | 81.3% (+/- 12.1%)|
|anxiety|logistic regression|N=9 train/test|78.3% (+/- 29.6)|
|parkinsons|logistic regression| N=13 train/test | 70.0% (+/- 19.4%)|
|multiple sclerosis|random forest|N=19 train/test|69.2% (+/- 5.7%)|
|dialect|random forest|N=21 train/test|65.1% (+/- 10.4%)|
|depression|hard voting|N=12 train/test|80.0% (+/- 12.6%)|
|cold|svm|N=16 train/test|78.1% (+/- 13.0%)|
|addiction|gaussian-nb|N=19 train/test|64.1% (n/a)|
|adhd|logistic regression|N=16 train/test|62.9% (+/- 4.6%)|
|dyslexia|gradient boosting|N=19 train/test|62.5% (+/- 12.6%)|
|glioblastoma|svm|N=10 train/test|59.9% (+/- 20.0%)|
|gender|hard voting|N=106 train/test|57.8% (+/- 2.7%)|
|autism|naive-bayes|N=14 train/test|57.1% (n/a)|

### mixed embeddings

We tested a few datasets here to see the performance of the mixedclassify.py script (mixed text and audio arrays). Here are the results:

| **Name**       | **Algorithm** | **Training Description** | **Accuracy**          |
| ------------- |-------------|-------------|-------------|
|glioblastoma|gradient boosting|N=10 train/test|96.0% (+/- 8.0%)|
|anxiety|logistic regression|N=9 train/test|90.0% (+/- 20.0)|
|cold|gradient boosting|N=16 train/test|87.5% (+/- 12.4%)|
|gender|svm|N=106 train/test|86.3% (+/- 2.8%)|
|als|svm|N=12 train/test|85.0% (+/- 20.0%)|
|schizophrenia|logistic regression| N=20 train/test | 84.6% (+/- 15.1%)|
|depression|svm|N=12 train/test|81.0% (+/- 18.5%)|
|parkinsons|gradient boosting| N=13 train/test | 80.0% (+/- 19.4%)|
|adhd|logistic regression|N=16 train/test|75.7% (+/- 14.8%)| 
|multiple sclerosis|random forest|N=19 train/test|74.1% (+/- 9.3%)|
|bipolar|gaussian-nb|N=19 train/test|71.8% (+/- 16.5%)|
|autism|random forest|N=14 train/test|67.1% (+/- 28.7%)|
|addiction|gaussian-nb|N=19 train/test|63.7% (+/- 13.0%)|
|dialect|decision-tree|N=21 train/test|59.3% (+/- 18.3%)|
|dyslexia|sk learn|N=19 train/test|58.9% (+/- 2.9%)|

## how to engineer datasets

This repository makes it seamless to build custom voice-based disease datasets using Youtube. 

We have found that Youtube is a reliable place to get labeled speech data if you know what to search for.

For example, if we were using Parkinson’s disease as an example to find data, you could search something like [“Parkinson’s disease: my story”](https://www.youtube.com/results?search_query=parkinson%27s+disease+my+story). You’ll quickly find many people who have shared their stories of living with Parkinson’s disease. 

We have built [a template](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/template.xlsx) (template.xlsx in this directory) for you to quickly label 20 second segments with labels of voice data along with age (e.g. twenties), gender (e.g. male), accent (e.g. British), audio quality (e.g. good/bad), and location (indoor vs. outdoor). Note that 20 seconds of audio has been the ideal amount of audio to label data from some experimentation, and additional data in the same video does not necessarily lead to more accurate results in data science modeling so you should use that as a target for labels. 

After you fill out this template, you can quickly download and cut the videos and extract the audio for further processing (using the script in this folder - yscrape.py). You can watch a quick tutorial on how this process works in the video below.

[![](https://github.com/NeuroLexDiagnostics/train-diseases/blob/master/data/tutorial.png)](https://drive.google.com/file/d/1KuXq73sRw99cFq4zen3ISiTXGFjIwt87/view)

## references

### TRIBE program
* [TRIBE program FAQ](https://drive.google.com/open?id=1BhGxQyvcO1YZKl-Yic0MDx8IZzqNjw6m)
* [TRIBE program application link](http://innovate.neurolex.co)
* [TRIBE 2 demo day video](https://drive.google.com/open?id=1hO184La1-66DzkAt2L0u6TDbTXXthrNG)
* [TRIBE 1 demo day video](https://drive.google.com/open?id=0B2lWd9np0dsnbktLQThmMHlEdDQ)

### Python libraries 
* [pafy](https://pythonhosted.org/Pafy/)
* [pytube](https://github.com/nficano/pytube)
* [youtube-dl](https://github.com/rg3/youtube-dl)
* [librosa](https://librosa.github.io/librosa/)
* [nltk](https://www.nltk.org/)
* [scikit-learn](http://scikit-learn.org/stable/index.html)
* [keras](https://keras.io/)
* [tensorflow](https://www.tensorflow.org/)

### Research papers (ongoing)
* [list of relevant research papers]()

