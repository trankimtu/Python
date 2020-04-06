#!/usr/bin/python3

import pandas as pd                                                             # Handles csv files
import numpy as np                                                              # array

import matplotlib.pyplot as plt                                                 # Graph generating library

import random                                                                   # importing random and regEx
import re

from sklearn.model_selection import train_test_split                            # sci-kit learning model to train and test split 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer    # sci-kit learning feature with two vectorizer: TfidfVectorizer and CountVectorizer
from sklearn.linear_model import LogisticRegression                             # importing linear model and naive bayes multinomial
from sklearn.naive_bayes import MultinomialNB

# helper library to use metric functions
from sklearn.metrics import confusion_matrix, classification_report             # helper library to use metric functions

import seaborn as sns

import argparse
from threading import *


"""
csvImports Description:
    opens the csv file and store it using pandas.
"""
def csvImport():
    # Loading the data utilizing pandas

    print("#####Loading CSV Data...#####")
    url_df = pd.read_csv("sample.csv")

    print("\nSample of our data of {}".format(len(url_df)))
    print(url_df.head())

    return url_df

"""
train_test Description:
    @param: url_df: takes the sample.csv and store it in an pandas array
    split the url into training and testing in respective to 80% and 20%
"""
def train_test(url_df):
    # Train = 80% and test = 20%
    test_percentage = .2

    # data must be split between training and testing the sample
    train_df, test_df = train_test_split(url_df, test_size = test_percentage, random_state = 42)

    labels = train_df['Class']
    test_labels = test_df['Class']
    
    print("\n#####Spliting Train and Testing...##### \n")

    # number set to show before bar graph
    print("\nCounting splited data frames...\n")
    print("Training Data Sample: {}".format(len(train_df)))
    print("Testing Data Sample:  {}".format(len(test_df)))

    return train_df, test_df, labels, test_labels

"""
train_test_graph Description:
    @param: train_df: takes the train_df from train_test method and generate a graph using mathplotlib.py
    @param: test_df: takes the test_df from train_test method and generate a graph using mathplotlib.py
"""
def train_test_graph(train_df, test_df):
    # This is where we generate a bar graph...

    
    print("\n#####Generating testing and training graph#####\n")
    # getting count of actual train set and test set
    barGraphTrain = pd.value_counts(train_df['Class'])
    barGraphTest = pd.value_counts(test_df['Class'])

    N = 2
    ind = np.arange(N)
    width = 0.35

    plt.bar(ind, barGraphTrain, width, label='Train')
    plt.bar(ind + width, barGraphTest, width, label = 'Test')

    plt.ylabel('Data sets')
    plt.xlabel('Training/Testing')
    plt.title('Good and Bad URL datasets')
    plt.xticks(ind + width /2, ('Train', 'Test'))
    plt.legend(loc='best')
    #plt.ion()
    #plt.show(block=True)
    plt.show()
"""
tokenizerURL Description:
    @param url: takes one of the url from csvImport method from test_url and tokenize the url
"""
def tokenizerURL(url):
    """
    This method will split the url into tokenized forms:
    www.example.com/this
        ex: example,this
    (tokenizer will remove www, . , -, /)
    """
    #Utilizing regEX to get [-,/] from the url
    tokens = re.split('[/-]', url)

    # for loop to iterate the whole url section
    for tok in tokens:
        if tok.find(".") >= 0:
            # splits the subdomains
            dotSplit = tok.split('.')
            # Remove top level domain .com, .edu, .gov
            # and www. since they're too common
            if "com" in dotSplit:
                dotSplit.remove("com")
            if "edu" in dotSplit:
                dotSplit.remove("edu")
            if "gov" in dotSplit:
                dotSplit.remove("gov")
            if "www" in dotSplit:
                dotSplit.remove("www")
            if "org" in dotSplit:
                dotSplit.remove("org")
            
            tokens += dotSplit

        return tokens

    print ("Tokenizer in transit...\n")




def vectorizer(train_df,test_df):
     
    countVec = CountVectorizer(tokenizer= tokenizerURL)
    tfidfVec= TfidfVectorizer(tokenizer=tokenizerURL)

    print("\nVectorizng data frames.... may take about a minute...\n")

    # print("\nTraining Count Vectorizer...\n")
    # countVecTrain_x = countVec.fit_transform(train_df['URLs'])

    # print("\nTraining TF-IDF Vectorizer...\n")
    # tfidfVecTrain_x = tfidfVec.fit_transform(train_df['URLs'])

    # print("\nTesting Count Vectorizer...\n")
    # countVecTest_x = countVec.transform(test_df['URLs'])

    # print("\nTesting TFIDF Vectorizer...\n")
    # tfidfVecTest_x = tfidfVec.transform(test_df['URLs'])

    # ======================== 2 Thread ========================
    class T1 (Thread):
        def __init__ (self, countVec, train_df, test_df):
            Thread.__init__(self)
            self.countVecTrain_x = None
            self.countVecTest_x = None

            self.countVec = countVec
            self.train_df = train_df
            self.test_df = test_df

        def run(self):

            print("\nThread 1 - Training Count Vectorizer...\n")
            countVecTrain_x = self.countVec.fit_transform(self.train_df['URLs'])
            self.countVecTrain_x = countVecTrain_x

            print("\nThread 1 - Testing Count Vectorizer...\n")
            countVecTest_x = self.countVec.transform(self.test_df['URLs'])
            self.countVecTest_x = countVecTest_x


        def join(self, *args):
            Thread.join(self, *args)
            return self.countVecTrain_x, self.countVecTest_x

    class T2 (Thread):
        def __init__ (self, tfidfVec, train_df, test_df):
            Thread.__init__(self)
            self.tfidfVecTrain_x = None
            self.tfidfVecTest_x = None

            self.tfidfVec = tfidfVec
            self.train_df = train_df
            self.test_df = test_df

        def run(self):
            print("\nThread 2 - Training TF-IDF Vectorizer...\n")
            tfidfVecTrain_x = self.tfidfVec.fit_transform(self.train_df['URLs'])
            self.tfidfVecTrain_x = tfidfVecTrain_x

            print("\nThread 2 - Testing TFIDF Vectorizer...\n")
            tfidfVecTest_x = self.tfidfVec.transform(self.test_df['URLs'])
            self.tfidfVecTest_x = tfidfVecTest_x

        def join(self, *args):
            Thread.join(self, *args)
            return self.tfidfVecTrain_x, self.tfidfVecTest_x


    countVec = T1(countVec, train_df, test_df)
    countVec.start()

    tfidfVec = T2(tfidfVec, train_df, test_df)
    tfidfVec.start()
    
    countVecTrain_x, countVecTest_x = countVec.join()
    tfidfVecTrain_x, tfidfVecTest_x = tfidfVec.join()

    # ======================== 4 Thread ========================
    # class T1 (Thread):
    #     def __init__ (self, countVec, train_df):
    #         Thread.__init__(self)
    #         self.countVecTrain_x = None
    #         self.countVec = countVec
    #         self.train_df = train_df
    #         print(f'countVec = {countVec}')
    #         print(f'train_df = {train_df}')

    #     def run(self):
    #         print("\nThread 1 - Training Count Vectorizer...\n")
    #         countVecTrain_x = self.countVec.fit_transform(self.train_df['URLs'])
    #         self.countVecTrain_x = countVecTrain_x

    #     def join(self, *args):
    #         Thread.join(self, *args)
    #         return self.countVecTrain_x

    # class T2 (Thread):
    #     def __init__ (self, tfidfVec, train_df):
    #         Thread.__init__(self)
    #         self.tfidfVecTrain_x = None
    #         self.tfidfVec = tfidfVec
    #         self.train_df = train_df
    #         print(f'tfidfVec = {tfidfVec}')
    #         print(f'train_df = {train_df}')

    #     def run(self):
    #         print("\nThread 2 - Training TF-IDF Vectorizer...\n")
    #         tfidfVecTrain_x = self.tfidfVec.fit_transform(self.train_df['URLs'])
    #         self.tfidfVecTrain_x = tfidfVecTrain_x

    #     def join(self, *args):
    #         Thread.join(self, *args)
    #         return self.tfidfVecTrain_x


    # class T3 (Thread):
    #     def __init__ (self, countVec, test_df):
    #         Thread.__init__(self)
    #         self.countVecTest_x = None
    #         self.countVec = countVec
    #         self.test_df = test_df
    #         print(f'countVec = {countVec}')
    #         print(f'test_df = {test_df}')

    #     def run(self):
    #         print("\nThread 3 - Testing Count Vectorizer...\n")
    #         countVecTest_x = self.countVec.transform(self.test_df['URLs'])
    #         self.countVecTest_x = countVecTest_x

    #     def join(self, *args):
    #         Thread.join(self, *args)
    #         return self.countVecTest_x

    # class T4 (Thread):
    #     def __init__ (self, tfidfVec, test_df):
    #         Thread.__init__(self)
    #         self.tfidfVecTest_x = None
    #         self.tfidfVec = tfidfVec
    #         self.test_df = test_df
    #         print(f'tfidfVec = {tfidfVec}')
    #         print(f'test_df = {test_df}')

    #     def run(self):
    #         print("\nThread 4 - Testing TFIDF Vectorizer...\n")
    #         tfidfVecTest_x = self.tfidfVec.transform(self.test_df['URLs'])
    #         self.tfidfVecTest_x = tfidfVecTest_x

    #     def join(self, *args):
    #         Thread.join(self, *args)
    #         return self.tfidfVecTest_x


    # countVecTrain = T1(countVec, train_df)
    # countVecTrain.start()

    # tfidfVecTrain = T2(tfidfVec, train_df)
    # tfidfVecTrain.start()
    

    # countVecTest = T3(countVec, test_df)
    # countVecTest.start()

    # tfidfVecTest = T4(tfidfVec, test_df)
    # tfidfVecTest.start()
    
    # countVecTrain_x = countVecTrain.join()
    # tfidfVecTrain_x = tfidfVecTrain.join()

    # countVecTest_x = countVecTest.join()
    # tfidfVecTest_x = tfidfVecTest.join()
    
    # ======================== End 4 Thread ========================
    

    print("\nVectorizing complete...\n")

    return countVecTrain_x, tfidfVecTrain_x, countVecTest_x, tfidfVecTest_x

def algorithmReport(confuMatrix, score, classReport):

    confuMatrix = confuMatrix.T

    plt.figure(figsize=(5,5))
    sns.heatmap(confuMatrix, annot=True, fmt="d", lineWidths=.5,square = True, cmap ='Blues', annot_kws={"size": 16}, xticklabels=['bad','good'], yticklabels=['bad', 'good'])
    
    plt.xticks(rotation = 'horizontal', fontsize=16)
    plt.yticks(rotation = 'horizontal', fontsize=16)
    plt.xlabel('Actual label', size = 20)
    plt.ylabel('Predicted Label', size = 20)

    title = 'Accuracy Score:  {0:.4}'.format(score)
    plt.title(title, size = 20)

    print(classReport)
    plt.ion()
    plt.show(block=True)

    print("\nReport Generator Defined...\n")

def LogicRegTFIDF(labels, test_labels,  tfidfVecTrain_x,  tfidfVecTest_x):
    # Training the Logistic Regression Algorithm

    LR_Tfidf = LogisticRegression(solver ='lbfgs')
    LR_Tfidf.fit(tfidfVecTrain_x, labels)

    score_LR_Count = LR_Tfidf.score(tfidfVecTest_x, test_labels)
    predictionsLRTfidf = LR_Tfidf.predict(tfidfVecTest_x)
    cmatrixLRTfidf = confusion_matrix(predictionsLRTfidf, test_labels)
    classReport_LRTfidf = classification_report(predictionsLRTfidf, test_labels)

    print("\nModel generating...\n")
    print("Logistic Regression w/ TfidfVectorizer")
    algorithmReport(cmatrixLRTfidf, score_LR_Count, classReport_LRTfidf)
    
# Logistic Regression with Vector Count
def LogRegression_CountVector (labels, test_labels, countVecTrain_x, countVecTest_x):
    #train model
    LR_CountVector = LogisticRegression(solver='lbfgs')
    LR_CountVector.fit(countVecTrain_x, labels)

    #test the mode (score, predictions, confusion matrix, classiificattion report)
    score_LR_CountVector = LR_CountVector.score (countVecTest_x, test_labels)
    predictionsCountVector = LR_CountVector.predict(countVecTest_x)
    cmatrixCountVector = confusion_matrix(test_labels, predictionsCountVector)
    creportCountVector = classification_report(test_labels,predictionsCountVector)

    print("\nModel generating...\n")
    print("Logistic Regression w/ Count Vector")
    algorithmReport(cmatrixCountVector, score_LR_CountVector, creportCountVector)


def mnbtf(labels, test_labels, tfidfVecTrain_X, tfidfVecTest_x):
       # Multinomial Naive Bayesian with TF-IDF
 
   # Train the model
    mnb_tfidf = MultinomialNB()
    mnb_tfidf.fit(tfidfVecTrain_X, labels)
    
    
    # Test the mode (score, predictions, confusion matrix, classification report)
    score_mnb_tfidf = mnb_tfidf.score(tfidfVecTest_x, test_labels)
    predictions_mnb_tfidf = mnb_tfidf.predict(tfidfVecTest_x)
    cmatrix_mnb_tfidf = confusion_matrix(test_labels, predictions_mnb_tfidf)
    creport_mnb_tfidf = classification_report(test_labels, predictions_mnb_tfidf)
    
    print("\n### Model Built ###\n")
    print("\nModel generating...\n")
    print("Multinomial Naive Bayesian w/ TFIDF")
    algorithmReport(cmatrix_mnb_tfidf, score_mnb_tfidf, creport_mnb_tfidf)
    
def mbbcv(labels, test_labels, countVecTrain_x, countVecTest_x):
    # Multinomial Naive Bayesian with Count Vectorizer

    # Train the model
    mnb_count = MultinomialNB()
    mnb_count.fit(countVecTrain_x, labels)


    # Test the mode (score, predictions, confusion matrix, classification report)
    score_mnb_count = mnb_count.score(countVecTest_x, test_labels)
    predictions_mnb_count = mnb_count.predict(countVecTest_x)
    cmatrix_mnb_count = confusion_matrix(test_labels, predictions_mnb_count)
    creport_mnb_count = classification_report(test_labels, predictions_mnb_count)

    print("\n### Model Built ###\n")
    print("\nModel generating...\n")
    print("Multinomial Naive Bayesian w/ Count Vectorizer")
    algorithmReport(cmatrix_mnb_count, score_mnb_count, creport_mnb_count)

"""
main Description
    Calls the respective methods and return call by function method
"""
def main(lt, lc, mt, mc):

    test_url = input("\n\nPlease input test URL or press Enter use default test URL:")
    if test_url == '':
        test_url = 'ussoccer.com/News/Federation-Services/2009/06/University-Of-Miami-President-Donna-E-Shalala-Joins-Team-To-Bring-FIFA-World-Cup-To-United-States-In.aspx'

    url_df = csvImport()
    train_df, test_df, labels, test_labels = train_test(url_df)
    train_test_graph(train_df,test_df)
    
    print("Full URL from the sample...\n")
    print(test_url)

    print("\nURL after tokenizer...\n")
    tokenized_url = tokenizerURL(test_url)
    print(tokenized_url)

    
    countVecTrain_x, tfidfVecTrain_x, countVecTest_x, tfidfVecTest_x = vectorizer(train_df, test_df)

# ===============================

    class T1 (Thread):
        def __init__ (self, labels, test_labels, tfidfVecTrain_x, tfidfVecTest_x):
            Thread.__init__(self)
            self.labels = labels
            self.test_labels = test_labels
            self.tfidfVecTrain_x = tfidfVecTrain_x
            self.tfidfVecTest_x = tfidfVecTest_x

        def run(self):
            print("\nThread 1 - LogicRegTFIDF...\n")
            LogicRegTFIDF (self.labels, self.test_labels, self.tfidfVecTrain_x, self.tfidfVecTest_x)

       
    class T2 (Thread):
        def __init__ (self, labels, test_labels, countVecTrain_x, countVecTest_x):
            Thread.__init__(self)
            self.labels = labels
            self.test_labels = test_labels
            self.countVecTrain_x = countVecTrain_x
            self.countVecTest_x = countVecTest_x

        def run(self):
            print("\nThread 2 - LogRegression_CountVector...\n")
            LogRegression_CountVector(labels, test_labels, countVecTrain_x, countVecTest_x)


    class T3 (Thread):
        def __init__ (self, labels, test_labels, tfidfVecTrain_x, tfidfVecTest_x):
            Thread.__init__(self)
            self.labels = labels
            self.test_labels = test_labels
            self.tfidfVecTrain_x = tfidfVecTrain_x
            self.tfidfVecTest_x = tfidfVecTest_x

        def run(self):
            print("\nThread 3 - mnbtf...\n")
            mnbtf(labels, test_labels, tfidfVecTrain_x,  tfidfVecTest_x)

           
    class T4 (Thread):
        def __init__ (self, labels, test_labels, countVecTrain_x, countVecTest_x):
            Thread.__init__(self)
            self.labels = labels
            self.test_labels = test_labels
            self.countVecTrain_x = countVecTrain_x
            self.countVecTest_x = countVecTest_x

        def run(self):
            print("\nThread 4 - mbbcv...\n")
            mbbcv(labels, test_labels, countVecTrain_x,  countVecTest_x)



    if lt == 'lt':
        LogicRegTFIDF_ = T1 (labels, test_labels, tfidfVecTrain_x,  tfidfVecTest_x)
        LogicRegTFIDF_.start()
        # LogicRegTFIDF_.join()
    if lc == 'lc':
        LogRegression_CountVector_ = T2 (labels, test_labels, countVecTrain_x, countVecTest_x)
        LogRegression_CountVector_.start()
        # LogRegression_CountVector_.join()

    if mt == 'mt':
        mnbtf_ = T3 (labels, test_labels, tfidfVecTrain_x,  tfidfVecTest_x)
        mnbtf_.start()
        # mnbtf_.join()
        
    if mc == 'mc':
        mbbcv_ = T4 (labels, test_labels, countVecTrain_x,  countVecTest_x)
        mbbcv_.start()
        # mbbcv_.join()

    if lt == 'lt':
        LogicRegTFIDF_.join()

    if lc == 'lc':
        LogRegression_CountVector_.join()

    if mt == 'mt':
        mnbtf_.join()
        
    if mc == 'mc':
        mbbcv_.join()

# ===============================





    # if lt == 'lt':
    #     LogicRegTFIDF(labels, test_labels, tfidfVecTrain_x,  tfidfVecTest_x)
    # if lc == 'lc':
    #     LogRegression_CountVector(labels, test_labels, countVecTrain_x, countVecTest_x)
    # if mt == 'mt':
    #     mnbtf(labels, test_labels, tfidfVecTrain_x,  tfidfVecTest_x)
    # if mc == 'mc':
    #     mbbcv(labels, test_labels, countVecTrain_x,  countVecTest_x)


"""
Calling main
"""
parser = argparse.ArgumentParser(description='MLMaliciousURL Program')
parser.add_argument('-lt','--lt', metavar='', help='LogicRegTFIDF')
parser.add_argument('-lc','--lc', metavar='', help='LogRegression_CountVector')
parser.add_argument('-mt','--mt', metavar='', help='mnbtf')
parser.add_argument('-mc','--mc', metavar='', help='mbbcv')

# group = parser.add_mutually_exclusive_group()
# group.add_argument ('-q', '--quiet', action='store_true', help='print quiet')
# group.add_argument ('-v', '--verbose', action='store_true', help='print verbose')

args =  parser.parse_args()

if __name__ == '__main__':
    # if args.quiet:
        # print('quiet')
        # main(args.lt, args.lc, args.mt, args.mc)
    # elif args.verbose:
        # print('verbose')
        # main(args.lt, args.lc, args.mt, args.mc)
    # else:
        main(args.lt, args.lc, args.mt, args.mc)
        # print(
        # """
        #     run in commandline: python .\maliciousURL.py
        #     Add '-q' for run 1 test and '-v' for multiple test
        #     Add '-lt lt' for LogicRegTFIDF test
        #     Add '-lc lc' for LogRegression_CountVector test
        #     Add '-mt mt' for mnbtf test
        #     Add '-mc mc' for mbbcv test

        # """
        # )



