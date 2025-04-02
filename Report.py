class Report:
    def __init__(self, report_id, reported_by, reported_player_id, reason, timestamp):
        self.report_id = report_id
        self.reported_by = reported_by
        self.reported_player_id = reported_player_id
        self.reason = reason
        self.timestamp = timestamp