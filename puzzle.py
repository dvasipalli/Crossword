#!/usr/bin/python3

import random as r
import math as m

def print_board(board):
    print ("______________________________________\n")
    for u in range(0, len(board)):
        print ("|", end = "")
        for v in range(0, len(board[u])):
            print (board[u][v], end = "")
            print ("|", end = "")
        print ("\n______________________________________\n")

def board_available(word, row, col, index, board):
#horizontal placement
    if word['align'] == 'H':
        for u in range(col-index, col-index+word['len']):
            if u==col:
                continue
            if board[row][u] != '-':
                return False
        return True
#vertical placement
    if word['align'] == 'V':
        for u in range(row-index, row-index+word['len']):
            if u==row:
                continue
            if board[u][col] != '-':
                return False
        return True

def fill_board(word, row, col, index, board):
    i=0
#horizontal placement
    if word['align'] == 'H':
        for u in range(col-index, col-index+word['len']):
            if u==col:
                i+=1
                continue
            board[row][u] = word['word'][i]
            i+=1
#vertical placement
    if word['align'] == 'V':
        for u in range(row-index, row-index+word['len']):
            if u==row:
                i+=1
                continue
            board[u][col] = word['word'][i]
            i+=1

def place_if_fit(word, c, row, col, board):
    index = word['word'].find(c)
#consider vertical placement
    if row-index>0 and word['len']-index == grid_size-row:
        word['align'] = 'V'
        if(board_available(word, row, col, index, board)):
            fill_board(word, row, col, index, board)
            return True
        else:
            word['align'] = ''
#consider horizontal placement
    if col-index>0 and word['len']-index == grid_size-col:
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
num_words = 50
f = open("/usr/dict/words")
words = f.read()
word = []
pwords = []
word = words.split()

for i in range(0,num_words):
    temp = {}
    temp['word'] = word[m.floor(r.random()*(len(word)-1))]
    while(len(temp['word']) > 10):
        temp['word'] = word[m.floor(r.random()*(len(word)-1))]
    temp['row'] = -1
    temp['col'] = -1
    temp['align'] = ""
    temp['len'] = len(temp['word'])
    pwords.append(temp)

#print(pwords)
pwords = sorted(pwords, key =lambda k: len(k['word']), reverse = True)

print(pwords)

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

print_board(board)
for u in range(1, num_words):
    place_in_board(pwords[u], board)

