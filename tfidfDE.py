#!/usr/bin/env python
# encoding: utf-8

"""
File: tfidfDE.py
Original author: Yasser Ebrahim
Release date: Oct 2012

Modified by: Julius Tens
E-Mail: mail@julius-tens.de
Web: https://github.com/juliuste
Date: 31.03.2016

Generate the TF-IDF ratings for a collection of documents.
"""

import math, sys, os


# error if python 2 is used
assert sys.version_info >= (3,0)

scriptDir = os.path.dirname(__file__)
lemmaHandle		 = open(os.path.join(scriptDir, 'lemmata.csv'), 'r')
stopwordHandle	  = open(os.path.join(scriptDir, 'stopwords.txt'), 'r')

def importLemmata(handle):
	lemmata = {}
	# import lemmata from file
	for line in handle:
		if len(line) == 0 or line[0] == '#':
			continue
		words = line.split()
		if len(words) != 2 or words[0] == words[1]:
			continue
		lemmata[words[0]] = words[1]
	return lemmata

def importStopwords(handle):
	# import stopwords from file
	stopwords = []
	for line in handle:
		if len(line.split()) == 0 or line[0] == '#':
			continue
		stopwords.append(line.split()[0])
	return stopwords


def lemmatize(text, lemmata):
	# lemmatize text
	for i in range(0,len(text)):
		if text[i] in lemmata:
			text[i] = lemmata[text[i]]
	
	# don't return any single letters
	text = [t for t in text if len(t) > 1]
	return text

def removeStopwords(text, stopwords):
	# remove stopwords
	content = [w for w in text if w not in stopwords]
	return content

def tokenize(text):
	# remove punctuation, tokenize
	return "".join(c if c.isalpha() else ' ' for c in text).split()

def isNoun(word): # pseudo check if given word is a noun (if it has a capital letter, so sometimes this method returns some garbage)
	return (len(word)>=1 and word[0].isupper())



def analyze(documentPaths, resultsPerDocument=-1, preferNouns=False, showRanking=True, verbose=False):
	
	if verbose:
		print('Initializing..')

	# load language data
	lemmata = importLemmata(lemmaHandle)
	stopwords = importStopwords(stopwordHandle)

	localWordFreqs = {}
	globalWordFreq = {}

	if verbose:
		print('Working through documents.. ')

	progress = 0;

	for f in documentPaths:
		# calculate progress
		progress += 1
		if progress%math.ceil(float(len(documentPaths))/float(20)) == 0:
			if verbose:
				print(str(100*progress/len(documentPaths))+'%')
		
		# local term frequency map
		localWordFreq = {}
		
		localWords = open(f, 'r').read()
		localWords = tokenize(localWords)
		localWords = removeStopwords(localWords, stopwords)
		localWords = lemmatize(localWords, lemmata)

		
		# increment local count
		for word in localWords:
			if word in localWordFreq:
				localWordFreq[word] += 1
			else:
				localWordFreq[word] = 1

		# increment global frequency (number of documents that contain this word)
		for (word,freq) in localWordFreq.items():
			if word in globalWordFreq:
				globalWordFreq[word] += 1
			else:
				globalWordFreq[word] = 1

		localWordFreqs[f] = localWordFreq


	if verbose:
		print('Calculating.. ')

	for f in documentPaths:

		writer = open(f + '_tfidf', 'w')
		result = []
		# iterate over terms in f, calculate their tf-idf, put in new list
		for (term,freq) in localWordFreqs[f].items():
			nounModifier = 1 + int(preferNouns)*int(isNoun(term))*0.3
			tf = bool(float(freq))*(1 + math.log(float(freq)))
			idf = math.log(float(1 + len(documentPaths)) / float(1 + globalWordFreq[term]))
			tfidf = float(tf) * float(idf) * nounModifier
			result.append([tfidf, term])

		# sort result on tfidf and write them in descending order
		result = sorted(result, reverse=True)
		for (tfidf, term) in result[:resultsPerDocument]:
			if showRanking:
				writer.write(term + '\t' + str(tfidf) + '\n')
			else:
				writer.write(term + '\n')

	if verbose:
		print('Success, with ' + str(len(documentPaths)) + ' documents.')

	