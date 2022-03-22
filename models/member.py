class Member:
    def __init__(self, first_name, last_name, address, email, id = None, premium = False, active = True):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.id = id
        self.premium = premium
        self.active = active
        self.bookings = []
