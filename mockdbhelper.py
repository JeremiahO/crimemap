class MockDBHelper:
    def connect(self, database="crimemap"):
        pass

    def get_all_inputs(self):
        return []  # 'billy', 'bobby', 'frank', For testing purposes.

    def add_input(self, data):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass
