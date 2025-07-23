from backend.app.utils.poker_primitives import *
from random import shuffle
from collections import Counter
from itertools import combinations

"""
Player needs: Hand, variable for Highest card, Kicker variable.
"""
class Player():
    def __init__(self, hand: Hand, chips: int) -> None:
        self.hand = hand
        self.chips = chips
        self.kicker = self.hand.getKicker()
        self.comboScore = 0
        self.best_five_cards = []
    
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
    
    def validateGameState(self):
        pass
    
    def _evaluateHand(self, hand: Hand) -> list[Card], int:
        allCards: list[Card] = self.board + list(hand.getCards())
        highScore: int = -1
        for comb in combinations(allCards, 5):
            currFive = self._getBestFiveCards(comb)
            if currFive > highScore:
                highScore = currFive
                bestFive = comb
        return bestFive, highScore

    def _getBestFiveCards(self, cards: list[Card]) -> int:
        # Sort cards by rank
        sorted_cards = sorted(cards, key=lambda x: x.rank, reverse=True)
        
        # Check for flush
        suits = [card.getSuit() for card in sorted_cards]
        is_flush = len(set(suits)) == 1
        
        # Check for straight
        is_straight = True
        for i in range(len(sorted_cards)-1):
            if sorted_cards[i].rank != sorted_cards[i+1].rank + 1:
                is_straight = False
                break
                
        # Count rank frequencies
        rank_counts = {}
        for card in sorted_cards:
            if card.rank in rank_counts:
                rank_counts[card.rank] += 1
            else:
                rank_counts[card.rank] = 1
                
        # Find highest frequency
        max_freq = max(rank_counts.values())
        
        # Determine hand type and return appropriate score
        if is_straight and is_flush:
            if sorted_cards[0].rank == Rank.ACE:
                return 100000000 + sorted_cards[0].rank# Royal flush
            return 90000000 + sorted_cards[0].rank# Straight flush
            
        if max_freq == 4:
            highest_quad = max(rank for rank, count in rank_counts.items() if count == 4)
            kicker = max(rank for rank, count in rank_counts.items() if count != 4)
            return 80000000 + highest_quad * 10000 + 100 * kicker# Four of a kind
            
        if max_freq == 3 and len(rank_counts) == 2:
            return # Full house
            
        if is_flush:
            return # Flush
            
        if is_straight:
            return # Straight
            
        if max_freq == 3:
            return # Three of a kind
            
        if max_freq == 2:
            pairs = len([count for count in rank_counts.values() if count == 2])
            if pairs == 2:
                return # Two pair
            return # One pair
            
        return # High card
        
        

    def _generateDeck(self) -> list[Card]:
        return [Card(suit, rank) for suit in Suit for rank in Rank]
    
    def getAllHands(self) -> tuple[Hand]:
        return [p.getHand() for p in self.currPlayers]

    def __init__(self, players: int, startingChips: int):
        self.deck = self._generateDeck()
        shuffle(self.deck)
        self.currPlayers = [Player(self._generateRandomHand(), startingChips) for _ in range(players)]
        self.board = []
        self.gameState = "preflop"
    


if __name__ == "__main__":
    p = PokerEngine(2,2)
    print(p.getAllHands()[0])
