Nomic Python is not a python implementation of Nomic

Nomic Python is not a model for the economy

Nomic Python is:

* Self modifying 
* Multiplayer
* Version controlled

There are no rules except the code, nomic.py

Actually, there are a few rules. And setup.

* Players may not run any other commands or modify any files not ending in .txt
* The only commands that can be ran are `python nomic.py` and `git commit -am "any text you want"`
* the last line printed by nomic.py is the name of the next player to play
* If nomic.py fails to run or print out a user's name as the last line, run `git revert`, TODO how to use git revert until all is good

Setup:

* clone this repo
* modify players.players to reflect who is playing. Names should be sorted alphabetically

How to play: (making nomic.py modify this section is considered __dangerous__ by some)
* The first player in players.payers run nomic and gives it some input over stdin. Editing .txt files before, during, or after runing nomic.py is allowed
* The last line printed from nomic.py should be a players name. They get to go next.

Win Condition: (this part is still up to debate, below are suggestions)
* nomic.py become deleted on your turn
* you get a segfault
* your score in players.players exceeds 10 and nomic.py prints `your name WINNER`
