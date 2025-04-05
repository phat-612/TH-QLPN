import json
import bcrypt
import os
class Admin:
    def __init__(self, ):
        self.username = None
        self.password = None
        pass
    def getData(self):
        try:
            with open("database/admin.json", "r", encoding="utf-8") as file:
                data = json.load(file)  # lấy dữ liệu
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"computers": []}  # Nếu file không tồn tại hoặc dữ liệu không hợp lệ
        return data
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
        admin_data = self.getData()
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
    
admin = Admin()
admin.add("admin", "admin")