class AccountDto:
    def __init__(self, id, name, page, size, initial_date, final_date, operator_name):
        self.id = id
        self.name = name
        self.page = page
        self.size = size
        self.initial_date = initial_date
        self.final_date = final_date
        self.operator_name = operator_name

    def is_valid_name_and_date(self):
        return self.is_valid_operator_name() and self.is_valid_date()

    def is_valid_operator_name(self):
        if self.operator_name is None:
            return False
        return True

    def is_valid_date(self):
        if self.initial_date is None and self.final_date is None:
            return False
        return True
