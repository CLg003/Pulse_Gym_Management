class Member:
    def __init__(self, first_name, last_name, address, email, active = True, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.active = active
        self.id = id
        self.bookings = []
