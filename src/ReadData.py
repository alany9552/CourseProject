import json
import nltk
from nltk.corpus import stopwords
import os
import glob
from nltk.stem.porter import *
from nltk import FreqDist
path="hotelReviews/"
projectSettings="settings/"
from collections import defaultdict
import string
from collections import defaultdict
from nltk import FreqDist

class Sentence:
    def __init__(self, wordList):
        self.wordFreqDict = FreqDist(wordList)#Dictionary of words in the sentence and corres. frequency
        self.assignedAspect = [] #list of aspects assigned to this sentence
    def __str__(self):
        return self.wordFreqDict.pformat(10000) + '##' + str(self.assignedAspect)

class Review:
    def __init__(self):
        self.sentences = [] #list of objects of class Sentence
        self.reviewId = ""
        self.ratings = {} #true ratings provided by the user

    def __str__(self):
        retStr = ""
        for sentence in self.sentences:
            retStr += sentence.__str__() + '\n'
        retStr += "###"+self.reviewId+"###"+str(self.ratings)+"\n"
        return retStr

class ReadData:
    def __init__(self):
        self.aspectKeywords = {} #aspect name <--> keywords list
        self.stopWords = []
        self.wordFreq = {} #dict with of all words and their freq in the corpus
        self.lessFrequentWords=set() #words which have frequency<5 in the corpus
        self.allReviews = [] #list of Review objects from the whole corpus
        self.aspectSentences = defaultdict(list) #aspect to Sentences mapping

    def readWords(self):
        fd1 = open(projectSettings+"SeedWords.json")
        seed = json.load(fd1)
        fd2 = open(projectSettings+"stopwords.dat")

        for aspect in seed["aspects"]:
            self.aspectKeywords[aspect["name"]] = aspect["keywords"]
        for stopWord in fd2:
            self.stopWords.append(stopWord.strip())
        for stopWord in stopwords.words('english'):
            if stopWord not in self.stopWords:
                self.stopWords.append(stopWord)


    def stemmingStopWRemoval(self, review, vocab):
        reviewObj = Review()
        #copying ratings into reviewObj
        for ratingType, rating in review["Ratings"].items():
            reviewObj.ratings[ratingType] = rating
        reviewObj.reviewId = review["ReviewID"]

        stemmer = PorterStemmer()
        reviewContent = review["Content"]
        sentencesInReview = nltk.sent_tokenize(reviewContent)
        puncs = {']', '!', '+', '`', '*', ')', '.', '\\', '~', '>', '#', '|',
        '<', '/', '{', ',', '[', '$', '}', '-', ';', '(', '%', '_',
        '@', "'", '=', '&', '"', ':', '^', '?'}

        for sentence in sentencesInReview:
            wordList=[]
            words = nltk.word_tokenize(sentence)
            for word in words:
                # if not all(c.isdigit() or c in puncs for c in word):
                for i in word:
                    if not ((i.isdigit()) and (i in puncs)):
                        word = word.lower()
                        if word not in self.stopWords:
                            word=stemmer.stem(word)
                            vocab.append(word)
                            wordList.append(word)
            if wordList:
                sentenceObj=Sentence(wordList)
                reviewObj.sentences.append(sentenceObj)
        self.allReviews.append(reviewObj)
            #print(reviewObj)

    def readReviewsFromJson(self):
        vocab=[]
        for filename in glob.glob(os.path.join(path, '*.json')):
            fd=open(filename)
            data=json.load(fd)
            for review in data["Reviews"]:
                self.stemmingStopWRemoval(review,vocab)

        self.wordFreq = FreqDist(vocab)
        for word,freq in self.wordFreq.items():
            if freq < 5:
                self.lessFrequentWords.add(word)
        for word in self.lessFrequentWords:
            del self.wordFreq[word]


    def removeLessFreqWords(self):
        emptyReviews = set()
        for review in self.allReviews:
            emptySentences = set()
            for sentence in review.sentences:
                deleteWords = set()
                for word in sentence.wordFreqDict.keys():
                    if word in self.lessFrequentWords:
                        deleteWords.add(word)
                for word in deleteWords:
                    del sentence.wordFreqDict[word]
                if not sentence.wordFreqDict:
                    emptySentences.add(sentence)

            temp = [x for x in review.sentences if x not in emptySentences]

            for i, x in enumerate(review.sentences):
                if x not in emptySentences:
                    review.sentences[i] = x #x?
                else:
                    review.sentences.pop(i)
            if not review.sentences:
                emptyReviews.add(review)

        temp2 = [x for x in self.allReviews if x not in emptyReviews]
        for i, x in enumerate(self.allReviews):
            if x not in emptyReviews:
                self.allReviews[i] = x #x?
            else:
                self.allReviews[i].pop(i)
