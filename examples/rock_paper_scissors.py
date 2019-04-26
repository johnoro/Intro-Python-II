# import module we need
import random

# file i/o functions for historical results
def load_results():
	with open("history.txt", "r") as text_file:
		history = text_file.read().split(",")
	return history

def save_results( w, t, l):
	with open("history.txt", "w") as text_file:
		text_file.write(f'{w},{t},{l}')


def user_win():
	global wins
	wins += 1
	return "you win :)"

def tie():
	global ties
	ties += 1
	return 'tie!'

def computer_win():
	global losses
	losses += 1
	return "computer wins :("


rps = [0, 'rock', 'paper', 'scissors']

def rpsgame(user, comp):
	user = rps[user]
	comp = rps[comp]
	def printResult(result): print(f'Computer chose {comp}...{result}')

	if user == comp:
		printResult(tie())
	elif (user == 'rock' and comp == 'scissors') \
			or (user == 'paper' and comp == 'rock') \
			or (user == 'scissors' and comp == 'paper'):
		printResult(user_win())
	else:
		printResult(computer_win())

	print()


results = map(int, load_results())
wins, ties, losses = results
print('Welcome to Rock, Paper, Scissors!')

def next_round():
	global computer, user, wins, ties, losses

	print('Wins: %s, Ties: %s, Losses: %s' % (wins, ties, losses))
	print('Please choose to continue...')

	computer = random.randint(1,3)
	user = int(input('[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n'))


next_round()

# gameplay loop
while not user == 9:
	if user not in range(1, 4):
		print("Invalid selection. Please try again.")
	else:
		rpsgame(user, computer)
	next_round()

save_results(wins, ties, losses)
