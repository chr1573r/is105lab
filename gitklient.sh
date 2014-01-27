#!/bin/bash
#
# gitklient.sh
#
# Kommandolinje klient for git(hub) - Christer Jonassen
# Forutsetter at repositoryet er satt opp sikkelig



Velg handling:

1. Commit alle endringer
   (git add * og git commit)

2. Synkroniser med github.com
   (git pull origin master og
   	git push origin master)


leggtilogcommit()
{
	echo "'Utfører git add *'"
	git add *

	echo "Utfører git commit"
	echo "Skriv inn kommentar til commiten du oppretter:"
	git commit -m "Kommentar"
}

synkronisermedgithub