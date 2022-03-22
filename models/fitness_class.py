from multiprocessing.dummy import active_children


class FitnessClass:
    def __init__ (self, name, category, day, time, active = True, id = None):
        self.name = name
        self.category = category
        self.day = day
        self.time = time
        self.active = active
        self.capacity = {
            "Gym" : 5,
            "Cardio" : 5,
            "Mind & Body" : 10 
        }
        self.full = False
        self.id = id
        