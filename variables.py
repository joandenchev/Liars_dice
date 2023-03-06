def mainMenuString():
    return '''
Main menu:
1 - start a coop game 
2 - start a pvp game
4 - go to settings
9 - exit
[game options: total player count; mode (1 for wild, 0 for normal)]
---------------------------'''


def settingsString():
    return '''
Settings:
1 - change default values
[options: 
which modes to apply to (1 - coop, 2 - pvp, 3 - both);
which value to change (1 - total player count, 2 - wild mode) 
||
pass 0 as first option to preview current settings
]
0 - go back to main menu
---------------------------'''


def promptInputError():
    return '''
Invalid input!
Please try again!
---------------------------'''
