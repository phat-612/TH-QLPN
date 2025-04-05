import json

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
            self.data = {"employees": []}
        
    
    def save_data(self):
        """Save data to the JSON file."""
        with open("database/employees.json", 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
    
    def add_employee(self, employee_id, name, username, password, address, phone):
        """Add a new employee."""
        new_employee = {
            "employee_id": employee_id,
            "configuration": {
                "name": name,
                "username": username,
                "password": password, 
                "address": address,
                "phone": phone
            }
        }
        self.data["employees"].append(new_employee)
        self.save_data()
        print ("Thêm nhân viên thành công")
    
    def update_employee(self, employee_id, **kwargs):
        """Update an existing employee's details."""
        for emp in self.data["employees"]:
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
        self.data["employees"] = [emp for emp in self.data["employees"] if emp["employee_id"] != employee_id]
        self.save_data()
        print("Xóa nhân viên thành công")
    
    def get_all_employees(self):
        """Retrieve all employees."""
        return self.data["employees"]
    
    def get_employee(self, employee_id):
        """Retrieve a specific employee by ID."""
        for emp in self.data["employees"]:
            if emp["employee_id"] == employee_id:
                return emp
        return None

# # Example usage:
# manager = Employee()
# # manager.add_employee(1010, "Nguyen Van Phat", "nguyenvanphat", "secure_password", "456 XYZ Street", "0987654321")
# manager.update_employee(2, name="Tran Van C")
# # manager.delete_employee(2)
# # print(manager.get_all_employees())