# First Draft of RPS project

#import random and time modules for later use
import random
import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)

def get_user_choice():
	user_choice = str(raw_input('Welcome to Rock Paper Scissors!\nMake a choice: rock (R), paper (P) or scissors (S). ')).upper()

	while True:
		if(user_choice in ('R','P','S')):
			return user_choice
		else:
			user_choice = str(raw_input("I didn't understand that. Try again: R, P or S? ")).upper()
	else:
		exit()


def get_computer_choice():
	computer_choice = random.choice(['R','P','S'])
	return computer_choice


def get_beats_list(user_choice,computer_choice):
	beats_dict = {
		'R' : {
			'alias' : 'rock',
			'beats' : 'S',
			'ties' : 'R',
			'loses to' : 'P'

			},

		'P' : {
			'alias' : 'paper',
			'beats' : 'R',
			'ties' : 'P',
			'loses to' : 'S'
		},

		'S' : {
			'alias' : 'scissors',
			'beats' : 'P',
			'ties' : 'S',
			'loses to' : 'R'
		}
	}

	computer_option_beats = beats_dict[computer_choice]['beats']
	computer_option_loses_to = beats_dict[computer_choice]['loses to']

	if user_choice == computer_option_loses_to:
		return 'You win!'
	elif user_choice == computer_option_beats:
		return 'The computer wins!'
	else:
		return "It's a tie!"


def play_again():

	while True:
		
		play_again_choice = str(raw_input('Play again? Y/N: ')).upper()
		
		if(play_again_choice == 'Y'):
			print run_game()
		elif (play_again_choice == 'N'):
			print 'Ok, thanks for playing!'
			exit()
		elif (play_again_choice in ("CONVINCE ME","NOT SURE","I DON'T KNOW")):
			convince_messages = ("Rock Paper Scissors is the best game ever! Don't believe me? Try it yourself.","C'mon, let's play a game!","You should definitely type Y.")
			print random.choice(convince_messages)
		else:
			print "I didn't understand that."
	
	else:
		exit()


def run_game():

		user_choice = get_user_choice()
		computer_choice = get_computer_choice()

		beats_result = get_beats_list(user_choice, computer_choice)

		print_slow('\n...\n...\n...\n')

		return "Your choice was %s.\n\nThe computer's choice was %s.\n\n%s\n" % (user_choice,computer_choice,beats_result)


def main():

	print run_game()
	print play_again()


print main()