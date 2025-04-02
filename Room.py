import json
class Room:
    def __init__(self, file_path="database/rooms.json"):
        self.file_path = file_path
        self.rooms = self.load_rooms()

    
    def load_rooms(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file).get("rooms", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_rooms(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({"rooms": self.rooms}, file, indent=4, ensure_ascii=False)
        
    def add_room (self, room_id, room_name, limit_cpt):
        if any(room["room_id"] == room_id for room in self.rooms):
            print(f"Phòng {room_name} đã tồn tại!")
            return

        new_room = {
            "room_id": self.room_id,
            "room_name": self.room_name,
            "limit_cpt": self.limit_cpt,
            "list_computers": []
        }
        self.rooms.append(new_room)
        self.save_rooms()
        print(f"Đã thêm phòng {room_name}!")
        
    def add_computer_to_room(self, room_id, computer_id, status="active"):
        for room in self.rooms:
            if room["room_id"] == room_id:
                if any(computer["computer_id"] == computer_id for computer in room["list_computers"]):
                    print(f"Máy tính {computer_id} đã có trong phòng {room['room_name']}, không thể thêm lại!")
                    return
                room["list_computers"].append({"computer_id": computer_id, "status": status})
                self.save_rooms()
                print(f"Đã thêm máy tính {computer_id} vào phòng {room['room_name']}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")

    def remove_computer_from_room(self, room_id, computer_id):
        for room in self.rooms:
            if room["room_id"] == room_id:
                room["list_computers"] = [comp for comp in room["list_computers"] if comp["computer_id"] != computer_id]
                self.save_rooms()
                print(f"Đã xóa máy tính {computer_id} khỏi phòng {room['room_name']}!")
                return
        print(f"Phòng có ID {room_id} không tồn tại!")
    
    def remove_room(self, room_id):
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
        print(json.dumps({"rooms": self.rooms}, indent=4, ensure_ascii=False))

# Sử dụng
room_manager = Room()
room_manager.add_room(1, "PM1", 40)
room_manager.add_computer_to_room(1, 101, "active")
room_manager.add_computer_to_room(1, 102, "broken")
room_manager.add_computer_to_room(1, 103, "maintenance")
room_manager.show_rooms()
room_manager.remove_computer_from_room(1, 101)
room_manager.show_rooms()
room_manager.remove_room(1)  # Không thể xóa do còn máy tính
room_manager.remove_computer_from_room(1, 102)
room_manager.remove_room(1)  # Bây giờ có thể xóa
room_manager.show_rooms()