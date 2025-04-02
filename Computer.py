import json

class Computer:
    def __init__(self, computer_id, monitor, cpu, ram, storage_type, storage_capacity, status):
        self.computer_id = computer_id
        self.monitor = monitor
        self.cpu = cpu
        self.ram = ram
        self.storage_type = storage_type
        self.storage_capacity = storage_capacity
        self.status = status
        
        # Đọc dữ liệu hiện tại từ file (nếu có)
        try:
            with open("database/computers.json", "r", encoding="utf-8") as file:
                data = json.load(file) # lấy dữ liệu
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"computers": []}  # Nếu file không tồn tại hoặc dữ liệu không hợp lệ

        # Thêm thông tin máy tính mới vào danh sách "computers"
        new_computer = {
            "computer_id": self.computer_id,
            "configuration": {
                "monitor": self.monitor,
                "CPU": self.cpu,
                "RAM": self.ram,
                "storageType": self.storage_type,
                "storageCapacity": self.storage_capacity,
                "status": self.status
            }
        }
        data["computers"].append(new_computer)

        # Ghi lại dữ liệu vào file
        with open("database/computers.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
computer1 = Computer(
    computer_id=101242342332  ,
    monitor="Dell 24 inch",
    cpu="Intel i5",
    ram="16GB",
    storage_type="SSD",
    storage_capacity="512GB",
    status="active"
)
print("Dữ liệu máy tính đã được ghi vào file.")
    