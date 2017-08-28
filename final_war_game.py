# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# mycards = [(s,r) for s in SUITES for r in RANKS]

# Same Method is as above ...
# mycards = []
# for r in RANKS:
#     for s in SUITES:
#         mycards.append((s,r))

class Deck():

    def __init__(self):
        print("Craeting New Ordered Deck!")
        self.allcards = [(s,r) for s in SUITES for r in RANKS]

    def Shuffling(self):
        print("Shuffling DEck!")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])



class Hand():

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()



class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Returs True if player still has cards left
        """
        return len(self.hand.cards) != 0


# GAME PLAY
print('Welcome to War Game!')
# Create a new Deck
d = Deck()
d.Shuffling()
half1, half2 = d.split_in_half()

#  Crate both players
comp = Player("computer", Hand(half1))

name = input("What is your name?  ")
user = Player(name, Hand(half2))

# Play ON automatically
total_round = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_round += 1
    print("Time for new rounds")
    print('here are the current standing!')
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(comp.name + " has the count: " + str(len(user.hand.cards)))
    print('play a card!')
    print('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print('war!')

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print('Game over, number of rounds:' + str(total_round))
print('a war happened '+ str(war_count) + ' times')
print('The Computer still have cards? ')
print(str(user.still_has_cards()))
print('The Human Player still have cards? ')
print(str(comp.still_has_cards()))
