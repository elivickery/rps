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
	user_choice = str(raw_input('Make a choice: rock (R), paper (P) or scissors (S). ')).upper()

	while True:
		if(user_choice in ('R','P','S')):
			return user_choice
		else:
			user_choice = str(raw_input("I didn't understand that. Try again: R, P or S? ")).upper()
	else:
		exit()


def get_computer_choice(prev_choice):

	# ## Randomly generated computer choice
	# computer_choice = random.choice(['R','P','S'])
	# return computer_choice

	## Computer strategy
	if(prev_choice == 'R'):
		computer_choice = 'P'
	elif(prev_choice == 'P'):
		computer_choice = 'S'
	elif(prev_choice == 'S'):
		computer_choice = 'R'
	else:
		computer_choice = random.choice(['R','P','S'])	

	return computer_choice	


def get_beats_list(user_choice,computer_choice):
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

	computer_option_beats = beats_dict[computer_choice]['beats']
	computer_option_loses_to = beats_dict[computer_choice]['loses to']

	if user_choice == computer_option_loses_to:
		result = 'Win'
	elif user_choice == computer_option_beats:
		result = "Lose"
	else:
		result = 'Tie'

	return result


def play_again(number_wins,prev_choice):

	while True:

		play_again_choice = str(raw_input('Play again? Y/N: ')).upper()

		if(play_again_choice == 'Y'):
			print run_game(number_wins,prev_choice)
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


def run_game(number_wins,prev_choice):

		user_choice = get_user_choice()
		computer_choice = get_computer_choice(prev_choice)

		beats_result = get_beats_list(user_choice, computer_choice)

		print_slow('\n...\n...\n...\n')

		print "Your choice was %s.\n\nThe computer's choice was %s.\n" % (user_choice,computer_choice)

		if(beats_result == 'Win'):
			number_wins += 1
			print 'You win!'
		elif(beats_result == 'Lose'):
			print 'The computer wins!'
		else:
			print "It's a tie!"

		print "Number of times you've won so far: %s" % (number_wins)

		play_again(number_wins,user_choice)

		return user_choice


def main():
	wins = 0
	prev_choice = None
	print 'Welcome to Rock Paper Scissors!\n'
	print run_game(wins,prev_choice)


print main()
