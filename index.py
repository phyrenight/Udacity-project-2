import tournament

def menu():
    """
        menu system for swiss pair tournament
    """
    choice = ""
    while choice != 'q':
        print "What would you like to do: "
        print "1) add a player"
        print "2) start tournament"
        print "3) view  current players"
        print "4) reset database"
        print "q) Enter q to quit"
        choice = raw_input("> ")
        if choice == '1':
            print "Enter a player's name:"
            name = raw_input("> ") # make a check to ensure that a name is inputted
            tournament.registerPlayer(name)
        elif choice == '2':
            numberOfPlayers = tournament.countPlayers()
            if numberOfPlayers < 6:
                print "Insufficient number of players. Tournament can not be started."
            else:
            	choice = 'q'
                startTournamentMenu()
        elif choice == '3':
        	players = tournament.playerStandings()
        	for i in players:  # try turning these two lines into a list comprehension
        	    print i        # 2
        elif choice == '4':
            print " Are you sure you want to erase the database:(y/n)"
            answer = raw_input("> ")
            if answer == 'y':
            	tournament.deleteMatches()
            	tournament.deletePlayers()
            elif answer == 'n':
            	print "Deletion of database cancelled"
            else:
            	print "Invalid input {}.".format(answer)
        elif choice == 'q':
            print "Exiting now...."
        else:
            print "Invalid entry"


def displayStandings():
    """
        tournament standings are print to the screen
    """
    results =  tournament.playerStandings()
    print "Current standings are: "
    for i in results:
        print "id:{} name: {} wins: {} loses: {} ".format(i[0], i[1], i[2], i[3])

def updateMatches():
    """
        Used to to get wins/loses of the players. 
    """
    displayCurrentMatches()
    print "Please enter the winners id "
    winner = int(raw_input("> ")) # add test make sure id is in tournament
    print "Print enter the losers id "
    loser = int(raw_input("> ")) #1 add test to make sure id is assigned to a player
    #2 try removing the loser input and have a search that retrieves the loser's id
    # and inputs that id into reportMatch() as loser.
    #add a feature that has the user verify that the right id's are being updated.
    tournament.reportMatch(winner,loser)
    displayCurrentMatches()


def displayCurrentMatches():
    """
       Displays the current matches taking place this round.
    """
    for i in tournament.swissPairings():
        print "match: {}({}) vs {}({})".format(i[1], i[0], i[3], i[2])


def startTournamentMenu():
    """
        menu to update each match. To view the standings and the match line ups
    """
    numberOfPlayers = tournament.countPlayers()
    totalMatches = numberOfPlayers * (numberOfPlayers-1)
    print numberOfPlayers, totalMatches
    choice = ""
    while choice != 'q':
        print "How would you like to proceed:"
        print "1) Display current matches"
        print "2) Display player's current standings"
        print "3) Update current matches"
        print "q) quit"
        choice = raw_input("> ")
        if choice == 1:
            displayCurrentMatches()
        elif choice == 2:
            displayStandings()
        elif choice == 3:
            updateMatches()
        elif choice == 'q':
            print "Exiting now"
        else:
            print "{} is an invalid choice, please try again".format(choice)


if __name__ == "__main__":
    displayStandings()
    tournament.connect()
    #updateMatches()
    displayCurrentMatches()
    menu()