class Player:
    def __init__(self, user_id, name, username, password, balance):
        super().__init__(user_id, name, username, password)
        self.balance = balance
    
    def add_balance(self, amount):
        self.balance += amount
    
    def deduct_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False