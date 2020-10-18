from datetime import datetime
start = datetime.now()

# Poker Hand Analyser Library for Project Euler: Problem 54
from collections import namedtuple
# import pe_lib

def character_frequency(s):
	freq = {}
	for i in s:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	return freq

suits = "HDCS".split()
faces = "2,3,4,5,6,7,8,9,T,J,Q,K,A"
face = faces.split(',')

class Card(namedtuple('Card', 'face, suit')):
	def __repr__(self):
		return ''.join(self)

def royal_flush(hand):
	royalface = "TJQKA"
	# sort the cards based on the face rank of each card
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

	first_card = ordered[0]
	other_cards = ordered[1:]

	# check if all are of the same suit
	if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
		if ''.join(card.face for card in ordered) in royalface:
			return 'royal-flush', ordered[-1].face
	return False

def straight_flush(hand):
	# sort the cards based on the face rank of each card
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

	first_card = ordered[0]
	other_cards = ordered[1:]

	# check if all are of the same suit
	if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
		if ''.join(card.face for card in ordered) in ''.join(face):
			return 'straight-flush', ordered[-1].face
	return False

def four_of_a_kind(hand):
	allfaces = [f for f,s in hand]
	
	# create a unique set of ranks
	uniqueRanks = set(allfaces)

	# if there are more than 2 ranks, it's not four of a kind
	if len(uniqueRanks) != 2:
		return False

	for f in uniqueRanks:
		# if there are 4 faces, it is four of a kind
		if allfaces.count(f) == 4:
			uniqueRanks.remove(f)
			return "four-of-a-kind", f

	return False

def full_house(hand):
	allfaces = [f for f,s in hand]

	rankFrequency = character_frequency(allfaces)

	# if there are 2 types of ranks and there's a card with 1 pair and 3 of a kind
	if len(rankFrequency) == 2 and (rankFrequency.values()[0] == 2 and rankFrequency.values()[1] == 3):
		return 'full-house'

	return False

def flush(hand):
	allfaces = [f for f,s in hand]

	first_card = hand[0]
	other_cards = hand[1:]

	if all(first_card.suit == card.suit for card in other_cards):
		return 'flush', sorted(allfaces, key=lambda f: face.index(f), reverse=True)

	return False

def straight(hand):
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))
	if ''.join(card.face for card in ordered) in ''.join(face):
		return 'straight', ordered[-1].face
	return False;

def three_of_a_kind(hand):
	allfaces = [f for f,s in hand]

	uniqueRanks = set(allfaces)

	if len(uniqueRanks) != 3:
		return False

	for f in uniqueRanks:
		if allfaces.count(f) == 3:
			uniqueRanks.remove(f)
			return "three-of-a-kind", f

	return False;

def two_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	
	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]
	
	# if there are more than two pairs
	if len(pairs) != 2:
		return False

	p1, p2 = pairs
	# get the difference using sets
	other_cards = [(allftypes - set(pairs)).pop()]
	return 'two-pair', pairs + other_cards if(face.index(p1) > face.index(p2)) else pairs[::-1] + other_cards

def one_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)

	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]

	# if there's more than one pair
	if len(pairs) != 1:
		return False

	allftypes.remove(pairs[0])
	return 'one-pair', pairs + sorted(allftypes, key=lambda f: face.index(f), reverse=True)

def high_card(hand):
	# collect all faces from each card
	allfaces = [f for f,s in hand]

	#sort the faces and show the highest card
	return "high_card", sorted(allfaces, key=lambda f: allfaces.index(f), reverse=True)[0] 

def create_hand_tuple(cards = "5D 8C 9S JS AC"):
	hand = []

	for card in cards.split():
		face, suit = card[:-1], card[-1]
		hand.append(Card(face, suit))

	return hand;

# functions
handrankorder = (royal_flush,straight_flush,four_of_a_kind,full_house,
				flush,straight,three_of_a_kind,two_pair,
				one_pair,high_card)

def determine_rank(cards):
	hand = create_hand_tuple(cards)
	for ranker in handrankorder:
		rank = ranker(hand)

		if rank:
			break
	return rank


for play in open('p054_poker.txt', 'r').readlines():
	play = play.strip()
	h1 = play[:15]
	h2 = play[15:]
	print(f"{determine_rank(h1)}\t\t{determine_rank(h2)}")

print(f"\n\n\nfin in {datetime.now()-start}")
