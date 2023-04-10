class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def cardValue(self):
    if self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
      return 10
    elif self.rank == 'A':
      return (1, 11)
    else:
      return int(self.rank)

  def __str__(self):
    return str(self.suit) + " of " + str(self.rank)

  def __repr__(self):
    return str(self)

  def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash(self.suit) + hash(self.rank)

  def __lt__(self, other):
    return self.rank < other.rank

  def __le__(self, other):
    return self.rank <= other.rank

  def __gt__(self, other):
    return self.rank > other.rank

  def __ge__(self, other):
    return self.rank >= other.rank
