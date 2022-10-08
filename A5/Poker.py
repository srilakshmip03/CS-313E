
import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards
    self.num_players = num_players

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)

      # self.players_hands is a sorted list of Card objects
      self.players_hands[i] = sorted_hand

      # for the purposes of printing the first chunk of info
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ': ' + hand_str)
    print()

    # see what kind of hand each player has
    hand_points = [0, 0, 0]	# create a list to store points for hand
    for i in range(self.num_players):
      print("Player " + str(i + 1) + ": ", end = "")
      if self.is_royal(self.players_hands[i]) != 0:
        print("Royal Flush")
        tup = (self.is_royal(self.players_hands[i]))
        hand_points[i] = tup[0], 10, i + 1
      elif self.is_straight_flush(self.players_hands[i]) != 0:
        print("Straight Flush")
        tup = ((self.is_straight_flush(self.players_hands[i])))
        hand_points[i] = tup[0], 9, i + 1
      elif self.is_four_kind(self.players_hands[i]) != 0:
        print("Four of a Kind")
        tup = (self.is_four_kind(self.players_hands[i]))
        hand_points[i] = (tup[0], 8, i + 1)
      elif self.is_full_house(self.players_hands[i]) != 0:
        print("Full House")
        tup = self.is_full_house(self.players_hands[i])
        hand_points[i] = (tup[0], 7, i + 1)
      elif self.is_flush(self.players_hands[i]) != 0:
        print("Flush")
        tup = self.is_flush(self.players_hands[i])
        hand_points[i] = (tup[0], 6, i + 1)
      elif self.is_straight(self.players_hands[i]) != 0:
        print("Straight")
        tup = self.is_straight(self.players_hands[i])
        hand_points[i] = (tup[0], 5, i + 1)
      elif self.is_three_kind(self.players_hands[i]) != 0:
        print("Three of a Kind")
        tup = self.is_three_kind(self.players_hands[i])
        hand_points[i] = (tup[0], 4, i + 1)
      elif self.is_two_pair(self.players_hands[i]) != 0:
        print("Two Pair")
        tup = self.is_two_pair(self.players_hands[i])
        hand_points[i] = (tup[0], 3, i + 1)
      elif self.is_one_pair(self.players_hands[i]) != 0:
        print("One Pair")
        tup = self.is_one_pair(self.players_hands[i])
        hand_points[i] = (tup[0], 2, i + 1)
      else:
        print("High Card")
        tup = self.is_high_card(self.players_hands[i])
        hand_points[i] = (tup[0], 1, i + 1)

    # sort by which player got the "best" outcome
    hand_points.sort(key=lambda tup: tup[1], reverse=True)
    print()

    # see if there are any ties. if there are, see how many and sort the ties according to score.
    res = [lis[1] for lis in hand_points]
    max_key = max(res)
    ties = res.count(max_key) - 1
    if ties == 0:
      print("Player " + str(hand_points[0][2]) + " wins.")
    else:
      for i in range(ties + 1):
        print("Player " + str(i + 1) + " ties.")

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ""

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ""

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Royal Flush"

  # determine if a hand is a straight flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ""

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ""

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Straight Flush"

  # determine if a hand is a four of a kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_four_kind(self, hand):
    fourk = False
    if (hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank) or \
            (hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank):
      points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      fourk = True

    if fourk:
      return points, "Four of a Kind"
    else:
      return 0, ""

  # determine if a hand is a full house
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_full_house (self, hand):
    full_house = False
    if hand[0].rank == hand[1].rank == hand[2].rank:
      if hand[3].rank == hand[4].rank:
        full_house =  True


    if hand[2].rank == hand[3].rank == hand[4].rank:
      if hand[0].rank == hand[1].rank:
        full_house = True

    if full_house:
      points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points, "Full House"

    else:
      return 0, ""

  # determine if a hand is a flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_flush (self, hand):
    same_suit = True
    for i in range(len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if same_suit:
      points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, "Flush"

    else:
      return 0, ""

  # determine if a hand is straight
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight (self, hand):
    rank_order = True
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ""

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Straight"

  # determine if a hand is a three of a kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_three_kind (self, hand):
    for i in range(2):
      if (hand[i].rank == hand[i + 1].rank == hand[i + 2].rank):
        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, "Three of a Kind"

    return 0, ""

  # determine if a hand is a two pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_two_pair (self, hand):
    one_pair = False
    two_pair = False
    for i in range(len(hand) - 3):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
      if (hand[i + 2].rank == hand[i + 3].rank):
        two_pair = True

    if one_pair and two_pair:
      points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, "Two Pair"

    else:
      return 0, ""

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    repeat = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True

    if (not one_pair):
      return 0, ""

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "One Pair"

  # determine if a hand is a  high card - no qualifications
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_high_card (self,hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "High Card"

def main():
  # read number of players from stdin
  file = open("poker.in")
  line = file.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()


if __name__ == "__main__":
  main()
