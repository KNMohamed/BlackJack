from .card import Card
from random import shuffle


class Deck:

  def __init__(self):
    all_suits = ['clubs', 'diamonds', 'hearts', 'spades']
    all_ranks = [
      '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    ]
    cards = [(suit, rank) for suit in all_suits for rank in all_ranks]
    self.cards = [Card(suit, rank) for suit, rank in cards]
    shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

  def deal_many(self, n):
    return [self.cards.pop() for i in range(n)]

  def __str__(self):
    return " ".join([str(card) for card in self.cards])

  def __repr__(self):
    return str(self)
