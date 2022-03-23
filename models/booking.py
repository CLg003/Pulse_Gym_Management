class Booking:
    def __init__ (self, member, fitness_class, arrived = False, id = None):
        self.member = member
        self.fitness_class = fitness_class
        self.arrived = arrived
        self.id = id