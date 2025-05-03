import json
from model.players import Player 

class playerManagement:
    
    def createPlayer(self, id, name, balance):
        
        # Create an instance of the Player class
        player = Player(id, name, balance)

        # Create a dictionary to store player data
        playerData = {
            "id": player.id,
            "name": player.name,
            "balance": player.balance
        }

        # Abrir el archivo JSON en modo de escritura
        with open('data/users.json', mode='r+') as jsonFile:
            # Leer el contenido existente si el archivo no está vacío
            try:
                jsonFile.seek(0)
                content = json.load(jsonFile)
            except json.JSONDecodeError:
                content = []

            # Agregar el nuevo jugador al contenido
            content.append(playerData)

            # Sobrescribir el archivo con los datos actualizados
            jsonFile.seek(0)
            json.dump(content, jsonFile, indent=4)
            
        return player
    
    def getPlayer(self, id):
        # Open the JSON file in read mode
        with open('data/users.json', mode='r') as jsonFile:
            # Load the content of the file into a variable
            players = json.load(jsonFile)
            for player in players:
                if player['id'] == id:
                    return Player(player['id'], player['name'], player['balance'])
        
        return None
    
    def listPlayers(self):
        """
        Leer y listar todos los jugadores del archivo JSON.
        """
        try:
            with open('data/users.json', mode='r') as jsonFile:
                players = json.load(jsonFile)
                if not players:
                    print("No players found.")
                else:
                    print("List of registered players:")
                    for player in players:
                        print(f"ID: {player['id']}, Name: {player['name']}, Balance: {player['balance']}")
        except FileNotFoundError:
            print("The file 'users.json' does not exist.")
        except json.JSONDecodeError:
            print("The file 'users.json' is empty or corrupted.")      