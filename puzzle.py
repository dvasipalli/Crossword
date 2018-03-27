#!/usr/bin/python3

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
                print (" ", end = "")
                print (board[u][v], end = "")
                print (" |", end = "")
        print ()
    print("+", end = "")
    for v in  range(0, len(board)):
        print ("---+", end = "")
    print ()

def print_words(pwords):
    for word in pwords:
        print ("word: {0:s} | board index[row, col]: [{1:d}, {2:d}] | align: {3:s}\n".format(word['word'], word['row'], word['col'], word['align']))

def board_available(word, row, col, index, board):
#horizontal placement
    if word['align'] == 'H':
        for u in range(col-index, col-index+word['len']):
            if u==col:
                continue
            if board[row][u] != '-':
                return False
        word['row'] = row
        word['col'] = col-index
        return True
#vertical placement
    if word['align'] == 'V':
        for u in range(row-index, row-index+word['len']):
            if u==row:
                continue
            if board[u][col] != '-':
                return False
        word['row'] = row-index
        word['col'] = col
        return True

def fill_board(word, row, col, index, board):
    i=0
#horizontal placement
    if word['align'] == 'H':
        for u in range(word['col'], word['col']+word['len']):
            if u==col:
                i+=1
                continue
            board[word['row']][u] = word['word'][i]
            i+=1
#vertical placement
    if word['align'] == 'V':
        for u in range(word['row'], word['row']+word['len']):
            if u==row:
                i+=1
                continue
            board[u][word['col']] = word['word'][i]
            i+=1

def place_if_fit(word, c, row, col, board):
    index = word['word'].find(c)
#consider vertical placement
    if row-index>0 and row-index+word['len'] < grid_size:
        word['align'] = 'V'
        if(board_available(word, row, col, index, board)):
            fill_board(word, row, col, index, board)
            return True
        else:
            word['align'] = ''
#consider horizontal placement
    if col-index>0 and col-index+word['len']-index < grid_size:
        word['align'] = 'H'
        if(board_available(word, row, col, index, board)):
            fill_board(word, row, col, index, board)
            return True
        else:
            word['align'] = ''
    return False

def place_in_board(word, board):
    for u in range(0, grid_size):
        for v in range(0, grid_size):
            for c in word['word']:
                if(board[u][v] == c):
                    if(place_if_fit(word, board[u][v], u, v, board)):
                        return;

grid_size = 15
num_words = 10
f = open("words")
words = f.read()
word = []
pwords = []
word = words.split()

for i in range(0, num_words):
    temp = {}
    temp['word'] = word[m.floor(r.random()*(len(word)-1))]
    temp['len'] = len(temp['word'])
    while(temp['len'] > grid_size-3 or temp['len'] < 3):
        temp['word'] = word[m.floor(r.random()*(len(word)-1))]
        temp['len'] = len(temp['word'])
    temp['row'] = -1
    temp['col'] = -1
    temp['align'] = ""
    temp['word'] = temp['word'].upper()
    pwords.append(temp)

pwords = sorted(pwords, key =lambda k: len(k['word']), reverse = True)

board = []

for u in range(0, grid_size):
    board.append([])
    for v in range(0,grid_size):
        board[u].append('-');

pwords[0]['row'] = 1
pwords[0]['col'] = 1
pwords[0]['align'] = 'H'

board[1][1] = pwords[0]['word'][0]
fill_board(pwords[0], 1, 1, 0, board)

for u in range(1, num_words):
    place_in_board(pwords[u], board)

print_board(board)
print_words(pwords)
