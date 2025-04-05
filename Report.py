import json
from datetime import datetime

class Report:
    def __init__(self, file_path="database/reports.json"):
        self.file_path = file_path

    def load_reports(self):
        """Tải dữ liệu từ file reports.json."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reports(self, reports):
        """Lưu dữ liệu vào file reports.json."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(reports, file, ensure_ascii=False, indent=4)

    def add_report(self, reported_by_username, reported_player_username, reason):
        """Thêm một báo cáo mới."""
        reports = self.load_reports()
        new_report = {
            "report_id": len(reports) + 1,
            "reported_by_username": reported_by_username,
            "reported_player_username": reported_player_username,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        reports.append(new_report)
        self.save_reports(reports)
        print(f"Báo cáo mới đã được thêm: {new_report}")

    def get_reports_by_player(self, player_id):
        """Lấy danh sách báo cáo liên quan đến một người chơi cụ thể."""
        reports = self.load_reports()
        return [report for report in reports if report["reported_player_username"] == player_id]

    def get_all_reports(self):
        """Lấy toàn bộ danh sách báo cáo."""
        return self.load_reports()
    def show_report(self):
        """Hiển thị thông tin của một báo cáo."""
        reports = self.load_reports()
        if not reports:
            print("Không có báo cáo nào.")
            return
        for report in reports:
            print(f"Thông tin báo cáo: {report}")
            return
    def delete_report(self, report_id):
        """Xóa một báo cáo theo ID."""
        reports = self.load_reports()
        updated_reports = [report for report in reports if report["report_id"] != report_id]
        if len(reports) == len(updated_reports):
            print(f"Không tìm thấy báo cáo với ID: {report_id}")
        else:
            self.save_reports(updated_reports)
            print(f"Đã xóa báo cáo với ID: {report_id}")


