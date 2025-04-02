class Transaction:
    def __init__(self, transaction_id, player_id, amount, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.player_id = player_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp
