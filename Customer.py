class Customer:
    def __init__(self, first_name, last_name, account_number, rented_dvds=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.rented_dvds = rented_dvds
