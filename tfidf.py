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
            python tfidf.py input_files.txt
    - This script will generate new files, one for each of the input files, with the suffix "_tfidf"
            which contains terms with corresponding tfidf score, each on a separate line

"""

supported_langs     = ('german')
# a list of (words-freq) pairs for each document
global_terms_in_doc = {}
# list to hold occurrences of terms across documents
global_term_freq    = {}
num_docs            = 0
lang                = 'german'
lang_dictionary     = {}
top_k               = -1
lemmaPath           = 'german/lemmata/list.csv'
stopwordPath        = 'german/stopwords/list.txt'

def loadLemmata(filePath): # updated
    f = open(filePath, 'r')
    for line in f:
        if len(line) == 0 or line[0] == '#':
            continue
        words = line.split()
        if len(words) != 2 or words[0] == words[1]:
            continue
        lang_dictionary[words[0]] = words[1]

def lemmatize(text): # updated
    for i in range(0,len(text)):
        if text[i] in lang_dictionary:
            text[i] = lang_dictionary[text[i]]
    
    # don't return any single letters
    text = [t for t in text if len(t) > 1]
    return text

def removeStopwords(text, filePath):
    # remove punctuation
    chars = ['.', '/', "'", '"', '„',  '?', '!', '#', '$', '%', '^', '&',
            '*', '(', ')', ' - ', '_', '+' ,'=', '@', ':', '\\', ',',
            ';', '~', '`', '´', '<', '>', '|', '[', ']', '{', '}', '–', '“',
            '»', '«', '°', '’']
    for c in chars:
        text = text.replace(c, ' ')
    
    text = text.split()

    stopwords = []
    f = open(filePath, 'r')
    for line in f:
        if len(line) == 0 or line[0] == '#':
            continue
        stopwords.append(line.split()[0])
    content = [w for w in text if w not in stopwords]
    return content

# __main__ execution

import math
from optparse import OptionParser

parser = OptionParser(usage='usage: %prog [options] input_file')
parser.add_option('-k', '--top-k', dest='top_k',
        help='output only terms with score no less k')
parser.add_option('-m', '--mode', dest='mode',
        help='display mode. can be either "both" or "term"')
(options, args) = parser.parse_args()

loadLemmata(lemmaPath)

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

reader = open(args[0])
all_files = reader.read().splitlines()

num_docs  = len(all_files)

print('initializing..')
for f in all_files:
    
    # local term frequency map
    terms_in_doc = {}
    
    doc_words    = open(f).read()
    #print 'words:\n', doc_words
    doc_words    = removeStopwords(doc_words, stopwordPath)
    #print 'after stopwords:\n', doc_words
    doc_words    = lemmatize(doc_words)
    #print 'after tokenize:\n', doc_words

    #quit()
    
    # increment local count
    for word in doc_words:
        if word in terms_in_doc:
            terms_in_doc[word] += 1
        else:
            terms_in_doc[word]  = 1

    # increment global frequency
    for (word,freq) in terms_in_doc.items():
        if word in global_term_freq:
            global_term_freq[word] += 1
        else:
            global_term_freq[word]  = 1

    global_terms_in_doc[f] = terms_in_doc

print('working through documents.. ')
for f in all_files:

    writer = open(f + '_tfidf', 'w')
    result = []
    # iterate over terms in f, calculate their tf-idf, put in new list
    max_freq = 0;
    for (term,freq) in global_terms_in_doc[f].items():
        if freq > max_freq:
            max_freq = freq
    for (term,freq) in global_terms_in_doc[f].items():
        idf = math.log(float(1 + num_docs) / float(1 + global_term_freq[term]))
        tfidf = float(freq) / float(max_freq) * float(idf)
        result.append([tfidf, term])

    # sort result on tfidf and write them in descending order
    result = sorted(result, reverse=True)
    for (tfidf, term) in result[:top_k]:
        if display_mode == 'both':
            writer.write(term + '\t' + str(tfidf) + '\n')
        else:
            writer.write(term + '\n')

print('success, with ' + str(num_docs) + ' documents.')
