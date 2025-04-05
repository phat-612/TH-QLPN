import json

class Room:
    def __init__(self, file_path="database/rooms.json"):
        self.file_path = file_path
        self.rooms = self.load_rooms()
        print(self.rooms)

    def load_rooms(self):
        """Tải danh sách phòng từ file JSON."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_rooms(self):
        """Lưu danh sách phòng vào file JSON."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({"rooms": self.rooms}, file, indent=4, ensure_ascii=False)
        self.rooms = self.load_rooms()

    def add_room(self, room_name, limit_cpt):
        """Thêm một phòng mới."""
        room_id = len(self.rooms) + 1  # Tạo ID phòng mới
        new_room = {
            "room_id": room_id,
            "room_name": room_name,
            "limit_cpt": limit_cpt,
            "list_computers": []
        }
        self.rooms.append(new_room)
        self.save_rooms()
        print(f"Đã thêm phòng {room_name}!")

    def add_computer_to_room(self, room_id, computer_id):
        """Thêm máy tính vào phòng."""
        for room in self.rooms:
            if room["room_id"] == room_id:
                if any(computer["computer_id"] == computer_id for computer in room["list_computers"]):
                    print(f"Máy tính {computer_id} đã có trong phòng {room['room_name']}, không thể thêm lại!")
                    return
                room["list_computers"].append({"computer_id": computer_id})
                self.save_rooms()
                print(f"Đã thêm máy tính {computer_id} vào phòng {room['room_name']}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")

    def remove_computer_from_room(self, room_id, computer_id):
        """Xóa máy tính khỏi phòng."""
        for room in self.rooms:
            if room["room_id"] == room_id:
                room["list_computers"] = [comp for comp in room["list_computers"] if comp["computer_id"] != computer_id]
                self.save_rooms()
                print(f"Đã xóa máy tính {computer_id} khỏi phòng {room['room_name']}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")

    def remove_room(self, room_id):
        """Xóa một phòng."""
        for room in self.rooms:
            if room["room_id"] == room_id:
                if room["list_computers"]:
                    print(f"Không thể xóa phòng {room['room_name']} vì vẫn còn máy tính trong phòng!")
                    return
                self.rooms.remove(room)
                self.save_rooms()
                print(f"Đã xóa phòng {room['room_name']}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")

    def update_room(self, room_id, new_name=None, new_limit=None):
        """Cập nhật thông tin phòng."""
        for room in self.rooms:
            if room["room_id"] == room_id:
                if new_name:
                    room["room_name"] = new_name
                if new_limit is not None:
                    room["limit_cpt"] = new_limit
                self.save_rooms()
                print(f"Đã cập nhật phòng {room_id}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")

    def show_rooms(self):
        """Hiển thị danh sách phòng."""
        if not self.rooms:
            print("Không có phòng nào.")
            return
        print("Danh sách trong phòng:")
        for room in self.rooms:
            print(f"ID: {room['room_id']}, Tên: {room['room_name']}, Giới hạn máy tính: {room['limit_cpt']}")
    def show_computers_in_room(self, room_id):
        """Hiển thị danh sách máy tính trong một phòng."""
        room_id = int(room_id)
        for room in self.rooms:
            if room["room_id"] == room_id:
                if not room["list_computers"]:
                    print(f"Phòng {room['room_name']} không có máy tính nào.")
                    return
                print(f"Các máy tính trong phòng {room['room_name']}:")
                for computer in room["list_computers"]:
                    print(f"- Máy tính ID: {computer['computer_id']}")
                return