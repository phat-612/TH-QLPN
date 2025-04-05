import json
import bcrypt
from Player import Player
from Employee import Employee
import os
class Admin:
    def __init__(self, ):
        self.username = None
        self.password = None
        self.player = Player()

        pass
    def add(self, username, password):
        """Lưu thông tin admin vào file admin.json."""
        hash_password = self.hash_password(password)
        admin_data = {
            "admin": {
                "username": username,
                "password": hash_password  # Mã hóa mật khẩu
            }
        }
        with open("database/admin.json", "w", encoding="utf-8") as file:
            json.dump(admin_data, file, ensure_ascii=False, indent=4)
    def login(self, username, password):
        """Kiểm tra thông tin đăng nhập admin."""
        admin_data = self.load_from_file()
        if admin_data["admin"]:
            stored_username = admin_data["admin"]["username"]
            stored_hashed_password = admin_data["admin"]["password"]
            if username == stored_username and self.verify_password(password, stored_hashed_password):
                self.username = username
                return True
        return False
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()  # Chuyển bytes thành string để lưu JSON

    @staticmethod
    def verify_password(input_password, stored_hashed_password):
        return bcrypt.checkpw(input_password.encode(), stored_hashed_password.encode())
    def add_player(self, player_id, name, username, password, balance):
        """Thêm người chơi mới."""
        self.player.add_player(player_id, name, username, password, balance)
    def add_employee(self, employee_id, name, username, password, address, phone):
        """Thêm nhân viên mới."""
        employee = Employee()
        employee.add_employee(employee_id, name, username, password, address, phone)

admin = Admin()
admin.add("admin", "admin")