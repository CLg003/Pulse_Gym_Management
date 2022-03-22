class FitnessClass:
    def __init__ (self, name, category, day, time, id = None):
        self.name = name
        self.category = category
        self.day = day
        self.time = time
        self.capacity = {
            "Gym" : 5,
            "Cardio" : 5,
            "Mind & Body" : 10 
        }
        self.full = False
        self.id = id
        