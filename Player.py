import json
import bcrypt
import os

class Player:
    def __init__(self):

        pass
    def add_player(self, name, username, password, balance):
        data = self.load_players()
        if data:
            last_id = max(player["player_id"] for player in data)
            player_id = last_id + 1
        else:
            player_id = 1  # Nếu danh sách rỗng, bắt đầu từ 1
        
        name = name
        username = username
        password = self.hash_password(password)  # Mã hóa mật khẩu
        balance = balance

        new_player = {
            "player_id": player_id,
            "name": name,
            "username": username,
            "password": password,  # Lưu mật khẩu đã mã hóa
            "balance": balance
        }

        data.append(new_player)
        self.save_players(data)
    def get_player_info(self, username):
        """Lấy thông tin người chơi theo tên đăng nhập."""
        player_data = self.load_players()
        for player in player_data:
            if player["username"] == username:
                return player["player_id"], player["name"], player['username'] , player["balance"]
        return None, None, None
    def login(self, username, password):
        player_data = self.load_players()
        for player in player_data:
            if player["username"] == username and self.verify_password(password, player["password"]):
                return True
        return False
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()  # Chuyển bytes thành string để lưu JSON

    @staticmethod
    def verify_password(input_password, stored_hashed_password):
        return bcrypt.checkpw(input_password.encode(), stored_hashed_password.encode())

    @staticmethod
    def load_players():
        try:
            with open("database/players.json", "r", encoding="utf-8") as file:
                return json.load(file) # lấy dữ liệu
        except (FileNotFoundError, json.JSONDecodeError):
            return {"players": []}

    @staticmethod
    def save_players(data):
        with open("database/players.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def update_player(player_id, new_data):
        data = Player.load_players()
        for player in data:
            if player["player_id"] == player_id:
                for key, value in new_data.items():
                    if key in player:  # Chỉ cập nhật các trường hợp lệ
                        player[key] = value
                Player.save_players(data)
                return "Cập nhật thành công!"
        return "Không tìm thấy người chơi!"

    @staticmethod
    def delete_player(player_id):
        data = Player.load_players()
        new_players = [player for player in data if player["player_id"] != player_id]
        if len(new_players) == len(data):
            return "Không tìm thấy người chơi để xóa!"
        data = new_players
        Player.save_players(data)
        return "Xóa thành công!"