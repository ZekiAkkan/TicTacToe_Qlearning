import numpy as np
import random
import pickle
import pygame
from TicTacToe import TicTacToe  # TicTacToe sınıfınızı ekleyin

class Agent:
    
    def __init__(self, game, screen, player='X', episode=100000, epsilon=0.9, discount_factor=0.6, eps_reduce_factor=0.01):
        self.game = game
        self.player = player
        self.brain = dict()
        self.episode = episode
        self.epsilon = epsilon
        self.discount_factor = discount_factor
        self.results = {'X': 0, 'O': 0, 'D': 0}
        self.test_results = {'X': 0, 'O': 0, 'D': 0}
        self.eps_reduce_factor = eps_reduce_factor
        self.screen = screen  # screen parametresi eklendi

    def save_brain(self, player):
        with open('brain'+player, 'wb') as brain_file:
            pickle.dump(self.brain, brain_file)

    def load_brain(self, player):
        try:
            with open('brain'+player, 'rb') as brain_file:
                self.brain = pickle.load(brain_file)
        except:
            print('No brain yet. You should train the agent first. So this game agent will play randomly')

    def reward(self, player, move_history, result):
        _reward = 0
        if player == 1:
            if result == 1:
                _reward = 1
                self.results['X'] += 1
            elif result == -1:
                _reward = -1
                self.results['O'] += 1
        elif player == -1:
            if result == 1:
                _reward = -1
                self.results['X'] += 1
            elif result == -1:
                _reward = 1
                self.results['O'] += 1
        if result == -2:
            self.results['D'] += 1
        move_history.reverse()
        for state, action in move_history:
            self.brain[state, action] = self.brain.get((state, action), 0.0) + _reward
            _reward *= self.discount_factor

    def use_brain(self):
        possible_actions = self.game.get_available_positions()
        max_qvalue = -1000
        best_action = possible_actions[0]
        for action in possible_actions:
            qvalue = self.brain.get((self.game.get_current_game_tuple(), action), 0.0)
            if qvalue > max_qvalue:
                best_action = action
                max_qvalue = qvalue
            elif qvalue == max_qvalue and random.random() < 0.5:
                best_action = action
                max_qvalue = qvalue
            elif len(possible_actions) == 9:
                best_action = random.choice(possible_actions)
                break

        return best_action

    def train_brain_x_byrandom(self):
        for _ in range(self.episode):
            if _ % 1000 == 0:
                print('Episode: '+str(_))
                self.epsilon -= self.eps_reduce_factor
            move_history = []
            while True:
                if sum(self.game.get_current_game() == 1) == 0 or random.random() < self.epsilon:
                    available_actions = self.game.get_available_positions()
                    action_x = random.choice(available_actions)

                    move_history.append([self.game.get_current_game_tuple(), action_x])

                    self.game.make_move(action_x)

                else:
                    action_x = self.use_brain()

                    move_history.append([self.game.get_current_game_tuple(), action_x])

                    self.game.make_move(action_x)

                if self.game.is_winner():
                    self.reward(1, move_history, self.game.winner)
                    break

                available_actions = self.game.get_available_positions()
                action_o = random.choice(available_actions)
                self.game.make_move(action_o)

                if self.game.is_winner():
                    self.reward(1, move_history, self.game.winner)
                    break

        self.save_brain('X')
        print('TRAINING IS DONE!')
        print('RESULTS:')
        print(self.results)

    def play_with_human(self):
        self.load_brain(self.player)
        order = 1 if self.player == 'X' else -1
        end_screen_opened = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and order == -1:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // 100
                    row = pos[1] // 100
                    action_o = row * 3 + column
                    if action_o in self.game.get_available_positions():
                        self.game.make_move(action_o)
                        self.game.draw_current_game(self.screen)
                        pygame.time.delay(500)
                        pygame.display.flip()
                        pygame.event.pump()
                        if self.game.is_winner(isgame=True) and not end_screen_opened:
                            self.show_end_game_screen()
                            end_screen_opened = True
                        else:
                            order *= -1
                elif event.type == pygame.MOUSEBUTTONDOWN and end_screen_opened:  # Yeniden başla butonunu kontrol et
                    pos = pygame.mouse.get_pos()
                    if 200 <= pos[0] <= 400 and 250 <= pos[1] <= 290:
                        self.game.reset_game()
                        self.game.draw_current_game(self.screen)
                        end_screen_opened = False

            if order == 1:  # X'in sırası
                action_x = self.use_brain()
                if action_x is not None:  # Bot hamle yapacaksa
                    self.game.make_move(action_x)
                    self.game.draw_current_game(self.screen)
                    pygame.time.delay(500)
                    pygame.display.flip()
                    pygame.event.pump()
                    if self.game.is_winner(isgame=True) and not end_screen_opened:
                        self.show_end_game_screen()
                        end_screen_opened = True
                    else:
                        order *= -1

            # İkinci oyunun sonunda kontrol edilecek
            if self.game.is_winner(isgame=True) and not end_screen_opened:
                self.show_end_game_screen()
                end_screen_opened = True

            if self.game.is_board_full() and not end_screen_opened:
                self.show_end_game_screen()
                end_screen_opened = True

            # Eğer oyun bitti ve bitiş ekranı gösterildiyse
            if end_screen_opened:
                # Yeniden başlat butonu tıklanırsa
                pos = pygame.mouse.get_pos()
                if 200 <= pos[0] <= 400 and 250 <= pos[1] <= 290:
                    end_screen_opened = False  # Bitiş ekranı kapatıldı
                    self.game.reset_game()  # Oyun sıfırlandı
                    self.game.draw_current_game(self.screen)  # Oyun tahtası çizildi
                    pygame.display.flip()  # Ekran güncellendi
                    order = 1 if self.player == 'X' else -1  # Eğer X oyuncu başlıyorsa, sıra onda olmalı

    def show_end_game_screen(self):
        end_screen = pygame.display.set_mode((600, 300))
        font = pygame.font.Font(None, 36)
        if self.game.winner == 1:
            message = "X Kazandı!"
            text_color = (0, 255, 0) 
        elif self.game.winner == -1:
            message = "O Kazandı!"
            text_color = (255, 0, 0) 
        else:
            message = "Berabere"
            text_color = (255, 255, 255) 
        text = font.render(message, True, text_color)
        text_rect = text.get_rect(center=(300, 150))
        end_screen.blit(text, text_rect)

        # Yeniden başla butonunu oluştur
        button_font = pygame.font.Font(None, 24)
        button_text = button_font.render("Tekrar Dene", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(300, 270))
        pygame.draw.rect(end_screen, (0, 0, 255), button_rect, border_radius=5)
        end_screen.blit(button_text, button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if button_rect.collidepoint(pos):
                        pygame.display.set_mode((300, 300))
                        self.game.reset_game()
                        self.game.draw_current_game(self.screen)
                        end_screen.fill((0, 0, 0))
                        pygame.display.flip()
                        return  # Döngüyü kır
