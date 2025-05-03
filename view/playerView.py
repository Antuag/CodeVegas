from controller.playerManagement import playerManagement

def CreatePlayerView():
    """
    Function to create a player view.
    """
    createPlayer = playerManagement()
    id = int(input("Enter your ID for 5 numbers: "))
    if len(str(id)) != 5:
        print("The ID must be 5 numbers.")
        return
    name = input("Enter your name: ")
    if name == "":
        print("The name cannot be empty")
        return
    balance = int(input("Enter your balance: "))
    if balance <= 0:
        print("The balance must be greater than 0.")
        return
    player = createPlayer.createPlayer(id, name, balance)
    print(f"Player {player.name} registered successfully with ID {player.id} and balance {player.balance}.")

