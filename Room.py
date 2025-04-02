class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.computers = []
    
    def add_computer(self, computer):
        self.computers.append(computer)