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

This is the directory to store all of the files including three main class: readData.py that includes the data proessig methods, BootStrap.py that contains the boot strapping algorithms and LRR.py that implemented the Linear Rating Regression model.


## How to run the model:
To run the software, users need to make sure they have installed the Python3 environment on their device. Also, the software uses nltk stopwords so users should use import nltk, nltk.download(‘stopwords’), and nltk.download(‘punkt’) to download the necessary dictionaries. 

* Background:
Python 3.7

* Required Packages:
NLTK

numpy

* Specific Step:
After the completion of installation, users can run the software using python3 ReadData.py, python3 BootStrap.py, and python3 LRR.py sequentially. Then, the running results would show up. The results will list the “ReviewId”, “Actual OverallRating”, and “Predicted OverallRating” respectively in your terminal window.

*Customize:
The software running can also be customized by users in terms of ratio of training dataset and testing dataset. In the line 46 LRR.py file, the users can change the percentage of the training set. Currently, the training dataset and testing dataset are in 3:1 ratio. In addition to the training ratio, users can also specify the maximum interaction steps and coverage threshold in line 370. Moreover, if they want to change the maximum interaction steps much lower, the changing of line 339 is also needed.

* Reading Results:
The results will list the “ReviewId”, “Actual OverallRating”, and “Predicted OverallRating” respectively. Also, there is a simple classification at the end of prediction that the review would be positive when the “Predicted OverallRating” is greater than 3.0 or negative when it is smaller than 3.0.
