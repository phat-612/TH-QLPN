class Employee:
    def __init__(self, user_id, name, username, password, address, phone):
        super().__init__(user_id, name, username, password)
        self.address = address
        self.phone = phone