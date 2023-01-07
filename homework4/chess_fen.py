import re
from collections import deque
 
CHESS_PIECES = {"r": 5, "n": 3, "b": 3, "q": 9, "k": 4, "p": 1}
FILES = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
 
def are_kings_adjacent(fen_str): #not correcto
    fen = [x.lower() for x in fen_str.split("/")]
    deq = deque([fen.pop(0)])
    for rank in fen:
        deq.append(rank)
        ls = list(deq)
        if ls[0].count("k") + ls[1].count("k") > 1:
            return True
        else:
           deq.popleft()
    return False
 
def are_pawns_invalid(fen_str):
    fen = [x.lower() for x in fen_str.split("/")]
    first_last_fen = fen[0] + fen[-1]
    return first_last_fen.count("p") > 0
    
 
class ChessException(Exception):
    def __init__(self, message):
        self._message = message
        super().__init__(self._message)
 
 
class ChessPosition():
    def __init__(self, fen_str):
        self._fen = fen_str
        self._white_score = self.get_white_score()
        self._black_score = self.get_black_score()

        if self._fen.count("k") != 1 or self._fen.count("K") != 1:
            raise ChessException("kings")
        elif are_kings_adjacent(self._fen):
            raise ChessException("kings")
        elif are_pawns_invalid(self._fen):
            raise ChessException("pawns")
 
    def __str__(self):
        return self._fen
 
    def __len__(self):
        letters = "".join(re.findall("[a-zA-Z]+", self._fen))
        return len(letters)
 
    def __getitem__(self, coords):
        split_fen = self._fen.split("/")
        rank = split_fen[-int(coords[1])]
        row = []
        for elem in rank:
            if '0' < elem < '9':
                for _ in range(int(elem)):
                    row.append(None)
            else:
                row.append(elem)
        return row[FILES[coords[0]]]
 
    def get_white_score(self):
        white_pieces = [char for char in self._fen if char.isupper()]
        return ChessScore(white_pieces)
 
    def get_black_score(self):
        black_pieces = [char for char in self._fen if char.islower()]
        return ChessScore(black_pieces)
 
    def white_is_winning(self):
        return self._white_score > self._black_score
 
    def black_is_winning(self):
        return self._white_score < self._black_score
 
    def is_equal(self):
        return self._white_score == self._black_score
 
class ChessScore():
    def __init__(self, pieces):
        self._pieces = [char.lower() for char in pieces]
        self._score = 0
 
        for key in CHESS_PIECES:
            self._score += self._pieces.count(key) * CHESS_PIECES[key]
 
    def __int__(self):
        return self._score
 
    def __lt__(self, obj):
        return self._score < obj._score
 
    def __le__(self, obj):
        return self._score <= obj._score
 
    def __eq__(self, obj):
        return self._score == obj._score
 
    def __ne__(self, obj):
        return self._score != obj._score
 
    def __gt__(self, obj):
        return self._score > obj._score
 
    def __add__(self, obj):
        return self._score + obj._score
 
    def __sub__(self, obj):
        return self._score - obj._score