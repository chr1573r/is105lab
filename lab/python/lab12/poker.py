# -*- coding: latin-1 -*-

#
#  IS-105 LAB11
#  Implementer alt som er markert med OPPGAVE.
#  I tillegg skal du i filen lab11defs.txt beskrive et program (så detaljert du kan)
#	for en poker server, hvor spillere kan melde seg på et poker spill, 
#	få utdelt en hånd hver, legge inn en sats eller kaste sin hånd 
#	og få utpekt en (eller flere i tilfelle uavgjort) vinner.
#	Det er lagt ut flere implementasjoner av sockets klient-tjener modell i Class Fronter.
#	Det som er aktuelt å se på er de som er implementert i Python.
#
#  lab11.py - kildekode som inneholder studentenes løsning.
#
#
#
import random # brukes for å dele ut kort

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Christer Jonassen', \
			'student2': 'Christoffer Lien', \
			'student3': 'Pål Sandnes', \
}

# Oppgave 
# 	Implementere pokerspill. Vi begynner med representasjon og testing.
#
#	Testing i Python kan gjøres med assert. Eksemplet under skal være selvforklarende.
#
#   Det er gitt et kortstokk http://en.wikipedia.org/wiki/Playing_card med 52 kort.
#	I denne oppgaven prøver vi å lage et prototype som gir svar på følgende:
#	Hvordan representere alle kort? Hvordan finne ut hvilken hånd er best? Hvordan dele ut kort?
#
#   Les deg opp på hva poker er og hvordan det spilles, hvis du ikke kjenner til det fra før.
#	Domenkunnskap i systemutvikling er viktigst!!!
#	http://no.wikipedia.org/wiki/Poker
#	http://en.wikipedia.org/wiki/Poker
#
#	Her er et forslag for representasjon av kort og hender, som jeg anbefaler dere å bruke.
#	Dere kan gjøre egne modifikasjoner, med de må være begrunnet i lab11defs.txt filen.
#
#   Typer (kind): H - heart, S - spade, C - club, D - diamond (13 kort av hver type)
#   Verdi (rank): A - ace, K - king, Q - queen, J - jack, T - ten, 9, 8, 7, 6, 5, 4, 3, 2
#   En hånd (hand): består av 5 kort http://en.wikipedia.org/wiki/Hand_rankings
#   Hånd rangeres fra høyest til lavest (i paranteser anbefalt navn på variabelen på en hånd): 
#		 8 - Straight flush (sf) (finnes også Royal Flush, som er den beste av Straight flush)
#		 7 - Four of a Kind (fk) 
#		 6 - Full House (fh) 
#	     5 - Flush (fl)
#		 4 - Straight (st) 
#		 3 - Three of a kind (tk) 
#	     2 - Two Pair (tp) 
#        1 - One Pair (op) 
#        0 - High Card (hc)
#   
#
# OPPGAVE: erstatt max med en funksjon allmax, som tar hensyn til uavgjort mellom to eller flere hender 
def pokerdebug(hands):
	"""
		Denne funksjonene må omdefineres for å ta hensyn til spesialtilfelle med flere like "Straight Flush" hender
		dvs. uavgjort
		Returnerer en eller flere hender: poker([hand, ...]) => [[hand], ...]
		hand_rank er en funksjon som må skrives og brukes i sammenligningen av "hender"
	"""
	print "##### POKER DEBUG START"
	global score

	print  "{}:{}> {}".format("DEBUG", "POKERDEBUG-hands", hands)

	for hand in hands:
		score = hand_rank(hand)
		print "{} \"{}\" - {}".format("### HAND RANK: IDENTIFIED", description, score )

	print "##### POKER DEBUG STOP"
	print "\n"
	return score


def poker(hands, mode):
		if mode == "winner":
			winner = allmax(hands, key=hand_rank)
			return winner
		elif mode == "score":
			allmax(hands, key=hand_rank)
			return description
	

def allmax(iterable, key=None):
    #Returnerer en liste over alle enheter som er like ift max verdi av iterable
    #print "{} {} ({})".format("### HAND RANK: IDENTIFIED", score[0], description)
    print  "{}:{}> {}".format("DEBUG", "ALLMAX", "START")
    iterable.sort(key=key,reverse=True) 
    result = iterable[0]
    maxValue = key(iterable[0]) if key else iterable[0]
    print  "{}:{}> {}".format("DEBUG", "ALLMAX", "STOP")
    for value in iterable[1:]:
        v = key(value) if key else value
        if v == maxValue: result.append(value)
        else: break
    return result

# OPPGAVE: fullføre denne funksjonene for alle hender i poker og lage tester med assert
def hand_rank(hand):
	"""
		Returnerer en verdi som indikerer verdi av en hånd. 
		Vi har gitt verdien til hendene i spesifikasjonen (8 Straight Flush, ...)
		Vi må også kunne skille mellom "like" hender (breaking ties).
		9 9 9 9 5 => (7,9,5) Four of Kind (7) and five kicker
		3 3 3 3 2 => (7,3,2) Four of Kind (7) and two kicker
		TD 8D 7D 5D 3D => (5, [10,8,7,5,3]) Flush (5) men alle kort må spesifiseres for å kunne sammenligne
		JC TC 9C 8C 7C => (8, 11) Straight Flush (8) Jack (11) High
		AS AH AC AD QH => (7, 14, 12) Four Aces (7, 14)  and a Queen kicker (12)
	"""
	print "\r"
	print "### HAND RANK START"
	#print  "{}:{}> {}".format("DEBUG", "HAND_RANK-hand", hand)
	ranks = card_ranks(hand)
	#print  "{}:{}> {}".format("DEBUG", "HAND_RANK-ranks", ranks)

#		 8 - Straight flush (sf) (finnes også Royal Flush, som er den beste av Straight flush)
#		 7 - Four of a Kind (fk) 
#		 6 - Full House (fh) 
#	     5 - Flush (fl)
#		 4 - Straight (st) 
#		 3 - Three of a kind (tk) 
#	     2 - Two Pair (tp) 
#        1 - One Pair (op) 
#        0 - High Card (hc)
	global description

	# TEST 8: Straight flush
	if straight(ranks) and flush(hand):
		description = "Straight-Flush"
		print description
		return (8, max(ranks)) # 2 3 4 5 6 => (8, 6)


	# TEST 7: 4 of a kind
	elif kind(4, ranks): # kan returnere både boolean og tall, i Java 0 er False
		retvalue = (7, kind(4, ranks), kind(1, ranks))
		description = "4 of a kind"
		print description
		return retvalue# 9 9 9 9 3 (7, 9, 3)

	# TEST 6: Full house
	elif kind(3, ranks) and kind(2, ranks): # kan returnere både boolean og tall, i Java 0 er False
		description = "Full House"
		print description
		return (6, kind(3, ranks), kind(2, ranks)) # 9 9 9 9 3 (7, 9, 3)

	# TEST 5: Flush
	elif flush(hand):
		description = "Flush"
		print description
		return (5, max(ranks)) # 2 3 4 5 6 => (8, 6)

	# TEST 4: Straight
	elif straight(ranks):
		description = "Straight"
		print description
		return (4, max(ranks)) # 2 3 4 5 6 => (8, 6)

	# TEST 3: 3 of a kind
	elif kind(3, ranks): # kan returnere både boolean og tall, i Java 0 er False
		description = "3 of a kind"
		print description
		return (3, kind(3, ranks), ranks) # 9 9 9 9 3 (7, 9, 3)

	# TEST 2: Two pair
	elif two_pair(ranks):
		description = "Two pair"
		print description
		#print (2, two_pair(ranks), ranks)
		return (2, two_pair(ranks), kind(1, ranks)) # 2 3 4 5 6 => (8, 6)

	# TEST 1: One pair
	elif one_pair(ranks):
		description = "One pair"
		print description
		return (1, max(ranks), ranks) # 2 3 4 5 6 => (8, 6)

	# TEST 0: High Card
	print  "{}:{}> {}".format("DEBUG", "HIGH-CARD-RETURN", (0, max(ranks)))
	description = "High card"
	print description
	return (0, max(ranks), ranks)
	
# Funksjonene card_ranks(hand) returnerer en ORDNET (sorted) tuple av verdier (ranks)
# Verdier for J, Q, K og A er tilsvarende 11, 12, 13, 14. 
# En hånd TD TC TH 7C 7D skal returnere [10,10,10,7,7]
def card_ranks(hand):

	# Denne funksjonen ble implementert i LAB 5. Bruk implementasjonen her
	#print  "{}:{}> {}".format("DEBUG", "CARD_RANK-hand", hand)
	#Returner en hånd som bare inneholder tallverdier i tuple format
	#proglangs_sortert=sorted(proglangs, key=lambda proglangs_sortert: proglangs_sortert[1])
	card_rank=(value_translate(hand[0][0]), value_translate(hand[1][0]), value_translate(hand[2][0]), value_translate(hand[3][0]), value_translate(hand[4][0]))
	#print "{} (unsorted,{})".format(card_rank,type(card_rank))
	card_rank_sorted=sorted(card_rank, key=lambda card_rank_sorted: card_rank_sorted, reverse=True)
	#print "{} (sorted,{})".format(card_rank_sorted,type(card_rank_sorted))
	print  "{}:{}> {}".format("DEBUG", "CARD_RANK-RETURN", card_rank_sorted)
	return card_rank_sorted

# Hjelpefunksjon for card_ranks
# Tolker om A, K, Q, J og T om til tallverdier.
# Oversetter alltid value til int.
def value_translate(value):

	if value == "A":
		value = 14
	elif value == "K":
		value = 13
	elif value == "Q":
		value = 12
	elif value == "J":
		value = 11
	elif value == "T":
		value = 10

	return int(value)

def card_rank2(hand):
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
	ranks.sort(reverse=True)
	return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

# OPPGAVE: Implementer denne funksjonen
# Funksjonen straight(ranks) returner True hvis hånden er en Straight.


def straight(ranks):
	print  "{}:{}> {}".format("DEBUG", "STRAIGHT-RETURN", (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5)
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

# OPPGAVE: Implementere denne funksjonen
# Funksjonen flush(hand) returnerer True hvis hånden er en Flush.
def flush(hand):
	types = [t for v,t in hand]
	print  "{}:{}> {}".format("DEBUG", "FLUSH-RETURN", len(set(types)) == 1)
	return len(set(types)) == 1

# OPPGAVE: Implementer denne funksjonen
# Funksjonen kind(nr, ranks) returnerer den første verdien (rank) som hånden har nøyaktig n av.
# For en hånd med 4 syvere, skal denne funksjonen returnere 7.

def kind(n, ranks):
	for r in ranks:
		if ranks.count(r) == n:
			#print r
			#print n
			print  "{}:{}> {} of a kind, {}'s".format("DEBUG", "KIND-RETURN", n, r, )
			return r
		
	print  "{}:{}> {} of a kind".format("DEBUG", "KIND-RETURN-FALSE", n )
	return None

# OPPGAVE: Implementer denne funksjonen
# Funksjonen two_pair(ranks) gjør følgende:
# hvis det er Two Pair, skal funksjonen returnere deres verdi (rank) som en tuple.
# For eksempel, en hånd med to toere og 2 firere vil gi en returverdi på (4, 2).

def two_pair(ranks):
    
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def one_pair(ranks):
	
	pair = kind(2, ranks)
	print  "{}:{}> {}".format("DEBUG", "ONE_PAIR-RETURN", pair)
	return pair

# OPPGAVE: Implementer denne funksjonen (brukes i poker funksjonen for å løse uavgjort tilfeller)
# For eksempel, gitt 4 følgende hender
#   [['6C', '7C', '8C', '9C', 'TC'],
#   ['6D', '7D', '8D', '9D', 'TD'],
#   ['9D', '9H', '9S', '9C', '7D'],
#   ['TD', 'TC', 'TH', '7C', '7D']]
# skal allmax returnere to hender [['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD']]
#def allmax(iterable, key=None):
#	return None

# Denne strukturen definerer et kortstokk for poker
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

# Denne funksjonen deler ut numhands med n kort i hver hånd
def deal(numhands, n=5, deck=mydeck):
    # Your code here.
	#print deck
	random.shuffle(deck)
	#print deck
	print "DEBUG:HANDS: {}".format([deck[n*i:n*(i+1)] for i in range(numhands)])
	return [deck[n*i:n*(i+1)] for i in range(numhands)]




def test():
   
	# Dette ble gjort i LAB 5
	# Den innebygde (built-in) funksjonen max kan brukes for å finne den beste hånden
	# Skriv test for den innebygde funksjonen max på flere "list of numbers" (lon)
	# Eksemplene er gitt, du må kommentere disse ut og sette på en verdi som ikke gir feil
	lon1 = [6, 7, 8, 0]
	lon2 = [6, 7, -9, 0]
	assert max(lon1) == 8
	assert max(lon2, key=abs) == -9

	sf = "6C 7C 8C 9C TC".split() # Straight Flush => ['6C', '7C', '8C', '9C', 'TC']
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	assert poker([sf, fk, fh]) == sf
	# Disse testtilfellene ble skrevet i LAB 5
	# Skriv tre nye testtilfeller som sammenligner hender basert på eksemplet overfor
	# 1) Four of Kind (fk) mot Full House (fh) skal returnere Four of Kind (fk)
	# 2) Full House (fh) mot Full House (fh) skal returnere Full House (fh)
	# 3) Straight (st) skal slå Two pair (tp) OBS! Du må selv lage eksempler på hender her
	

	
	# Dette ble gjort i LAB 5
	# 1) teste et tilfelle der det kun er en hånd og at poker returnerer den samme hånden
	# 2) teste et tilfelle hvor man sammenligner en Straight Flush med 100 Full Houses
	# og det må da returnere Straight Flush (urealistisk med så mange spillere, men 
	# vi tar høyde for det).
	# Hva skjer hvis man har en tom liste som inn-data, dvs. ingen hender?
	assert poker([sf]) == sf
	assert poker([sf, 100*fh]) == sf

	# Dette ble gjort i LAB 5
	# Implementer funksjonen card_rank(hand) og legg til tester for 
	# sf, fk og fh variabler som er definert i denne testfunksjonen
	# Du kan gjerne definere flere hender og legge til flere tester :)
	#print card_ranks(sf)
	assert card_ranks(sf) == (10,9,8,7,6)
	assert card_ranks(fk) == (9,9,9,9,7)

def test2():
	# 
	# hand_rank(..) implementere i denne laben (LAB 11)
	# Her er gitt noen eksempler på testing av denne funksjonen som man kan bruke på et senere tidspunkt
	#
	# 8 straight-flush 
	assert pokerdebug([['AC', 'KC', 'TC', 'QC', 'JC']]) == (8, 14) 
	
	# 7 four of a kind 
	assert pokerdebug([['AC', 'AD', 'AH', 'AS', 'JC']]) == (7, 14, 11)
	
	# 6 full house 
	assert pokerdebug([['AC', 'AD', 'AH', 'QC', 'QD']]) == (6, 14, 12)
	
	# 5 flush 
	assert pokerdebug([['AC', '5C', 'TC', 'QC', 'JC']]) == (5, 14)
	
	# 4 straight 
	assert pokerdebug([['AC', 'KH', 'TS', 'QC', 'JC']]) == (4, 14)
	
	# 3 three of a kind 
	assert pokerdebug([['AC', 'AH', 'AS', 'QC', 'JC']]) == (3, 14, [14, 14, 14, 12, 11])
	
	# 2 two pair 
	assert pokerdebug([['AC', 'AH', 'TS', 'TC', 'JC']]) == (2, (14, 10), 11)
	
	# 1 one pair 
	assert pokerdebug([['KC', 'KH', 'TS', '2C', '1C']]) == (1, 13, [13, 13, 10, 2, 1])


	return "Done testing"

#print "Winner: {}".format(poker(deal(5)))
#test2()