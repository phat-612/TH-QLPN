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
        
        # self.room_id = room_id
        # self.room_name = room_name
        # self.limit_cpt = limit_cpt
        # self.computers = []

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
    
    def show_rooms(self):
        print(json.dumps({"rooms": self.rooms}, indent=4, ensure_ascii=False))

# Sử dụng
room_manager = Room()
room_manager.add_room(1, "PM1", 40)
room_manager.add_computer_to_room(1, 101, "active")
room_manager.show_rooms()