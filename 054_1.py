from datetime import datetime
start = datetime.now()

def poker(hands):
    scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    # winner = sorted(scores)[-1][0]
    return hands[winner]

def score(hand):
    ranks = '23456789TJQKA'
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    if len(score) == 5:
        if ranks[0:2] == (12, 3): #adjust if 5 high straight
            ranks = (3, 2, 1, 0, -1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        '''no pair, straight, flush, or straight flush'''
        score = ([1, (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
    return score, ranks


vic1 = 0
data = open('p054_poker.txt', 'r').readlines()
for play in data:
	s = play.strip()
	h1 = s[:15]
	h2 = s[15:]
	print(f"{h1}\t\t\t{h2}")
	print(f"{score(h1.split())}\t\t\t{score(h2.split())}")
	# if h1 == poker([h1, h2]):
	# 	vic1 += 1
	# 	print("player one won")
	# # print(poker([h1, h2]))
	print()

print(F"total: {vic1}")


print(f"\n\n\nfin in {datetime.now()-start}")