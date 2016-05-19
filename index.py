import tournament


def menu():
    """
        menu system for swiss pair tournament
    """
    choice = ""
    while choice != 'quit':
        print "What would you like to do: "
        print "1) add a player"
        print "2) start tournament"
        print "3) view  current players"
        print "4) reset database"
        print "Enter quit to exit"
        choice = raw_input("> ")
        if choice == '1':
            print "Enter a player's name:"
            name = raw_input("> ")
            if name != "" or name != " ":
                tournament.registerPlayer(name)
            else:
                print "Invalid name"
        elif choice == '2':
            numberOfPlayers = tournament.countPlayers()
            if numberOfPlayers < 6:
                print "Insufficient number of players. Tournament can \
                       not be started."
            else:
                print "Do you wish to start the tournament?"
                print "You will not be able to add anymore players if you do."
                print "Enter yes to continue and no to cancel."
                start = raw_input("> ")
                if start == 'yes':
                    choice = 'quit'
                    startTournamentMenu()
                else:
                    print "start of tournament cancelled"
        elif choice == '3':
            players = tournament.playerStandings()
            for i in players:
                print "player's name: {} id: {}".format(i[1], i[0])
        elif choice == '4':
            print " Are you sure you want to erase the database:(yes/no)"
            answer = raw_input("> ")
            if answer == 'yes':
                tournament.deleteMatches()
                tournament.deletePlayers()
            elif answer == 'no':
                print "Deletion of database cancelled"
            else:
                print "Invalid input {}.".format(answer)
        elif choice == 'quit':
            print "Exiting now...."
        else:
            print "Invalid entry"


def displayStandings():
    """
        tournament standings are print to the screen
    """
    results = tournament.playerStandings()
    print "Current standings are: "
    for i in results:
        print "id:{} name: {} wins: {} loses:\
         {} ".format(i[0], i[1], i[2], i[3])


def updateMatches(currentLineUp):
    """
        Used to to get wins/loses of the players.
    """
    displayCurrentMatches(currentLineUp)
    print "Please enter the winners id "
    winner = int(raw_input("> "))  # add test make sure id is in tournament
    print "Print enter the losers id "
    loser = int(raw_input("> "))  # 1 add test to make sure id is
    # assigned to a player
    # 2 try removing the loser input and have a search that retrieves the
    # loser's id
    # and inputs that id into reportMatch() as loser.
    # add a feature that has the user verify that the right id's
    # are being updated.
    tournament.reportMatch(winner, loser)
    MatchesPlayedThisRound += 1
    displayCurrentMatches(currentLineUp)


def displayCurrentMatches(currentLineUp):
    """
       Displays the current matches taking place this round.
    """
    for i in currentLineUp:
        print "match: {}({}) vs {}({})".format(i[1], i[0], i[3], i[2])


def startTournamentMenu():
    """
        menu to update each match. To view the standings and the match line ups
    """

    currentLineUp = tournament.swissPairings()
    numberOfPlayers = tournament.countPlayers()
    totalMatchesPlayed = 0
    matchesPlayedThisRound = 0
    totalMatches = numberOfPlayers * (numberOfPlayers-1)
    print numberOfPlayers, totalMatches
    choice = ""
    while choice != 'quit':
        if matchesPlayedThisRound == numberOfPlayers/2:
            # checks to see if all the matches were played for the round
            currentLineUp = tournament.swissPairings()
            matchesPlayedThisRound = 0
            displayCurrentMatches()
        print "How would you like to proceed:"
        print "1) Display current matches"
        print "2) Display player's current standings"
        print "3) Update current matches"
        print "Enter quit to exit"
        if totalMatchesPlayed == totalMatches:
            player = getTopThree()
            print "tournament has ended"
            print "1st place winner is: {}".format(player.next())
            print "2nd place winner is: {}".format(player.next())
            print "3rd place winner is: {}".format(player.next())
            choice = 'quit'
        else:
            choice = raw_input("> ")
        if choice == '1':
            displayCurrentMatches(currentLineUp)
        elif choice == '2':
            displayStandings()
        elif choice == '3':
            updateMatches(currentLineUp)
        elif choice == 'quit':
            print "Exiting now"
        else:
            print "{} is an invalid choice, please try again".format(choice)


def getTopThree():
    """
        returns the top three players one at a time
    """
    for i in tournament.playerStandings():
        yield i[1]


if __name__ == "__main__":
    displayStandings()
    tournament.connect()
    # updateMatches()
    displayCurrentMatches(tournament.playerStandings())
    menu()
