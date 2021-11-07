import numpy as np
import sys

class tic_tac_toe:
    def __init__(self):
        print('|---------------------------------------------------------------------------------------------------------------|')
        print('|| ==========    ==    =======      ==========    ========    =======      ==========    =========    ======== ||')
        print('||     ==        ==    ==               ==        ==    ==    ==               ==        ==     ==    ==       ||')
        print('||     ==        ==    ==       ==      ==        ========    ==       ==      ==        ==     ==    ======   ||')
        print('||     ==        ==    ==               ==        ==    ==    ==               ==        ==     ==    ==       ||')
        print('||     ==        ==    =======          ==        ==    ==    =======          ==        =========    ======== ||')
        print('|---------------------------------------------------------------------------------------------------------------|')
        print('                                           --SELECT PLAYERS--')
        self.grid = np.array([i for i in range(9)], dtype=str).reshape(3,3)
        self.allowed_indexes = np.arange(9, dtype=int)
        self.taken_indexes = []
        self.turn = 0
        self.players = {'X': input('PLAYER X: '), 'O': input('PLAYER O: ')}
    def print_grid(self):
        print('-------------')
        for i in range(3):
            print('| %s | %s | %s |' %(self.grid[i,0], self.grid[i,1], self.grid[i,2]))
            print('-------------')
    def update_grid(self, cell_number, player):
        self.allowed_indexes[cell_number] = 42069420
        self.taken_indexes.append(player_input)
        self.turn += 1
        self.grid.flat[cell_number] = player
    def take_input(self, player):
        while True:
            try:
                player_input = int(input('{} SELECT A CELL NUMBER: '.format(self.players[player])))
                assert(player_input in self.allowed_indexes)
            except ValueError:
                print('The input needs to be an integer, try again!')
            except AssertionError:
                if player_input in self.taken_indexes:
                    print('That cell is taken, try again!')
                else:
                    print('Invalid Cell number, try again!')
            else:
                break
        return player_input
    def test_win(self, player):
        for i in range(3):
            if np.all(self.grid[i] == self.grid[i,0])\
            or np.all(self.grid.T[i] == self.grid.T[i,0]):
                self.print_grid()
                sys.exit('{} WON!'.format(self.players[player]))
        if np.all(np.diagonal(self.grid) == self.grid[0,0])\
        or np.all(np.diagonal(np.fliplr(self.grid)) == self.grid[0,-1]):
           self.print_grid()
           sys.exit('{} WON!'.format(self.players[player]))
        if self.turn == 9:
            self.print_grid()
            sys.exit('DRAW!')
        return False


game = tic_tac_toe()
while True:
    game.print_grid()
    player_input = game.take_input('X')
    game.update_grid(player_input, 'X')
    game.test_win('X')

    game.print_grid()
    player_input = game.take_input('O')
    game.update_grid(player_input, 'O')
    game.test_win('O')
