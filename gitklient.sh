#!/bin/bash

# gitklient.sh
# Kommandolinje klient for git(hub) - Christer Jonassen
# 
# Forutsetter at current directory er et repository og at det er riktig satt opp.


trap "{ echo \"Fanget stopp signal, avslutter...\"; sleep 1;  exit; }" SIGINT SIGTERM # Set trap for catching Ctrl-C and kills, so we can reset terminal upon exit
trap "{ clear; echo \"gitklient terminated at `date`\"; }" EXIT # exit procedure


bekreft()
{
	echo "Trykk en tast for å fortsette..."
	read -n 1 SELECTION
}

leggtilogcommit()
{
	echo "'Utfører git add *'"
	git add *

	echo "Skriv inn kommentar til commiten du oppretter:"
	read KOMMENTAR

	echo "Vil bli commitet med kommentaren: $KOMMENTAR"
	bekreft
	echo "Utfører git commit!"
	git commit -m "$KOMMENTAR"
}

synkronisermedgithub()
{
	echo "Laster ned..."
	echo "(git pull origin master)"
	sleep 1
	git pull origin master
	echo "Laster opp..."
	echo "(git push origin master)"
	sleep 1
	git push origin master
}

meny()
{
clear
echo "$SELECTION"
echo "Velg handling:"
echo    
echo "1. Commit alle endringer"
echo "   (git add * og git commit)"
echo    
echo "2. Synkroniser med github.com"
echo "   (git pull origin master og"
echo "       git push origin master)"
echo   
echo "X. Avslutt"
echo
echo
echo "Velg en handling (1, 2 eller X):"

read -n 1 SELECTION

case "$SELECTION" in
 	1)
		leggtilogcommit
		;;

	2)
		synkronisermedgithub
		;;

	x)
		exit
		;;

	X)
		exit
		;;

	*)
		;;
esac
}

# selve runscriptet
while true
        do
        	meny
        done
