
import random as r
import math as m

class Crossword:
    """Generates a cross word puzzle"""
    def __init__(self, r, c, n):
        self.rows = r
        self.cols = c
        self.nwords = n
        self.board = [['-' for i in range(c)] for j in range(r)]    #intializing board with '-'
        self.pwords = []

    def CreateCrossword(self, words):
        #sorting words based in length descending order
        words = sorted(words, key =lambda k: k['len'], reverse = True)
        words[0]['row'] = 1
        words[0]['col'] = 1
        words[0]['align'] = 'H'
        self.board[1][1] = words[0]['word'][0]
        Crossword.fill_board(words[0], 1, 1, self.board)
        
        for i in range(1, len(words)):
            Crossword.place_in_board(self.rows, self.cols, self.board, words[i])

        return self.board

    @classmethod
    def place_in_board(cls, rows, cols, board, word):
        for u in range(0, rows):
            for v in range(0, cols):
                for c in word['word']:
                    if(board[u][v] == c):
                        if(Crossword.place_if_fit(rows, cols, board, word, c, u, v)):
                            return;

    @classmethod
    def place_if_fit(cls, rows, cols, board, word, c, row, col):
        index = word['word'].find(c)
    #consider vertical placement
        if row-index>=0 and row-index+word['len'] < rows:
            word['align'] = 'V'
            word['row'] = row-index
            word['col'] = col
            if(Crossword.board_available(word, row, col, board)):
                Crossword.fill_board(word, row, col, board)
                return True
            else:
                word['align'] = ''
    #consider horizontal placement
        if col-index>=0 and col-index+word['len']-index < cols:
            word['align'] = 'H'
            word['row'] = row
            word['col'] = col-index
            if(Crossword.board_available(word, row, col, board)):
                Crossword.fill_board(word, row, col, board)
                return True
            else:
                word['align'] = ''
        return False

    @classmethod
    def board_available(cls, word, row, col, board):
    #horizontal placement
        if word['align'] == 'H':
            for u in range(word['col'], word['col']+word['len']):
                if u==col:
                    continue
                if board[row][u] != '-':
                    word['row'] = -1
                    word['col'] = -1
                    return False
            return True
    #vertical placement
        if word['align'] == 'V':
            for u in range(word['row'], word['row']+word['len']):
                if u==row:
                    continue
                if board[u][col] != '-':
                    word['row'] = -1
                    word['col'] = -1
                    return False
            return True

    @classmethod
    def fill_board(cls, word, row, col, board):
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

