import json 
class Transaction:
    def __init__(self, transaction_id, player_id, amount, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.player_id = player_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        try:
            with open("database/transactions.json", "r", encoding="utf-8") as file:
                data = json.load(file) # lấy dữ liệu
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"transactions": []}  
        new_transaction = {
        "transaction_id": self.transaction_id,   
        "player_id": self.player_id,
        "amount": self.amount,
        "type": self.transaction_type,
        "timestamp": self.timestamp,
        }
        data["transactions"].append(new_transaction)
        with open("database/transactions.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # sửa máy tính 
    
    def edit_transaction(transaction_id, new_player_id, new_amount, new_transaction_type, new_timestamp):
        try:
            with open("database/transactions.json", "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc dữ liệu từ file
        except (FileNotFoundError, json.JSONDecodeError):
            print("Không tìm thấy dữ liệu giao dịch.")
            return

        # Tìm giao dịch cần sửa và cập nhật các thông tin
        for transaction in data["transactions"]:
            if transaction["transaction_id"] == transaction_id:
                transaction["player_id"] = new_player_id
                transaction["amount"] = new_amount
                transaction["type"] = new_transaction_type
                transaction["timestamp"] = new_timestamp
                break
        else:
            print("Không tìm thấy giao dịch cần chỉnh sửa.")
            return

        # Lưu lại các thay đổi vào tệp JSON
        with open("database/transactions.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Cập nhật file

        print("Giao dịch đã được cập nhật thành công.")

    def delete_transaction(transaction_id):
        try:
            # Đọc dữ liệu từ tệp JSON
            with open("database/transactions.json", "r", encoding="utf-8") as file:
                data = json.load(file)  
        except (FileNotFoundError, json.JSONDecodeError):
            print("Không tìm thấy dữ liệu giao dịch.")
            return

        # Tìm giao dịch cần xóa
        transaction_found = False
        for transaction in data["transactions"]:
            if transaction["transaction_id"] == transaction_id:
                data["transactions"].remove(transaction)  # Xóa giao dịch
                transaction_found = True
                break

        if not transaction_found:
            print("Không tìm thấy giao dịch cần xóa.")
            return

        # Lưu lại các thay đổi vào tệp JSON
        with open("database/transactions.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Cập nhật file

        print("Giao dịch đã được xóa thành công.")
# Gọi hàm sửa giao dịch
# transaction1 = Transaction.edit_transaction(
#     transaction_id=101242342332,
#     new_player_id=3,
#     new_amount=-21000,
#     new_transaction_type="player",
#     new_timestamp="2025-04-02 11:00:00"
# )
transaction1 = Transaction.delete_transaction(101242342332)
print("Đã xóa thành công")

