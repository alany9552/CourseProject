# CourseProject for CS410 at University of Illinois at Urbana-Champaign

## The python implementation is following the instructions from research papers:

"Latent Aspect Rating Analysis on Review Text Data: A Rating Regression Approach", 
http://sifaka.cs.uiuc.edu/~wang296/paper/rp166f-wang.pdf

"Latent Aspect Rating Analysis without Aspect Keyword Supervision",
http://sifaka.cs.uiuc.edu/~wang296/paper/p618.pdf

## Implementations and Contributers:

This implementation uses the orignal implementation given by the author (http://www.cs.virginia.edu/~hw5x/Codes/LARA.zip).
Also, the Latent Rating Regression model and Bootstrap use the implementation of existing models from:
https://github.com/redris96/LARA
https://github.com/seanliu96/LARA
https://github.com/biubiutang/LARA-1

## Contributors:
Chengmin Huang - ch61@illinois.edu
Xuehao Wang - xuehaow2@illinois.edu
Ge Yu - gey2@illinois.edu

## Organization of the implemenataion:

* src/hotelRivews:

This directory includes the hotel reviews download from the database http://times.cs.uiuc.edu/~wang296/Data/ from TripAdvisor. For testing, we include only one review file. You are free to download the whole dataset to do a better training, which might take up to 30 minutes to run 10 json files.
 
* src/Settings:

This is the directory to store the pre-difined laten words and stopwords downloaded from nltk libaray.

* src/modelData:

This is the directory to store the data after processed by readData.py, the file includes the ratings, reviewID, each word's frequencyy and the aspectKeywords after reading thereviews.

* src

This is the directory to store all of the files including three main class: readData.py, BootStrap.py and LRR.py




There are two classes Sentence and Review each coded in different python files. These act as data containers for a sentence and a single review respectively. 
ReadData contains all functions for processing the reviews. BootStrap class contains the bootstrapping algorithm as explained in the paper. LRR class contains the implementation of Rating Regression algorithm as described in the paper. 
We had initially coded as ipython notebooks so .ipynb files also exist.
* hotelReviews directory is where the review files go (json encoded) - both Training and Testing data
* settings directory contains the configuration files for the model
* modelData will contain the files generated by the model

How to run:
Have nltk and scipy installed. Also download modules for nltk-stopwords and porter-stemmer. 

For preprocessing reviews:
python3 BootStrap.py

For running the main model:
python3 LRR.py
