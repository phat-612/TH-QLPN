import json
import datetime

class Transaction:
    def __init__(self, file_path="database/transactions.json"):
        self.file_path = file_path

    def load_data(self):
        """Tải dữ liệu từ file JSON."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return { []}  # Trả về danh sách rỗng nếu file không tồn tại hoặc lỗi

    def save_data(self, data):
        """Lưu dữ liệu vào file JSON."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_transaction(self, player_id, amount, transaction_type):
        """Thêm giao dịch mới."""
        data = self.load_data()
        transaction_id = len(data) + 1  # Tạo ID giao dịch mới
        timestamp = datetime.datetime.now().isoformat()

        new_transaction = {
            "transaction_id": transaction_id,
            "player_id": player_id,
            "amount": amount,
            "type": transaction_type,
            "timestamp": timestamp,
        }
        data.append(new_transaction)
        self.save_data(data)
        print(f"Giao dịch mới đã được thêm: {new_transaction}")

    def edit_transaction(self, transaction_id, new_player_id, new_amount, new_transaction_type, new_timestamp):
        """Sửa thông tin giao dịch."""
        data = self.load_data()

        # Tìm giao dịch cần sửa và cập nhật các thông tin
        for transaction in data:
            if transaction["transaction_id"] == transaction_id:
                transaction["player_id"] = new_player_id
                transaction["amount"] = new_amount
                transaction["type"] = new_transaction_type
                transaction["timestamp"] = new_timestamp
                break
        else:
            print("Không tìm thấy giao dịch cần chỉnh sửa.")
            return

        self.save_data(data)
        print("Giao dịch đã được cập nhật thành công.")

    def delete_transaction(self, transaction_id):
        """Xóa giao dịch theo ID."""
        data = self.load_data()

        # Tìm giao dịch cần xóa
        transaction_found = False
        for transaction in data:
            if transaction["transaction_id"] == transaction_id:
                data.remove(transaction)
                transaction_found = True
                break

        if not transaction_found:
            print("Không tìm thấy giao dịch cần xóa.")
            return

        self.save_data(data)
        print("Giao dịch đã được xóa thành công.")

    def get_daily_revenue(self, date=None):
        """
        Lấy tổng doanh thu trong ngày.
        :param date: Ngày cần tính doanh thu (định dạng 'YYYY-MM-DD'). Nếu không truyền, lấy ngày hiện tại.
        :return: Tổng doanh thu trong ngày.
        """
        if date is None:
            date = datetime.datetime.now().strftime('%Y-%m-%d')  # Lấy ngày hiện tại nếu không truyền

        data = self.load_data()

        # Tính tổng doanh thu trong ngày
        total_revenue = 0
        if "transactions" not in data:
            print("Không có giao dịch nào.")
            return total_revenue
        for transaction in data:
            transaction_date = transaction["timestamp"].split("T")[0]  # Lấy phần ngày từ timestamp
            if transaction_date == date and transaction["amount"] > 0:  # Chỉ tính các giao dịch có số tiền dương
                total_revenue += transaction["amount"]

        return total_revenue

