# train-diseases

This repository is for training models related to disease prediction. This summarizes our lab's work in this area and makes it accessible to the public. If you'd like to contribute, please let us know! 

Take a second to watch this video below on why we started our company and why we think this research is impactful. 

![](https://youtu.be/QRdjBK6Ask0)

## how you can contribute

You can contribute to our lab by either pursuing a data science project to model existing data or doing a research-related project to collect more data for us to analyze. Since many of our datasets have a very small number of samples, we're very focused on curating a larger dataset and have it open-sourced to advance this work into the world. 

If this is something you're interested in, definitely apply to our Innovation Fellows program [here](http://innovate.neurolex.co)!

## list of available datasets 

Here is a list of all datasets you can currently model in this repo (table below). Some datasets are IRB-restricted and cannot be posted publicly. For these datasets, please contact Reza Hosseini Ghomi (MD/MSE), our Chief Medical Officer, @ reza@neurolex.co for access.

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

## how to engineer data 

Video here describing process.

## references

### Python libraries 
* [pafy](https://pythonhosted.org/Pafy/)
* [pytube](https://github.com/nficano/pytube)
* [youtube-dl](https://github.com/rg3/youtube-dl)

### Research papers (ongoing)
* [list of relevant research papers]()

