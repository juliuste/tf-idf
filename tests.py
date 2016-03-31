#!/usr/bin/env python
# encoding: utf-8

"""
File: tests.py
Author: Julius Tens
E-Mail: mail@julius-tens.de
Web: https://github.com/juliuste
Date: 31.03.2016

Some tests for the tfidf module.
"""

import tfidf

def test_tokenize():
	assert tfidf.tokenize(u'!Äöüß“ Habén, deswegen alsó!. .. …halb-sowichtig! echt_Mal dènn+so') == [u'Äöüß', u'Habén', u'deswegen', u'alsó', u'halb', u'sowichtig', u'echt', u'Mal', u'dènn', u'so']

def test_removeStopwords():
	assert tfidf.removeStopwords([u'Halló', u'ünd', u'Weltördnüsseß', u'im', u'lapîdar', u'a', u'Toll', u'undsoweiteründsófort'], [u'ünd', u'im', u'a', u'undsoweiteründsófort']) == [u'Halló', u'Weltördnüsseß', u'lapîdar', u'Toll']

def test_lemmatize():
	assert tfidf.lemmatize([u'Diésen', u'verwirklichten', u'Manifestes', u'Herkünft', u'sei', u'unbekannter', u'als', u'erwartet', u'sprach', u'der', u'Schimpanse'], {u'verwirklichten':u'verwirklichen', u'Manifestes':u'Manifest', u'sei':u'sein', u'unbekannter':u'unbekannt', u'erwartet':u'erwarten', u'sprach':u'sprechen'}) == [u'Diésen', u'verwirklichen', u'Manifest', u'Herkünft', u'sein', u'unbekannt', u'als', u'erwarten', u'sprechen', u'der', u'Schimpanse']

"""
def test_importStopwords():
	temp = tempfile.TempFile()
	assert tfidf.importStopwords(StringIO.write(u"Ein\n \n\nStopwort\n#kein\n#Wort\nzwei Wörter\nnormal")) == [u'Ein', u'Stopwort', u'zwei', u'normal']

def test_importLemmata():
	assert tfidf.importLemmata(StringIO.write(u"ganz normal\n \n\nwiederum\nkeine richtigen Stopwörter\noder nicht\n#aber sicher\nteste testen")) == {u'ganz':u'normal', u'oder':u'nicht', u'teste':u'testen'}
"""