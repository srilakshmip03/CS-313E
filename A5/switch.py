#  File: Poker.py

#  Description:

#  Student's Name: Srila Palanikumar

#  Student's UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: September 18, 2022

#  Date Last Modified: September 20, 2022

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


class Poker(object):
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        print()

        # determine the each type of hand and print
        points_hand = []  # create list to store points for each hand
        h_hand = []  # create list to store h value for each hand
        for i in range(len(self.players_hands)):
            if self.is_royal(self.players_hands[i]) != 0:
                points_hand.append(self.is_royal(self.players_hands[i]))
                h_hand.append(10)
                print("Player", str(i + 1) + ": Royal Flush")
            elif self.is_straight_flush(self.players_hands[i]) != 0:
                points_hand.append(self.is_straight_flush(self.players_hands[i]))
                h_hand.append(9)
                print("Player", str(i + 1) + ": Straight Flush")
            elif self.is_four_kind(self.players_hands[i]) != 0:
                points_hand.append(self.is_four_kind(self.players_hands[i]))
                h_hand.append(8)
                print("Player", str(i + 1) + ": Four of a Kind")
            elif self.is_full_house(self.players_hands[i]) != 0:
                points_hand.append(self.is_full_house(self.players_hands[i]))
                print("Player", str(i + 1) + ": Full House")
                h_hand.append(7)
            elif self.is_flush(self.players_hands[i]) != 0:
                points_hand.append(self.is_flush(self.players_hands[i]))
                print("Player", str(i + 1) + ": Flush")
                h_hand.append(6)
            elif self.is_straight(self.players_hands[i]) != 0:
                points_hand.append(self.is_straight(self.players_hands[i]))
                print("Player", str(i + 1) + ": Straight")
                h_hand.append(5)
            elif self.is_three_kind(self.players_hands[i]) != 0:
                points_hand.append(self.is_three_kind(self.players_hands[i]))
                print("Player", str(i + 1) + ": Three of a Kind")
                h_hand.append(4)
            elif self.is_two_pair(self.players_hands[i]) != 0:
                points_hand.append(self.is_two_pair(self.players_hands[i]))
                print("Player", str(i + 1) + ": Two Pair")
                h_hand.append(3)
            elif self.is_one_pair(self.players_hands[i]) != 0:
                points_hand.append(self.is_one_pair(self.players_hands[i]))
                h_hand.append(2)
                print("Player", str(i + 1) + ": One Pair")
            else:
                points_hand.append(self.is_high_card(self.players_hands[i]))
                h_hand.append(1)
                print("Player", str(i + 1) + ": High Card")
        print()

        # determine winner and print
        max_players = []  # list of players with max h value
        max_val = max(h_hand)
        for i in range(len(points_hand)):
            if h_hand[i] == max_val:
                max_players.append(i)
            else:
                continue
        j = 0
        if len(max_players) == 1:
            print("Player", str(max_players[0] + 1), "wins.")
        else:
            while j < len(max_players):
                if points_hand[max_players[j]] == max(points_hand):
                    print("Player", str(max_players[j] + 1) + " ties.")
                    points_hand[max_players[j]] = 0
                    j = 0
                elif len(max_players) == 1:
                    print("Player", str(max_players[j] + 1) + " ties.")
                    return
                else:
                    j += 1
        return

    # determine if a hand is a royal flush
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if rank_order:
            return 10 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank
        else:
            return 0

    def is_straight_flush(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return False

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and ((hand[i].rank + 1) == hand[i + 1].rank)

        if rank_order:
            return 9 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank
        else:
            return 0

    def is_four_kind(self, hand):
        count = 0
        for card in range(len(hand) - 1):
            if (hand[card].rank == hand[card + 1].rank):
                count += 1
                same_card = hand[card].rank
            else:
                different_card = hand[card].rank
        if (count == 4):
            return 8 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank
        else:
            return 0

    def is_full_house(self, hand):
        similar_cards_left = 0  # how many cards have similar rank from left
        similar_cards_right = 0  # how many cards have similar rank from the right
        leng = len(hand)
        for i in range(leng - 1):
            if hand[0].rank == hand[i].rank:
                similar_cards_left += 1
            else:
                continue
            if hand[leng - 1].rank == hand[leng - i - 1].rank:
                similar_cards_right += 1
            else:
                continue

        if (similar_cards_left + similar_cards_right == 5):
            return 7 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank
        else:
            return 0

    def is_flush(self, hand):
        for i in range(len(hand) - 1):
            if hand[i].suit != hand[i + 1].suit:
                return False
        return True

    def is_straight(self, hand):
        rank_order = True
        for i in range(len(hand) - 1):
            rank_order = rank_order and (hand[i].rank + 1 == hand[i + 1].rank)
        if rank_order:
            return 5 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank
        else:
            return 0

    def is_three_kind(self, hand):
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                if (i + 2 < len(hand) - 1) and (hand[i + 1].rank == hand[i + 2].rank):
                    return 3 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + \
                           hand[3].rank * 13 + hand[4].rank
            else:
                continue
        return 0

    def is_two_pair(self, hand):
        amount_ranks = []
        for i in range(len(hand)):
            if hand[i].rank not in amount_ranks:
                amount_ranks.append(hand[i].rank)
            else:
                continue
        if len(amount_ranks) != 3:
            return 0
        else:
            return 3 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank

    def is_one_pair(self, hand):
        amount_ranks = []
        for i in range(len(hand)):
            if hand[i].rank not in amount_ranks:
                amount_ranks.append(hand[i].rank)
            else:
                continue
        if len(amount_ranks) != 4:
            return 0
        else:
            return 2 * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                3].rank * 13 + hand[4].rank

    def is_high_card(self, hand):
        return 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[3].rank * 13 + \
               hand[4].rank


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
