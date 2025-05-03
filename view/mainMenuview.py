from view.playerView import CreatePlayerView
from controller.playerManagement import playerManagement

controller = playerManagement()

def mainMenu():
    
    print("Welcome to the casino CodeVegas")
    print("Please select the option number: ")
    option = input("1. Register\n2. Login\n3. Exit\nYour choice: ")
    if option == "1":
        print("Registering...")
        CreatePlayerView()
        mainMenu()
    elif option == "2":
        print("Logging in...")
        player = controller.listPlayers()
        if player:
            print("Players registered:")
            for p in player:
                print(f"ID: {p['id']}, Name: {p['name']}, Balance: {p['balance']}")
                mainMenu()
        
    elif option == "3":
        print("Exiting...")
        exit()# Exit the program
    else:
        print("Invalid option. Please try again.")
        mainMenu()  # Restart the menu if the input is invalid
    