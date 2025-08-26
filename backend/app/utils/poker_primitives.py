from enum import IntEnum
from enum import StrEnum


class Suit(IntEnum):
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3

    def __str__(self) -> str:
        symbolMap: dict[Suit] = {self.CLUBS: '♣', self.DIAMONDS: '♦',
                                 self.HEARTS: '♥', self.SPADES: '♠'}
        return symbolMap[self]

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self) -> str:
        mappings: set[str] = {self.JACK: 'J', self.QUEEN: 'Q', self.KING: 'K', self.ACE: 'A'}
        return mappings.get(self, str(self.value))

class HandCombo(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    SET = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    QUADS = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.suit}{self.rank}"
    
    def __str__(self):
        return f"{self.suit}{self.rank}"
    
    def compareTo(self, obj):
        if self.rank > obj.rank:
            return 1
        elif self.rank < obj.rank:
            return -1
        return 0
    def getSuit(self) -> Suit:
        return (self.suit)

class Hand:
    def __init__(self, card1: Card, card2: Card):
        self.cards: tuple[Card] = (card1, card2)
    def getKicker(self) -> Card:
        return self.cards[0] if self.cards[0].compareTo(self.cards[1]) == 1 else self.cards[1]
    def getCards(self) -> tuple[Card]:
        return self.cards
    def isPair(self) -> bool:
        return self.cards[0].compareTo(self.cards[1]) == 0
    def __str__(self):
        return f'{self.cards[0]} {self.cards[1]}'
    
class Board:
    def __init__(self, cards: list[Card]):
        self.cards = cards


if __name__ == "__main__":
    c: Card = Card(Suit.DIAMONDS, Rank.TEN)
    c2: Card = Card(Suit.DIAMONDS, Rank.FIVE)
    h: Hand = Hand(c, c2)
    print(h)