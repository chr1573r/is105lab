# -*- coding: latin-1 -*-

"""
Poker klient utvikles her
Dette eksemplet gir mulighet til å sende flere kommandoer gjennom socketen
Man kan avslutte forbindelse med å sende en tom linje
"""

import socket
import sys


host = 'localhost'
port = 10000
size = 1024
myhandgfx = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
sys.stdout.write('>')

while 1:
    # lese fra tastaturet (må finne på kommandoer)
	# kan droppe feilsjekking i denne versjonen
    line = sys.stdin.readline()
    if line == '\n':
        break
    elif line == "JOIN":
        parse = yes

    s.send(line)
	
    data = s.recv(size)
    datasplit = data.split(",")

    if datasplit[0] == "211": #HAND OK
        
        del datasplit[0]
        for card in datasplit:
            value = card[0]
            suit = card[1]
            
            if suit == "H":
                suit = u'\u2764'
                
            elif suit == "S":
                suit = u'\u2660'

            elif suit == "D":
                suit = u'\u2666'

            elif suit == "C":
                suit = u'\u2663'
            print "|{}{}| ".format(value, suit.encode('utf-8')),
        print "\n"

    elif datasplit[0] == "221": #SHOWDOWN OK
        print "Winner:"
        result = datasplit[1]
        del datasplit[1]
        del datasplit[0]
        for card in datasplit:
            value = card[0]
            suit = card[1]
            
            if suit == "H":
                suit = u'\u2764'
                
            elif suit == "S":
                suit = u'\u2660'

            elif suit == "D":
                suit = u'\u2666'

            elif suit == "C":
                suit = u'\u2663'
            print "|{}{}| ".format(value, suit.encode('utf-8')),
        print "({})".format(result)
        print "\n"

    else:
        print data
    sys.stdout.write('> ')
s.close()
