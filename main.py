import variables

switcherValue = 1
arguments = []


def switcher():
    match switcherValue:
        case 1:
            mainMenu()
        case _:
            variables.promptInputError()
            mainMenu()


def mainMenu():
    print(variables.mainMenuString())
    text = input('Command: ')
    argss = text.split(' ')


print('Welcome to\033[1m Liar\'s dice\033[0m!')
mainMenu()
