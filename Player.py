import json
import bcrypt
import os

class Player:
    def __init__(self):
        pass
    def add_player(self, player_id, name, username, password, balance):
        self.player_id = player_id
        self.name = name
        self.username = username
        self.password = self.hash_password(password)  # Mã hóa mật khẩu
        self.balance = balance

        player_data = self.load_players()

        # Kiểm tra trùng ID
        for player in player_data["players"]:
            if player["player_id"] == self.player_id:
                print("ID người chơi đã tồn tại! Không thể thêm.")
                return

        new_player = {
            "player_id": self.player_id,
            "name": self.name,
            "username": self.username,
            "password": self.password,  # Lưu mật khẩu đã mã hóa
            "balance": self.balance
        }

        player_data["players"].append(new_player)
        self.save_players(player_data)
    def login(self, username, password):
        player_data = self.load_players()
        for player in player_data["players"]:
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
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"players": []}

    @staticmethod
    def save_players(data):
        with open("database/players.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def update_player(player_id, new_data):
        data = Player.load_players()
        for player in data["players"]:
            if player["player_id"] == player_id:
                player.update(new_data)
                Player.save_players(data)
                return "Cập nhật thành công!"
        return "Không tìm thấy người chơi!"

    @staticmethod
    def delete_player(player_id):
        data = Player.load_players()
        new_players = [player for player in data["players"] if player["player_id"] != player_id]
        
        if len(new_players) == len(data["players"]):
            return "Không tìm thấy người chơi để xóa!"
        
        data["players"] = new_players
        Player.save_players(data)
        return "Xóa thành công!"

# # Test thêm player mới
# playerTest = Player(
#     player_id=2,
#     name="Nguyễn Văn B",
#     username="0354514832",
#     password="1",
#     balance=100000
# )

# print("Thêm dữ liệu thành công")

# # Test cập nhật thông tin player
# print(Player.update_player(2, {"name": "Nguyễn Văn CC" ,"balance": 99900999}))

# # Test xóa player
# # print(Player.delete_player(2))
