import random


class Bid:
    def __init__(this, value, count):
        this.value = value
        this.count = count

    def isHigher(this, comparable):
        return comparable.value > this.value or \
            comparable.value == this.value and \
            comparable.count > this.count

    def isValid(this, dice):
        valueMatches = 0
        for x in dice:
            if x == this.value:
                valueMatches += 1
        return valueMatches >= this.count


class Player:
    idCounter = 1

    def __init__(this):
        this.diceValues = None
        this.currentBid = None
        this.diceCount = 5
        this.playerId = Player.idCounter
        Player.idCounter += 1

    def roll(this):
        arr = []
        i = 0
        while i < this.diceCount:
            arr.append(random.randint(1, 6))
            i += 1
        this.diceValues = arr

    def minusDie(this, diceTaken=1):
        this.diceCount -= diceTaken

    def isAlive(this):
        return this.diceCount > 0

    def bid(this, value, count):
        this.currentBid = Bid(value, count)

    def manualBid(this):
        value = input('Enter face value: ')
        count = input('Enter number of dice: ')
        this.bid(value, count)


class Round:
    roundCounter = 1

    def __init__(this, activePlayers):
        this.turnIndex = 1
        this.activePlayers = activePlayers
        this.roundNumber = Round.roundCounter
        Round.roundCounter += 1
        this.loser = None
        this.activePlayers[0].manualBid()
        this.rotate()

    def challenge(this, challenger: Player, challenged: Player):
        if challenged.currentBid.isValid():
            challenger.minusDie()
            this.loser = challenger
        else:
            challenged.minusDie()
            this.loser = challenged

        if not this.loser.isAlive():
            this.activePlayers.remove(this.loser)

    def rotate(this, bids: bool, ):
        if bids:
            this.turnIndex += 1


def initializePlayers(count, aiOn):
    players = []
    if aiOn:
        players.append(Player)
        i = 1
        while i < count:
            players.append(AI)
            i += 1
    else:
        i = 0
        while i < count:
            players.append(Player)
            i += 1
    return players


class Game:

    def __init__(this, mode, playerCount, aiOn):
        this.mode = mode
        this.players = initializePlayers(playerCount, aiOn)
        this.aiOn = aiOn
        Round.roundCounter = 1
        Player.idCounter = 1

    def start(this):
        activePlayers = this.players.copy()
        while len(activePlayers) > 1:
            round = Round(activePlayers)


class AI(Player):

    def __init__(this):
        super().__init__()

    def choose(this):
        #makes decision on what to play