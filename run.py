import pygame
from TicTacToe import TicTacToe
from Agent import Agent

pygame.init()
screen = pygame.display.set_mode((300, 300))  # ekran oluşturuldu
pygame.display.set_caption('Tic Tac Toe')

game = TicTacToe()
agent = Agent(game, screen, 'X', episode=100000)  # screen parametresi tanımlandı

agent.train_brain_x_byrandom()

agent.play_with_human()
