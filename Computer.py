import json


class Computer:
    def getData(self):
        try:
            with open("database/computers.json", "r", encoding="utf-8") as file:
                data = json.load(file)  # lấy dữ liệu
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"computers": []}  # Nếu file không tồn tại hoặc dữ liệu không hợp lệ
        return data

    def saveData(self, data):
        # Ghi lại dữ liệu vào file
        with open("database/computers.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    def __init__(self):
        pass
    def addComputer(self, computer_id=None, monitor=None, cpu=None, ram=None, storage_type=None, storage_capacity=None, status=None):
        data = self.getData()

        # Nếu không truyền `computer_id`, lấy id cuối cùng + 1
        if computer_id is None:
            if data["computers"]:
                last_id = max(computer["computer_id"] for computer in data["computers"])
                self.computer_id = last_id + 1
            else:
                self.computer_id = 1  # Nếu danh sách rỗng, bắt đầu từ 1
        else:
            self.computer_id = computer_id

        self.monitor = monitor
        self.cpu = cpu
        self.ram = ram
        self.storage_type = storage_type
        self.storage_capacity = storage_capacity
        self.status = status

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
        self.saveData(data)  # Lưu lại dữ liệu mới vào file
        print(f"Máy tính có ID {self.computer_id} đã được thêm thành công.")
    def editComputer (self, computer_id=None, monitor=None, cpu=None, ram=None, storage_type=None, storage_capacity=None, status=None):
        if computer_id is None:
            print('Máy tính không tồn tại')
        data = self.getData()
        computer_id = int(computer_id)
        # Tìm máy tính theo ID
        computers = data['computers']
        isEdit = False
        for computer in computers:
            if computer['computer_id'] == computer_id:
                # Cập nhật thông tin máy tính
                if monitor is not None:
                    computer['configuration']['monitor'] = monitor
                if cpu is not None:
                    computer['configuration']['CPU'] = cpu
                if ram is not None:
                    computer['configuration']['RAM'] = ram
                if storage_type is not None:
                    computer['configuration']['storageType'] = storage_type
                if storage_capacity is not None:
                    computer['configuration']['storageCapacity'] = storage_capacity
                if status is not None:
                    computer['configuration']['status'] = status
                isEdit = True
                break
        if not isEdit:
            print(f"Máy tính với ID {computer_id} không tồn tại.")
            return
        # Lưu lại dữ liệu đã chỉnh sửa vào file
        print(f"Máy tính với ID {computer_id} đã được chỉnh sửa thành công.")
        self.saveData(data)
    def deleteComputer (self, computer_id):
        computer_id = int(computer_id)
        if computer_id is None:
            print('Máy tính không tồn tại')
        data = self.getData()
        # Tìm máy tính theo ID
        computers = data['computers']
        isDelete = False
        for computer in computers:
            if computer['computer_id'] == computer_id:
                isDelete = True
                data['computers'].remove(computer)
                break
        if not isDelete:
            print(f"Máy tính với ID {computer_id} không tồn tại.")
            return
        # Lưu lại dữ liệu đã chỉnh sửa vào file
        print(f"Máy tính với ID {computer_id} đã được xóa thành công.")
        self.saveData(data)
    def getComputer(self, computer_id=None):
        data = self.getData()
        computers = data["computers"]
        if computer_id is None:
            return computers
        for computer in computers:
            if computer["computer_id"] == computer_id:
                return computer
        return None
    def showAllComputer(self):
        data = self.getData()
        computers = data["computers"]
        if len(computers) == 0:
            print("Không có máy tính nào")
        for index, computer in enumerate(computers, start=1):
            print(f"\n🖥️ Máy tính {index}:")
            print(f"   🆔 ID: {computer['computer_id']}")
            print(f"   🖥️ Màn hình: {computer['configuration']['monitor']}")
            print(f"   🔢 CPU: {computer['configuration']['CPU']}")
            print(f"   💾 RAM: {computer['configuration']['RAM']}")
            print(f"   🗄️ Loại ổ cứng: {computer['configuration']['storageType']}")
            print(f"   💽 Dung lượng ổ cứng: {computer['configuration']['storageCapacity']}")
            print(f"   ✅ Trạng thái: {computer['configuration']['status']}")
    def show_computer_status(self, status):
        data = self.getData()
        computers = data["computers"]
        filtered_computers = [computer for computer in computers if computer["configuration"]["status"] == status]
        if len(filtered_computers) == 0:
            print(f"Không có máy tính nào với trạng thái {status}.")
        else:
            for index, computer in enumerate(filtered_computers, start=1):
                print(f"\n🖥️{index}. Máy {computer['computer_id']}")
