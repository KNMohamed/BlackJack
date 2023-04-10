class Player():

  def __init__(self):
    self.hand = []
    self.possibleScores = (0, 0)

  def drawCard(self, deck):
    self.hand.append(deck.deal())

  # def calculateHandScore(self):
  #   for card in self.hand:
  #     cardValue = card.cardValue()
  #     if cardValue[0] == 1:
  #       self.possibleScores = self.possibleScores + (cardValue[1], )
