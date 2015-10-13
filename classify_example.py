'''
Created on Sep 21, 2012
Umesh R Hodeghatta
@author: user
'''
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import reuters
import nltk.tokenize
 
def word_feats(words):
    return dict([(word, True) for word in words])

pos_sent1 = "This is very good movie"
pos_sent2 = "Excellent movie"
pos_sent3 = "I liked this movie"
pos_sent4 =" good entertainment"

neg_sent1 = "very bad movie"
neg_sent2 = "this movie sucks"
neg_sent3 = "this is horrible movie"
neg_sent4 = "will not reccomend this movie"

negids = [neg_sent1,neg_sent2,neg_sent3,neg_sent4]
posids = [pos_sent1,pos_sent2,pos_sent3,pos_sent4]

    
negfeats = [(word_feats(nltk.word_tokenize(f)), 'neg') for f in negids]
print negfeats
posfeats = [(word_feats(nltk.word_tokenize(f)), 'pos') for f in posids]
print posfeats

negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print trainfeats
print "train on %d instances, test on %d instances" % (len(trainfeats), len(testfeats))
print testfeats 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy: ', nltk.classify.util.accuracy(classifier,testfeats)
classifier.show_most_informative_features()

print "running test classification"
test_features = word_feats(nltk.word_tokenize("it is a very bad movie"))
print classifier.classify(test_features)


"""
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
"""
