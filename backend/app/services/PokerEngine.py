from backend.app.utils.poker_primitives import *
from random import shuffle

"""
Player needs: Hand, variable for Highest card, Kicker variable.
"""
class Player():
    def __init__(self, hand: Hand, chips: int) -> None:
        self.hand = hand
        self.chips = chips
        self.kicker = self.hand.getKicker()
        self.combo = HandCombo.PAIR if self.hand.isPair() else HandCombo.HIGH_CARD
    
    def getChips(self) -> int:
        return self.chips
    
    def setChips(self, num: int) -> None:
        self.chips = num
    
    def setHand(self, h: Hand) -> None:
        self.hand = h
    
    def getHand(self) -> Hand:
        return self.hand
    
    def getCombo(self) -> HandCombo:
        return self.combo
    
    def setCombo(self, c: HandCombo) -> None:
        self.combo = c

class PokerEngine():
    """
    Pseudorandom
    """
    def _generateRandomHand(self) -> Hand:
        card1: Card = self.deck[0]
        self.deck.remove(card1)
        card2: Card = self.deck[0]
        self.deck.remove(card2)
        return Hand(card1, card2)
    
    def _validateGameState(self):
        pass

    def _generateDeck(self) -> list[Card]:
        return [Card(suit, rank) for suit in Suit for rank in Rank]
    
    def getAllHands(self) -> tuple[Hand]:
        return [p.getHand() for p in self.currPlayers]

    def __init__(self, players: int, startingChips: int):
        self.deck = self._generateDeck()
        shuffle(self.deck)
        self.currPlayers = [Player(self._generateRandomHand(), startingChips) for _ in range(players)]
    


if __name__ == "__main__":
    p = PokerEngine(2,2)
    print(p.getAllHands()[0])
