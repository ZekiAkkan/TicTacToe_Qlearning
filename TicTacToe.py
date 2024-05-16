import numpy as np
import pygame

class TicTacToe:
    """
    current_state: holds the current game current_state like [0 X 0 0 0 0 0 0 0]
    
    """
    
    def __init__(self):
        self.current_state = np.zeros(9, dtype=np.int8)
        self.winner = None
        self.player = 1
    
    def draw_current_game(self, screen):
        screen.fill((240, 235, 227))
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, (255, 255, 255), (j*100, i*100, 100, 100), 3)
                if self.current_state[i*3+j] == 1:
                    pygame.draw.line(screen, (0, 0, 0), (j*100+20, i*100+20), (j*100+80, i*100+80), 3)
                    pygame.draw.line(screen, (0, 0, 0), (j*100+80, i*100+20), (j*100+20, i*100+80), 3)
                elif self.current_state[i*3+j] == -1:
                    pygame.draw.circle(screen, (0, 0, 0), (j*100+50, i*100+50), 30, 3)
        pygame.display.flip()
    
    def get_current_game(self):
        return self.current_state
    
    def get_current_game_tuple(self):
        return tuple(self.current_state)

    def get_available_positions(self):
        return np.argwhere(self.current_state == 0).ravel()

    def reset_game(self):
        self.current_state = np.zeros(9, dtype=np.int8)
        self.player = 1

    def make_move(self, action):
        if action in self.get_available_positions():
            self.current_state[action] = self.player
            self.player *= -1
        else:
            print('It is not available')

    def _make_move(self, _current_state, action):
        _current_state[action] = self.player
        return _current_state

    def get_next_states(self):
        states = []
        _current_state = self.current_state
        _available_moves = self.get_available_positions()
        for move in _available_moves:
            states.append(self._make_move(_current_state=_current_state, action=move))
        return states

    def is_board_full(self):
        return all(self.current_state)

    
    def is_winner(self, isgame=False):
        winner_coordinates = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                        [0, 4, 8], [2, 4, 6]])
        for coordinate in winner_coordinates:
            total = sum(self.current_state[coordinate])
            if total == 3:  # X winner
                if isgame:
                    print('X is Winner!')
                self.winner = 1
                self.reset_game()
                return 1
            elif total == -3:  # O Winner
                if isgame:
                    print('O is Winner!')
                self.winner = -1
                self.reset_game()
                return -1
            elif sum(self.current_state == 1) == 5:  # Draw
                if isgame:
                    print('DRAW')
                self.winner = -2
                self.reset_game()
                return -2
        return False
