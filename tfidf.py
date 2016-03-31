#!/usr/bin/env python
# encoding: utf-8

"""
File: tfidf.py
Original author: Yasser Ebrahim
Release date: Oct 2012

Modified by: Julius Tens
E-Mail: mail@julius-tens.de
Web: https://github.com/juliuste
Date: 30.03.2016

Generate the TF-IDF ratings for a collection of documents.

This script will also tokenize the input files to extract words (removes punctuation and puts all in
    lower case).

Usage:
    - Create a file to hold the paths+names of all your documents (in the example shown: input.txt)
    - Make sure you have the full paths to the files listed in the file above each on a separate line
    - For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
    - Simply run this script file with your input file as a single parameter, for example:
            python tfidf.py examples/input.txt
    - This script will generate new files, one for each of the input files, with the suffix "_tfidf"
            which contains terms with corresponding tfidf score, each on a separate line
"""

import math, codecs
from optparse import OptionParser


supported_langs     = ('german')
# a list of (words-freq) pairs for each document
# list to hold occurrences of terms across documents
lang                = 'german'
top_k               = -1
lemmaHandle         = codecs.open('german/lemmata/list.csv', 'r', 'utf-8')
stopwordHandle      = codecs.open('german/stopwords/list.txt', 'r', 'utf-8')

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
        if len(line) == 0 or line[0] == '#':
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



# __main__ execution


# --- Parameter handling -----------------------------------
parser = OptionParser(usage='usage: %prog [options] input_file')
parser.add_option('-k', '--top-k', dest='top_k',
        help='output only terms with score no less k')
parser.add_option('-m', '--mode', dest='mode',
        help='display mode. can be either "both" or "term"')
(options, args) = parser.parse_args()

if options.top_k:
    top_k = int(options.top_k)
display_mode = 'both'
if options.mode:
    if options.mode == 'both' or options.mode == 'term':
        display_mode = options.mode
    else:
        parser.print_help()

if not args:
    parser.print_help()
    quit()
# ----------------------------------------------------------

print('Initializing..')

# read main input file
files = codecs.open(args[0], 'r', 'utf-8').read().splitlines()

# load language data
lemmata = importLemmata(lemmaHandle)
stopwords = importStopwords(stopwordHandle)

localWordFreqs = {}
globalWordFreq = {}

print('Working through documents.. ')

progress = 0;

for f in files:
    # calculate progress
    progress += 1
    if progress%math.ceil(float(len(files))/float(20)) == 0:
        print(str(100*progress/len(files))+'%')
    
    # local term frequency map
    localWordFreq = {}
    
    localWords = codecs.open(f, 'r', 'utf-8').read()
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


print('Calculating.. ')

for f in files:

    writer = codecs.open(f + '_tfidf', 'w', 'utf-8')
    result = []
    # iterate over terms in f, calculate their tf-idf, put in new list
    for (term,freq) in localWordFreqs[f].items():
        tf = bool(float(freq))*(1 + math.log(float(freq)))
        idf = math.log(float(1 + len(files)) / float(1 + globalWordFreq[term]))
        tfidf = float(tf) * float(idf)
        result.append([tfidf, term])

    # sort result on tfidf and write them in descending order
    result = sorted(result, reverse=True)
    for (tfidf, term) in result[:top_k]:
        if display_mode == 'both':
            writer.write(term + '\t' + str(tfidf) + '\n')
        else:
            writer.write(term + '\n')

print('Success, with ' + str(len(files)) + ' documents.')