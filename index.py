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
            name = raw_input("> ")
            tournament.registerPlayer(name)
        elif choice == '2':
            numberOfPlayers = tournament.countPlayers()
            if numberOfPlayers < 6:
                print "Insufficient number of players. Tournament can not be started."
            else:
            	choice = 'q'
                #tournamentPlay()
                #the processes in this else are just for testing
                pairs = []
                pairs = tournament.swissPairings()
                print "Current matches are:"
                for i in pairs:
                    print i
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






if __name__ == "__main__":
    tournament.connect()
    menu()