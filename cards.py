from random import shuffle
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit

class Deck:
    ranks = {'2','3','4','5','6','7','8','9','J','Q','K','A'}
    suits = {'\u2660','\u2661','\u2662','\u2663'}
    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank,suit))
    def dealCard(self):
        return self.deck.pop()
    def shuffle(self):
        shuffle(self.deck) 

first = Deck()
print(first.dealCard().getRank)