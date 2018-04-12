from __future__ import division
from __future__ import print_function

# RULE 101
from random import randint as dice
# player.players has names on even index lines, followed by scores
# A player's name is proceeded by a '*' when it is their turn

with open('players.players', 'r') as players_file:
	players_text = list(players_file)
	players = players_text[::2]
	scores = players_text[1::2]

	for i in range(len(players)):
		if players[i][0] == '*':
			players[i] = players[i][1:]
			scores[i] = str(int(scores[i]) + dice(1, 6)) + '\n'
			next_i = (i+1) % len(players)		
			players[next_i] = '*' + players[next_i]
			next_player = players[next_i]
			break

	players_text_new = list()
	for i in range(len(players) * 2):
		if i % 2 == 0:
			players_text_new.append(players[i//2])
		else:
			players_text_new.append(scores[i//2])

with open('players.players', 'w') as players_file:
	players_file.write("".join(players_text_new))

# RULE 102
# self modify according to input

def get_changefile():
	changefile_name = input('Enter the name of a .txt file starting with "# RULE 2XX" \
(where 2XX is a number starting with 2) to replace that rule: ')

	if changefile_name[-4:] == '.txt':
		print('bad filename, sorry')
		return

	with open(changefile_name) as changefile:
		first_line = changefile.readline()

		if first_line[:8] != '# RULE 2':
			print('file doesn\'t start with rule definition for rule 200-299, no go.')
			return

	return changefile_name


def apply_change(changefile_name):
	new_nomic = ''
	with open(changefile_name) as changefile:
		header = changefile.readline()
		body = changefile.read()

	with open('nomic.py') as nomic:
		inside_to_be_replaced = False
		has_replaced_rule = False
		for line in nomic:
			if line == header:
				inside_to_be_replaced, has_replaced_rule = True, True
				new_nomic += header + body
			elif inside_tag:
				if line[:8] == '# RULE 2':
					inside_to_be_replaced = False
			else:
				new_rule += line
		if not has_replaced_rule:
			new_nomic += header + body

changefile_name = get_changefile()

if changefile_name:
	apply_change(changefile_name)
else:
	print('bad command, sorry, next player.')

print(next_player)
