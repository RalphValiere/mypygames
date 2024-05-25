# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:23:20 2024

@author: valie
"""

# The Rock Paper Scissors game

class RockPaperSci():
    def __init__(self, number_player, quantity_round):
        # Options to choose and match history set up
        from numpy import random
        self.choices = ['rock', 'paper', 'scissors']
        
        # Setting number of players
        while number_player > 2 or number_player <= 0:
            print('Please enter an number that is an integer and less than 3. ', 
                  'This game can only be played with 1 or 2 players.')
            number_player = input('Choose the number of players for this game: ') 
            number_player = int(number_player)        
        self.number_player = number_player
        
        # Setting number of rounds
        while type(quantity_round) != int:
            print('Please enter an number of round that is an integer.', 
                  ' You can play as many you want! Just enter an integer')
            quantity_round = input('Choose the number of round: ') 
            quantity_round = int(quantity_round)
        self.quantity_round = quantity_round
        
        # Setting up match history
        
        if self.number_player == 1:
            self.total_wins_solo = 0
            self.total_loss_solo = 0
            self.total_draw_solo = 0
        elif self.number_player == 2:
            self.total_wins_p_one = 0
            self.total_wins_p_two = 0
            self.total_draw_mult = 0
        
        # Message for completion of set up
        print('Your game has been set up.', self.number_player,
              'player(s) for', self.quantity_round, 'rounds.', 
              'You can start playing.')
        
    def play(self):
        from numpy import random
        
        # Iniatilizing the scores
        score_soloplayer = 0 # 1 player vs Computer
        score_computer = 0 # 1 player vs Computer
        score_player_one = 0 # Two players
        score_player_two = 0 # Two players
        
        # Playing the rounds now!
        for round in range(1,self.quantity_round+1):
            
            # Player 1 vs Computer
            if self.number_player == 1:
                print(f'Player 1 VS Computer - Round {round}')
                my_choice = input('Pick one of rock, paper or scissors: ')
                computer_choice = random.choice(self.choices)
                print(f'Computer choice: {computer_choice}')
                if my_choice == 'rock' and computer_choice == 'paper':
                    print('You lost! Computer is better than you! AI will replace you all!\n')
                    score_computer += 1
                elif my_choice == 'rock' and computer_choice == 'scissors':
                    print('You might have won this time, but AI will come back for you!\n')
                    score_soloplayer += 1
                elif my_choice == 'paper' and computer_choice == 'rock':
                    print('You might have won this time, but AI will come back for you!\n')
                    score_soloplayer += 1
                elif my_choice == 'paper' and computer_choice == 'scissors':
                    print('You lost! Computer is better than you! AI will replace you all!\n')
                    score_computer += 1
                elif my_choice == 'scissors' and computer_choice == 'rock':
                    print('You lost! Computer is better than you! AI will replace you all!\n')
                    score_computer += 1
                elif my_choice == 'scissors' and computer_choice == 'paper':
                    print('You might have won this time, but AI will come back for you!\n')
                    score_soloplayer += 1
                elif my_choice == computer_choice:
                    print('A draw? How can a human be equal to an AI?\n')
                    score_soloplayer += 0
                else:
                    print('You probably chose an illegal move! That means you lost! Ah Ah Ah!\n')
                    score_computer += 1
                    
            # Player 1 vs Player 2
            elif self.number_player == 2:
                print(f'Player 1 VS Player 2 - Round {round}')
                playerone = input('Player 1! Pick one of rock, paper or scissors: ')
                playertwo = input('Player 2! Pick one of rock, paper or scissors: ')
                if playerone == 'rock' and playertwo == 'paper':
                    print('Player 2 wins!!\n')
                    score_player_two += 1
                elif playerone == 'rock' and playertwo == 'scissors':
                    print('Player 1 wins!!\n')
                    score_player_one += 1
                elif playerone == 'paper' and playertwo == 'rock':
                    print('Player 1 wins!!\n')
                    score_player_one += 1
                elif playerone == 'paper' and playertwo == 'scissors':
                    print('Player 2 wins!!\n')
                    score_player_two += 1
                elif playerone == 'scissors' and playertwo == 'rock':
                    print('Player 2 wins!!\n')
                    score_player_two += 1
                elif playerone == 'scissors' and playertwo == 'paper':
                    print('Player 1 wins!!\n')
                    score_player_one += 1
                elif playerone == playertwo and playerone in self.choices:
                    print('This is a draw!\n')
                    score_player_one += 0
                    score_player_two += 0
                elif playerone not in self.choices and playertwo in self.choices:
                    print('Player 1 made an illegal move! Player 2 wins\n')
                    score_player_two += 1
                elif playerone in self.choices and playertwo not in self.choices:
                    print('Player 2 made an illegal move! Player 1 wins\n')
                    score_player_one += 1
                elif playerone not in self.choices and playertwo not in self.choices:
                    print('Both players made an illegal move! This is draw\n')
                    score_player_one += 0
                    score_player_two += 0
                    
        # Compiling scores now
        if self.number_player == 1:
            self.score_soloplayer = score_soloplayer
            self.score_computer = score_computer
            self.number_draw = self.quantity_round - score_soloplayer - score_computer
            self.score_player_one = 'Game mode: "Player vs Computer". Select "score_soloplayer" to see score'
            self.score_player_two = 'Game mode: "Player vs Computer". Select "score_soloplayer" to see score'
            
            # Results of the game
            if self.score_soloplayer > self.score_computer:
                print('\n\nYou have won the game!\n\nCONGRATULATIONS!!')
                self.total_wins_solo += 1
            elif self.score_soloplayer < self.score_computer:
                print('\n\nYou have lost the game!\n\nMaybe next time you can win!')
                self.total_loss_solo += 1
            elif self.score_soloplayer == self.score_computer:
                print('\n\nThe game ended with a draw!\n\nWanna play again?')
                self.total_draw_solo += 1
                     
        elif self.number_player == 2:
            self.score_player_one = score_player_one 
            self.score_player_two = score_player_two
            self.number_draw = self.quantity_round - score_player_one - score_player_two
            self.score_soloplayer = 'Game mode: "Multiplayers". Select "score_player_one" or "score_player_two"'
            self.score_computer = 'Game mode: "Multiplayers". Select "score_player_one" or "score_player_two"'
            
            # Results of the game
            if self.score_player_one > self.score_player_two:
                print('\n\nPlayer 1 has won the game!\n\nCONGRATULATIONS TO PLAYER 1!!')
                self.total_wins_p_one += 1
            elif self.score_player_one < self.score_player_two:
                print('\n\nPlayer 2 has won the game!\n\nCONGRATULATIONS TO PLAYER 2!!')
                self.total_wins_p_two += 1
            elif self.score_player_one == self.score_player_two:
                print('\n\nThe game ended with a draw!\n\nWanna play again?')
                self.total_draw_mult += 1
    
    def game_history(self):
        
        if self.number_player == 1:
            print(' Number  of matches won:', self.total_wins_solo, 'match(es)\n',
                  'Number of matches lost:', self.total_loss_solo, 'match(es)\n',
                  'Number of draws:', self.total_draw_solo, 'match(es)\n')
        elif self.number_player == 2:
            print(' Number  of matches won by Player 1:', self.total_wins_p_one, 'match(es)\n',
                  'Number of matches won by Player 2:', self.total_wins_p_two, 'match(es)\n',
                  'Number of draws between Player 1 and Player 2:', self.total_draw_mult, 'match(es)\n')
            
# Testing for Player vs Computer

game_on = RockPaperSci(1, 10)
game_on.play()
game_on.score_soloplayer
game_on.score_computer
game_on.score_player_one
game_on.game_history()


# Testinf for two players

game_on = RockPaperSci(2, 5)
game_on.play()
game_on.score_soloplayer
game_on.score_computer
game_on.score_player_one
game_on.game_history()
