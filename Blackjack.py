  # File: Blackjack.py

  # Description: This program simulates a game of black jack among a user defined number of players.

  # Student's Name: Mathew Perez

  # Student's UT EID: mjp3457
 
  # Partner's Name: Samuel F. Gutierrez

  # Partner's UT EID: sfg384

  # Course Name: CS 313E 

  # Unique Number: 51340

  # Date Created: 2/16/2018

  # Date Last Modified: 2/16/2018

  
import  random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if self.rank == 1:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards

  def hit (self, card):
    self.cards.append(card)

  def getPoints (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10
    
    return count

  # does the player have 21 points or not
  def hasBlackjack (self):
    return len (self.cards) == 2 and self.getPoints() == 21

  # complete the code so that the cards and points are printed
  def __str__ (self):
    hand = ""
    for i in range (len(self.cards)):
      hand += (str(self.cards[i]) + ' ')
    return hand + "- "+ str(self.getPoints()) + " points"

# Dealer class inherits from the Player class
class Dealer (Player):
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True

  # over-ride the hit() function in the parent class
  # add cards while points < 17, then allow all to be shown
  def hit (self, deck):
    self.show_one_card = False
    while self.getPoints() < 17:
      self.cards.append (deck.deal())

  # return just one card if not hit yet by over-riding the str function
  def __str__ (self):
    if self.show_one_card:
      return str(self.cards[0])
    else:
      return Player.__str__(self)

class Blackjack (object):
  def __init__ (self, numPlayers = 1):
    self.deck = Deck()
    self.deck.shuffle()

    self.numPlayers = numPlayers
    self.Players = []

    # create the number of players specified
    # each player gets two cards
    for i in range (self.numPlayers):
      self.Players.append (Player([self.deck.deal(), self.deck.deal()]))

    # create the dealer
    # dealer gets two cards
    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

  def play (self):
    # Print the cards that each player has
    for i in range (self.numPlayers):
      print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))

    # Print the cards that the dealer has
    print ('Dealer: ' + str(self.dealer))
    print()

    # Each player hits until he says no
    playerPoints = []
    for i in range (self.numPlayers):
      while True:
        choice = input ("Player " + str(i+1)  + ', do you want to hit? [y / n]: ')
        if choice in ('y', 'Y'):
          (self.Players[i]).hit (self.deck.deal())
          points = (self.Players[i]).getPoints()
          print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))
          if points >= 21:
            print()
            break
        else:
          print()
          break
      playerPoints.append ((self.Players[i]).getPoints())

    # Dealer's turn to hit
    self.dealer.hit (self.deck)
    dealerPoints = self.dealer.getPoints()
    print ('Dealer: ' + str(self.dealer))
    print()

    # determine the outcome; you will have to re-write the code
    # it was written for just one player having playerPoints
    # do not output result for dealer
    # if the dealer has black jack
    if self.dealer.hasBlackjack():
      winners = []
      for i in range (len(self.Players)):
        if self.Players[i].hasBlackJack():
          winners.append(i+1)
      if len(winners) > 1:
        for i in range (len(winners)):
          print("Player " + str(winners[i]) + " ties")
    
    # if dealer busts
    elif (dealerPoints > 21):
      winners = []
      losers = []
      for i in range (len(self.Players)):
        if (self.Players[i].getPoints() <= 21):
         print ("Player " + str(i+1) + " wins")
        else:
         print("Player " + str(i+1) + " loses")
        
    elif not(self.dealer.hasBlackjack()):
      for x in range (len(self.Players)):
        if (self.dealer.getPoints() > self.Players[x].getPoints()) or self.Players[x].getPoints()>21:
          print("Player " + str(x+1) +" loses")
        elif self.dealer.getPoints() == self.Players[x].getPoints():
          print ("Player " + str(x+1) + " ties")
        else:
          print ("Player " + str(x+1) + " wins")

      print()

def main ():
  print()
  numPlayers = eval (input ('Enter number of players: '))
  while (numPlayers < 1 or numPlayers > 6):
    numPlayers = eval (input ('Enter number of players: '))
  print()
  game = Blackjack (numPlayers)
  game.play()

main()
