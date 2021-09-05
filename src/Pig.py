# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */

import random as rnd


win_points = 20  # Points to win (decrease if testing)
players = []
def run():

    #set_players reads allows players to input how many players there are and what their names are.

    welcome_msg(win_points)
    global players
    players = set_players()

    status_msg(players)
    currentIndex = rnd.randint(0,len(players) - 1)#Randomizes an integer between index 0 and the array players length - 1 (max index)
    #current = players[currentIndex] #Applies random index to select first player
    executePlayerCommand(players[currentIndex])

class Player:

    def __init__(self, name='', id=0):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round
        self.ID = id


# ---- Game logic methods --------------

#Dice/roll logic
def rollDice():
    return rnd.randint(1,6)

def roll(current_player):
    rolledValue = rollDice()

    if rolledValue > 1:
        addRoundPoints(current_player, rolledValue)
        round_msg(rolledValue, current_player)
        hasWon = playerWon(current_player)
        if hasWon == False:
            executePlayerCommand(current_player)
        else:
            game_over_msg(current_player, False)


    else:
        round_msg(rolledValue, current_player)
        zeroRoundPoints(current_player)
        next(current_player)

#Current player logic
def next(current_player):
    addTotPts(current_player) #Adds Round Points to Total Points
    status_msg(players)
    nextID = current_player.ID % len(players) -1
    executePlayerCommand(players[nextID])

#Player command logic
def readPlayerCommand():
    _input = input("Choose a command (r = roll, n = next, q = quit game)\n")

    if _input == 'r' or _input == 'n' or _input =='q':
        return  _input
    else:
        return input("INPUT VALID COMMAND!! (r = roll, n = next, q = quit game)\n") #Make sure user inputs a valid command


def executePlayerCommand(current_player):
    currentPlayer_msg(current_player)
    command = readPlayerCommand()
    if command == 'r':
        roll(current_player)
    elif command == 'n':
        next(current_player)
    elif command == 'q':
        pass #MAKE SOMETHING CLEVER

# ---- IO Methods --------------
def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")


def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")


def round_msg(result, current_player):
    if result > 1:
        print("Got " + str(result) + " running total is " + str(current_player.roundPts))
    else:
        print("Got 1 lost it all!")

def addRoundPoints(current_player, addValue):
    current_player.roundPts += addValue

def zeroRoundPoints(current_player):
    current_player.roundPts = 0

def addTotPts(current_player):
    current_player.totalPts += current_player.roundPts
    current_player.roundPts = 0

def playerWon(current_player):
    if current_player.totalPts + current_player.roundPts >= win_points:
        return True
    else:
        return  False


def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")

def currentPlayer_msg(current_player):
    print(f"The current player is {current_player.name}")


def get_player_choice(player):
    input("Player is " + player.name + " > ")

def set_players():
    _players = []
    n = int(input("How many players are going to play? \n"))

    for i in range(n):
        outputIndex = i +1
        playerName = input(f"What is the name of player {outputIndex} ?\n")
        _players.append(Player(playerName, i))

    return  _players


# ----- Testing -----------------
# Here you run your tests i.e. call your game logic methods
# to see that they really work (IO methods not tested here)
def test():
    # This is hard coded test data
    # An array of (no name) Players (probably don't need any name to test)
    test_players = [Player(), Player(), Player()]
    # TODO Use for testing of logical methods (i.e. non-IO methods)


if __name__ == "__main__":
    run()
