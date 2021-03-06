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

import tfidfDE, io

def test_tokenize():
	assert tfidfDE.tokenize('!Äöüß“ Habén, deswegen alsó!. .. …halb-sowichtig! echt_Mal dènn+so') == ['Äöüß', 'Habén', 'deswegen', 'alsó', 'halb', 'sowichtig', 'echt', 'Mal', 'dènn', 'so']

def test_removeStopwords():
	assert tfidfDE.removeStopwords(['Halló', 'ünd', 'Weltördnüsseß', 'im', 'lapîdar', 'a', 'Toll', 'undsoweiteründsófort'], ['ünd', 'im', 'a', 'undsoweiteründsófort']) == ['Halló', 'Weltördnüsseß', 'lapîdar', 'Toll']

def test_lemmatize():
	assert tfidfDE.lemmatize(['Diésen', 'verwirklichten', 'Manifestes', 'Herkünft', 'sei', 'unbekannter', 'als', 'erwartet', 'sprach', 'der', 'Schimpanse'], {'verwirklichten':'verwirklichen', 'Manifestes':'Manifest', 'sei':'sein', 'unbekannter':'unbekannt', 'erwartet':'erwarten', 'sprach':'sprechen'}) == ['Diésen', 'verwirklichen', 'Manifest', 'Herkünft', 'sein', 'unbekannt', 'als', 'erwarten', 'sprechen', 'der', 'Schimpanse']

def test_isNoun():
	assert tfidfDE.isNoun('Änderungsantrag') == True
	assert tfidfDE.isNoun('umgänglich') == False
	assert tfidfDE.isNoun('a') == False
	assert tfidfDE.isNoun('1') == False
	assert tfidfDE.isNoun('“') == False
	assert tfidfDE.isNoun('') == False
	assert tfidfDE.isNoun(' ') == False
	assert tfidfDE.isNoun("\n") == False

def test_importStopwords():
	assert tfidfDE.importStopwords(io.StringIO("Ein\n \n\nStopwort\n#kein\n#Wort\nzwei Wörter\nnormal")) == ['Ein', 'Stopwort', 'zwei', 'normal']

def test_importLemmata():
	assert tfidfDE.importLemmata(io.StringIO("ganz normal\n \n\nwiederum\nkeine richtigen Stopwörter\noder nicht\n#aber sicher\nteste testen")) == {'ganz':'normal', 'oder':'nicht', 'teste':'testen'}