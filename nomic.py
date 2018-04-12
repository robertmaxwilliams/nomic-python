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
rule_change = input('Enter the name of a .txt file starting with "# RULE XXX" \
(where XXX is a number) to replace that rule: ')

new_rule = ""
new_nomic = ""
tag = ""
if rule_change[-4:] == '.txt':
	# do stuff with file
	with open(rule_change) as change_file:
		for i, line in enumerate(change_file):
			if i == 0:
				if line[:8] == '# RULE 2':
					tag = line
				else:
					print('file doesn\'t start with rule definition, no go.')
					break
			else: 
				new_rule += line
	with open('nomic.py') as nomic:
		inside_tag = False
		has_replaced_rule = False
		for line in nomic:
			if line == tag:
				inside_tag, has_replaced_rule = True, True
				new_nomic += tag + new_rule
			elif inside_tag:
				if line[:8] == '# RULE 2':
					inside_tag = False
			else:
				new_rule += line
		if not has_replaced_rule:
			new_nomic += tag + new_rule
else:
	print('bad command, sorry, next player.')

