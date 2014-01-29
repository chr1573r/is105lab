# -*- coding: latin-1 -*-

#
#  IS-105 LAB2
#
#  lab2.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': '-', \
			'student2': '-', \
            'student3': '-', \
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
def ascii_fugl():
	print """
	       \/_
	  \,   /( ,/
	   \\\' ///
	    \_ /_/
	    (./
	     '` 
	"""
	pass

# 
#  Oppgave 2
#    'return 2' - 2 skal erstattes med en korrekt returverdi, 2 er kun en stedsholder
#    bitAnd - x&y
#    Eksempel: bitAnd(6, 5) = 4
#
def bitAnd(x, y):
	return x&y # Returner resultat av x AND Y

# Denne oppgaven var lik oppg2?
# 
#  Oppgave 3  
#    bitAnd - x&y
#    Eksempel: bitAnd(6, 5) = 4
#
#def bitAnd(x, y):
#  return 2

#
#  Oppgave 4
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
	return x^y # Returner resultat av x XOR y

#
#  Oppgave 5
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
	return x^y # Returner resultat av x OR Y

#
#  Oppgave 6
#    ascii8Bin - ta et tegn som argument og returnerer ascii-verdien som 8 bits streng binært
#    Eksempel: ascii8('A) = 01000001
#
#  Tips:
#    For å finne desimalverdien til et tegn bruk funksjonen ord, for eksempel
#      ord('A) , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
def ascii8Bin(bokstav): # definere en funksjon som heter ascii8Bin, som tar i mot parameter "bokstav"
	
	binary = ord(bokstav) # setter en variabel som heter binary. Den inneholder resultatet av funksjonen ord(bokstav)

	return '{0:08b}'.format(binary) # returner resulat, tallet satt i "binary", skrevet binært

# 
#  Oppgave 7
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#
def transferBin(string): 
	l = list(string)
	for c in l:
		#if c != "None":
		print ascii8Bin(c)
	pass

#
#  Oppgave 8
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
# 
def ascii2Hex(bokstav): # støtte funksjon til transferHex
	
	hexy = ord(bokstav) # setter en variabel som heter hexy. Den inneholder resultatet av funksjonen ord(bokstav)

	return '{0:02x}'.format(hexy) # returner resulat, tallet satt i "hext", skrevet hexadesimalt	

def transferHex(string):
	l = list(string)
	for c in l:
		#if c != "None":
		print ascii2Hex(c)
	pass

# Selve runscriptet

print "\n\n# Oppgave 1"
print "\nascii_fugl() resultat:"
ascii_fugl()

print "\n\n# Oppgave 3"
print "\nbitXor(4, 5) resultat:"
print bitXor(4, 5)

print "\n\n# Oppgave 4"
print "\nbitOr(0, 1) resultat:"
print bitOr(0, 1)

print "\n\n# Oppgave 5"
print "\nbitAnd(6, 5) resultat:"
print bitAnd(6, 5)

print "\n\n# Oppgave 6"
print "\nasciiBin('A') resultat:"
print ascii8Bin("A")

print "\n\n# Oppgave 7"
print "\ntransferBin(\"Hei og hopp\") resultat:"
transferBin("Hei og hopp")

print "\n\n# Oppgave 8"
print "\nascii2Hex('A') resultat:"
print ascii2Hex('A')

print "\ntransferHex('Hei og hopp') resultat:"
transferHex('Hei og hopp')
