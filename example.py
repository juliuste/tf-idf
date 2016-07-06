#!/usr/bin/env python
# encoding: utf-8

"""
File: example.py
Author: Julius Tens
E-Mail: mail@julius-tens.de
Web: https://github.com/juliuste
Date: 15.05.2016
"""

import tfidfDE
from optparse import OptionParser

# __main__ execution
if __name__ == '__main__':

    # --- Parameter handling -----------------------------------
    parser = OptionParser(usage='usage: %prog [options] input_file')
    parser.add_option('-k', '--top-k', dest='top_k',
            help='output only terms with score no less k')
    parser.add_option('-o', '--wordsonly', action='store_true', dest='wordsOnly', default=False, 
            help='output only the words, not their rankings')
    parser.add_option('-n', '--nouns', action='store_true', dest='nouns', default=False, 
            help='prefer nouns (give them an advantage in the algorithm')
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False, 
            help='enable console logging')
    (options, args) = parser.parse_args()

    top_k = -1
    if options.top_k:
        top_k = int(options.top_k)
    nouns = bool(options.nouns)
    verbose = bool(options.verbose)
    showRanking = not bool(options.wordsOnly)

    if not args:
        parser.print_help()
        quit()


# read main input file
files = open(args[0], 'r').read().splitlines()

tfidfDE.analyze(files, top_k, nouns, showRanking, True, verbose)