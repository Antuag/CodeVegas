class Player:
    def __init__(self, id, name, balance):
        self.name = name
        self.id = id
        self.balance = balance
        
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Balance: {self.balance}"