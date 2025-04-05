from Computer import Computer
from Player import Player
from Admin import Admin
from Employee import Employee
import json


def menu_player():
    
    while True:
        print("----CHAO MUNG BAN DEN VOI THE GIOI GAME----")
        print("1. Tong thoi gian ban muon choi game")
        print("2. Kiem tra so tien trong tai khoan")
        print("3. Nap tien vao tai khoan")
        print("4. Thoat")
        choice = input("Lua chon: ")

        if choice == "1":
            print("Ban da chon: Tong thoi gian ban muon choi game")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "2":
            print("Ban da chon: Kiem tra so tien trong tai khoan")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "3":
            print("Ban da chon: Nap tien vao tai khoan")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "4":
            print("Thoat menu Nguoi choi. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

def menu_admin():
    print("----CHAO MUNG BAN DEN VOI HE THONG QUAN LY PHONG NET----")
    print("Nhap thong tin admin de dang nhap")
    username = input("Ten dang nhap: ")
    password = input("Mat khau: ")
    admin = Admin()
    if admin.login(username, password):
        while True:
            print("----CHAO MUNG BAN DEN VOI HE THONG QUAN LY PHONG NET----")
            print("1. Tong doanh thu trong ngay")
            print("2. Xem tinh trang may")
            print("3. Xem bao cao vi pham")
            print("4. Tao tai khoan nhan vien")
            print("5. Tao tai khoan nguoi choi")
            print("5. Thoat")
            choice = input("Lua chon: ")

            if choice == "1":
                print("Ban da chon: Tong doanh thu trong ngay")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "2":
                print("Ban da chon: Xem tinh trang may")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "3":
                print("Ban da chon: Xem bao cao vi pham")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "4":
                print("Ban da chon: Tao tai khoan nhan vien")
                username = input("Ten dang nhap: ")
                password = input("Mat khau: ")
                name = input("Ten nhan vien: ")
                address = input("Dia chi: ")
                phone = input("So dien thoai: ")
                admin.add_employee(employee_id=1, name=name, username=username, password=password, address=address, phone=phone)
            elif choice == "5":
                print("Ban da chon: Tao tai khoan nguoi choi")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "6":
                print("Thoat menu Quan tri. Tam biet!")
                break

            
    else:
        print("Dang nhap khong thanh cong. Vui long kiem tra lai thong tin dang nhap.")
        return
def menu_employee():
    while True:
        print("----CHAO MUNG BAN DEN VOI HE THONG QUAN LY PHONG NET----")
        print("1. Quan ly nguoi choi")
        print("2. Quan ly nhan vien")
        print("3. Quan ly may tinh")
        print("4. Thoat")
        choice = input("Lua chon: ")

        if choice == "1":
            print("Ban da chon: Quan ly nguoi choi")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "2":
            print("Ban da chon: Quan ly nhan vien")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "3":
            print("Ban da chon: Quan ly may tinh")
            # Thêm logic xử lý cho tùy chọn này
        elif choice == "4":
            print("Thoat menu Nhan vien. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

def main_menu():
    while True:
        print("---HE THONG QUAN LY PHONG NET---")
        print("------VUI LONG DANG NHAP DE SU DUNG CHUC NANG------")
        print("1. Nguoi choi")
        print("2. Nhan vien")
        print("3. Quan tri")
        print("4. Thoat")
        choice = input("Lua chon: ")

        if choice == "1":
            print("Dang nhap voi tu cach Nguoi choi")
            # Thêm logic xử lý cho Nguoi choi
        elif choice == "2":
            print("Dang nhap voi tu cach Nhan vien")
            # Thêm logic xử lý cho Nhan vien
        elif choice == "3":
            print("Dang nhap voi tu cach Quan tri")
            # Thêm logic xử lý cho Quan tri
        elif choice == "4":
            print("Thoat chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

if __name__ == "__main__":
    main_menu()