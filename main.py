from Computer import Computer
from Player import Player
from Admin import Admin
from Employee import Employee
from Report import Report
from Transaction import Transaction
from Room import Room

import json


def menu_player():
    print("----CHAO MUNG BAN DEN VOI THE GIOI GAME----")
    print("Nhap thong tin de dang nhap")
    username = input("Ten dang nhap: ")
    password = input("Mat khau: ")
    player = Player()
    transaction = Transaction()
    if player.login(username, password):
        player_id, name, username, balance = player.get_player_info(username)
        balance = int(balance)
        print(f"Xin chao {name}! So du tai khoan cua ban la: {balance}")
        while True:
            print(f"----CHAO MUNG BAN DEN VOI THE GIOI GAME - {name}----")
            print("1. Tong thoi gian ban muon choi game")
            print("2. Kiem tra so tien trong tai khoan")
            print("3. Nap tien vao tai khoan")
            print("4. Thoat")
            choice = input("Lua chon: ")

            if choice == "1":
                print("Ban da chon: Tong thoi gian ban muon choi game")
                time_play = int(input("Nhap thoi gian choi game (phut): "))
                
                time_play = int(time_play)
                if time_play <= 0:
                    print("Thoi gian choi game phai lon hon 0.")
                    continue
                else:
                    print(f"Ban da chon choi game trong {time_play} phut.")
                    balance -= time_play * 100  # Giả sử mỗi phút chơi game tốn 1000 đồng
                    transaction.add_transaction(player_id=player_id, amount=-time_play * 100, transaction_type="play")
                    player.update_player(player_id=player_id, new_data={'balance': (balance)})
                
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "2":
                print("Ban da chon: Kiem tra so tien trong tai khoan")
                print(f"So du tai khoan cua ban la: {balance}")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "3":
                print("Ban da chon: Nap tien vao tai khoan")
                inp_balance = int(input("Nhap so tien ban muon nap: "))
                if inp_balance <= 0:
                    print("So tien nap phai lon hon 0.")
                    continue
                
                transaction.add_transaction(player_id=player_id, amount=inp_balance, transaction_type="deposit")
                player.update_player(player_id=player_id,new_data= {'balance':(inp_balance + balance)})
                balance += inp_balance
                print(f"Ban da nap {inp_balance} vao tai khoan {username}.")
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
            print("6. Thoat")
            choice = input("Lua chon: ")

            if choice == "1":
                print("Ban da chon: Tong doanh thu trong ngay")
                transaction = Transaction()
                print(f"Tong doanh thu trong ngay: {transaction.get_daily_revenue()}")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "2":
                print("Ban da chon: Xem tinh trang may")
                print("1. Xem tình trạng máy đang hoạt động")
                print("2. Xem tình trạng máy đang bảo trì")
                print("3. Xem tình trạng máy đang hỏng")
                sub_choice = input("Lua chon: ")
                if sub_choice == "1":
                    print("Ban da chon: Xem tinh trang may dang hoat dong")
                    computer = Computer()
                    computer.show_computer_status(status="active")
                elif sub_choice == "2":
                    print("Ban da chon: Xem tinh trang may dang bao tri")
                    computer = Computer()
                    computer.show_computer_status(status="maintenance")
                elif sub_choice == "3":
                    print("Ban da chon: Xem tinh trang may dang hong")
                    computer = Computer()
                    computer.show_computer_status(status="broken")
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "3":
                print("Ban da chon: Xem bao cao vi pham")
                report = Report()
                report.show_report()
                # Thêm logic xử lý cho tùy chọn này
            elif choice == "4":
                print("Ban da chon: Tao tai khoan nhan vien")
                username = input("Ten dang nhap: ")
                password = input("Mat khau: ")
                name = input("Ten nhan vien: ")
                address = input("Dia chi: ")
                phone = input("So dien thoai: ")
                employee = Employee()
                employee.add_employee(name=name, username=username, password=password, address=address, phone=phone)
            elif choice == "5":
                print("Ban da chon: Tao tai khoan nguoi choi")
                # Thêm logic xử lý cho tùy chọn này
                username = input("Ten dang nhap: ")
                password = input("Mat khau: ")
                name = input("Ten nguoi choi: ")
                balance = input("So du: ")
                player = Player()
                player.add_player(name=name, username=username, password=password, balance=balance)
            elif choice == "6":
                print("Thoat menu Quan tri. Tam biet!")
                break

            
    else:
        print("Dang nhap khong thanh cong. Vui long kiem tra lai thong tin dang nhap.")
        return
def menu_employee():
    print("----CHAO MUNG BAN DEN VOI HE THONG QUAN LY PHONG NET----")
    print("Nhap thong tin de dang nhap")
    username = input("Ten dang nhap: ")
    password = input("Mat khau: ")
    employee = Employee()
    if employee.login(username, password):
        employee_id, name = employee.get_employee_info(username)
        while True:
            print(f"----XIN CHAO NHANH VIEN {name}----")
            print("1. Bao cao tinh trang may")
            print("2. Bao cao vi pham")
            print("3. Thoat")
            choice = input("Lua chon: ")
            if choice == "1":
                print("Ban da chon: Bao cao tinh trang may")
                room = Room()
                room.show_rooms()
                room_id = input("Nhap ID phong: ")
                room.show_computers_in_room(room_id)
                computer_id = input("Nhap ID may: ")
                status = input("Nhap tinh trang (active/maintenance/broken): ")
                computer = Computer()
                computer.editComputer(computer_id = computer_id, status = status)
            elif choice == "2":
                print("Ban da chon: Bao cao vi pham")
                report = Report()
                reported_player_username = input("Nhap ten nguoi choi bi bao cao: ")
                reason = input("Nhap ly do bao cao: ")
                report.add_report(reported_by_username=username, reported_player_username=reported_player_username, reason=reason)
            elif choice == "3":
                print("Thoat menu Nhan vien. Tam biet!")
                break

        

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
            menu_player()
            # Thêm logic xử lý cho Nguoi choi
        elif choice == "2":
            print("Dang nhap voi tu cach Nhan vien")
            menu_employee()
            # Thêm logic xử lý cho Nhan vien
        elif choice == "3":
            print("Dang nhap voi tu cach Quan tri")
            menu_admin()
        elif choice == "4":
            print("Thoat chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

if __name__ == "__main__":
    main_menu()