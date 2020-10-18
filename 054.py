from datetime import datetime
start = datetime.now()



from collections import namedtuple
 
class Card(namedtuple('Card', 'face, suit')):
	def __repr__(self):
		return ''.join(self)
 
 
# suit = '♥ ♦ ♣ ♠'.split()
suit = 'H D C S'
# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 T j q k a'.upper()
lowaces = 'a 2 3 4 5 6 7 8 9 T j q k'.upper()
# faces as lists
face   = faces.split()
lowace = lowaces.split()
 
 
def straightflush(hand):
	f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
			 else (face, faces) )
	ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
	first, rest = ordered[0], ordered[1:]
	if ( all(card.suit == first.suit for card in rest) and
		 ' '.join(card.face for card in ordered) in fs ):
		return '9', ordered[-1].face
	return False
 
def fourofakind(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	if len(allftypes) != 2:
		return False
	for f in allftypes:
		if allfaces.count(f) == 4:
			allftypes.remove(f)
			return '8', [f, allftypes.pop()]
	else:
		return False
 
def fullhouse(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	if len(allftypes) != 2:
		return False
	for f in allftypes:
		if allfaces.count(f) == 3:
			allftypes.remove(f)
			return '7', [f, allftypes.pop()]
	else:
		return False
 
def flush(hand):
	allstypes = {s for f, s in hand}
	if len(allstypes) == 1:
		allfaces = [f for f,s in hand]
		return '6', sorted(allfaces,
							   key=lambda f: face.index(f),
							   reverse=True)
	return False
 
def straight(hand):
	f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
			 else (face, faces) )
	ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
	first, rest = ordered[0], ordered[1:]
	if ' '.join(card.face for card in ordered) in fs:
		return '5', ordered[-1].face
	return False
 
def threeofakind(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	if len(allftypes) <= 2:
		return False
	for f in allftypes:
		if allfaces.count(f) == 3:
			allftypes.remove(f)
			return ('4', [f] +
					 sorted(allftypes,
							key=lambda f: face.index(f),
							reverse=True))
	else:
		return False
 
def twopair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	pairs = [f for f in allftypes if allfaces.count(f) == 2]
	if len(pairs) != 2:
		return False
	p0, p1 = pairs
	other = [(allftypes - set(pairs)).pop()]
	return '3', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other
 
def onepair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	pairs = [f for f in allftypes if allfaces.count(f) == 2]
	if len(pairs) != 1:
		return False
	allftypes.remove(pairs[0])
	return '2', pairs + sorted(allftypes,
									  key=lambda f: face.index(f),
									  reverse=True)
 
def highcard(hand):
	allfaces = [f for f,s in hand]
	return '1', sorted(allfaces,
							   key=lambda f: face.index(f),
							   reverse=True)
 
handrankorder =  (straightflush, fourofakind, fullhouse,
				  flush, straight, threeofakind,
				  twopair, onepair, highcard)


def rank(cards):
	hand = handy(cards)
	for ranker in handrankorder:
		rank = ranker(hand)
		if rank:
			break
	assert rank, "Invalid: Failed to rank cards: %r" % cards
	return rank
 
def handy(cards='2H 2B 2♣ k♣ q♦'):
	hand = []
	for card in cards.split():
		f, s = card[:-1], card[-1]
		assert f in face, "Invalid: Don't understand card face %r" % f
		assert s in suit, "Invalid: Don't understand card suit %r" % s
		hand.append(Card(f, s))
	assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
	assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
	return hand


vic1 = 0
with open('p054_poker.txt', 'r') as f:
	l = f.readline().strip()
	h1 = l[:15]
	h2 = l[15:]
	if rank(h1) > rank(h2):
		print(f"victory for p1")
		vic1 += 1

print(F"total: {vic1}")

print(f"\n\n\nfin in {datetime.now()-start}")