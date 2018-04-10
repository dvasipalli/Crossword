#!/usr/bin/python3

import crossword as cr
import random as r
import math as m

def print_board(board):
    for u in range(0, len(board)):
        print("+", end = "")
        for v in  range(0, len(board[u])):
            print ("---+", end = "")
        print ("\n|", end = "")
        for v in range(0, len(board[u])):
            if board[u][v] == '-':
                print ("   |", end = "")
            else:
                print (" {0:s} |".format(board[u][v]), end = "")
        print ()
    print("+", end = "")
    for v in  range(0, len(board)):
        print ("---+", end = "")
    print ()

def print_words(pwords):
    for word in pwords:
        print ("word: {1:{0:d}s} | board index[row, col]: [{2:3d}, {3:3d}] | align: {4:s}".format(pwords[0]['len'], word['word'], word['row'], word['col'], word['align']))
        

f = open("words", "r")
s = f.read()
tempwords = s.split()
numwords = 15
nummin = 3
nummax = 13
rows = 15
cols = 15

words = []

for i in range(0, numwords):
    temp = {}
    temp['word'] = tempwords[m.floor(r.random()*len(tempwords))]
    temp['len'] = len(temp['word'])
    while(temp['len'] > nummax or temp['len'] < nummin):
        temp['word'] = tempwords[m.floor(r.random()*(len(tempwords)-1))]
        temp['len'] = len(temp['word'])
    temp['row'] = -1
    temp['col'] = -1
    temp['align'] = ''
    temp['hint'] = "this is a place holder for hints"
    words.append(temp)

cross = cr.Crossword(rows, cols, numwords)

b = cross.CreateCrossword(words)

print_board(b)
