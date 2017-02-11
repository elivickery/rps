# First Draft of RPS project

#import random module for later use
import random

# Greet the user and ask for input

def ask_for_input():
	print 'Welcome to Rock Paper Scissors.'
	user_choice = raw_input('Make a choice: rock (R), paper (P) or scissors (S).')


def get_computer_choice():
	computer_choice = random.choice(['R','P','S'])
	return computer_choice

def beats_list(user_choice,computer_choice):

	beats_dict = {
		'R' : {

			'beats' : 'S',
			'ties' : 'R',
			'loses to' : 'P'

			},

		'P' : {

			'beats' : 'R',
			'ties' : 'P',
			'loses to' : 'S'
		},

		'S' : {

			'beats' : 'P',
			'ties' : 'S',
			'loses to' : 'R'
		}
	}

	user_option_beats = beats_dict[user_choice]['beats']
	user_option_ties = beats_dict[user_choice]['ties']
	user_option_loses_to = beats_dict[user_choice]['loses to']

	computer_option_beats = beats_dict[computer_choice]['beats']
	computer_option_ties = beats_dict[computer_choice]['ties']
	computer_option_loses_to = beats_dict[computer_choice]['loses to']


def main():
	print ask_for_input()

	if(user_choice == 'R' || user_choice == 'P' || user_choice == 'S'):
		print 'You picked %!' % (user_choice)
		print get_computer_choice()
		print beats()
	else:
		print "I didn't understand that. Try again."
		print ask_for_input()

	print 
