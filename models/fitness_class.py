from multiprocessing.dummy import active_children


class FitnessClass:
    def __init__ (self, name, category, day, time, active = True, premium = False, id = None):
        self.name = name
        self.category = category
        self.day = day
        self.time = time
        self.active = active
        self.premium = premium
        self.capacity = {
            "Gym" : 5,
            "Cardio" : 5,
            "Mind & Body" : 10 
        }
        self.full = False
        self.id = id
        