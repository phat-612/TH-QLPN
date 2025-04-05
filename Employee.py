import json
import bcrypt
import os
class Employee:
    def __init__(self):
        self.load_data()
        pass
    
    def load_data(self):
        """Load data from the JSON file."""
        try:
            with open("database/employees.json", 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []
        
    def get_employee_info(self, username):
        """Get employee information by username."""
        for employee in self.data:
            if employee["configuration"]["username"] == username:
                return employee["employee_id"], employee["configuration"]["name"],
                
    def save_data(self):
        """Save data to the JSON file."""
        with open("database/employees.json", 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
        self.load_data()  # Tải lại dữ liệu sau khi lưu để đảm bảo tính nhất quán
    def login(self, username, password):
        for employee in self.data:
            if employee['configuration']["username"] == username and self.verify_password(password, employee['configuration']["password"]):
                print("Đăng nhập thành công")
                return True
        print("Đăng nhập thất bại")
        return False
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()  # Chuyển bytes thành string để lưu JSON

    @staticmethod
    def verify_password(input_password, stored_hashed_password):
        return bcrypt.checkpw(input_password.encode(), stored_hashed_password.encode())
    def add_employee(self, name, username, password, address, phone):
        """Add a new employee."""
        
        if self.data:
            last_id = max(employee["employee_id"] for employee in self.data)
            employee_id = last_id + 1
        else:
            employee_id = 1  # Nếu danh sách rỗng, bắt đầu từ 1
       
        new_employee = {
            "employee_id": employee_id,
            "configuration": {
                "name": name,
                "username": username,
                "password": self.hash_password(password),  # Mã hóa mật khẩu
                "address": address,
                "phone": phone
            }
        }
        self.data.append(new_employee)
        self.save_data()
        print ("Thêm nhân viên thành công")
    
    def update_employee(self, employee_id, **kwargs):
        """Update an existing employee's details."""
        for emp in self.data:
            if emp["employee_id"] == employee_id:
                for key, value in kwargs.items():
                    if key in emp:
                        emp[key] = value
                self.save_data()
                print("Cập nhật thành công")
                return True
        return False
    
    def delete_employee(self, employee_id):
        """Delete an employee by ID."""
        self.data = [emp for emp in self.data if emp["employee_id"] != employee_id]
        self.save_data()
        print("Xóa nhân viên thành công")
    
    def get_all_employees(self):
        """Retrieve all employees."""
        return self.data
    
    def get_employee(self, employee_id):
        """Retrieve a specific employee by ID."""
        for emp in self.data:
            if emp["employee_id"] == employee_id:
                return emp
        return None

# # Example usage:
# manager = Employee()
# # manager.add_employee(1010, "Nguyen Van Phat", "nguyenvanphat", "secure_password", "456 XYZ Street", "0987654321")
# manager.update_employee(2, name="Tran Van C")
# # manager.delete_employee(2)
# # print(manager.get_all_employees())