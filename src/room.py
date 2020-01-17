# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item1, item2):

        self.name = name
        self.description = description
        self.item1 = item1
        self.item2 = item2

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"\nCurrent Location: {self.name}\n\n{self.description}\n\nItems in room: {self.item1} and {self.item2}\n"


    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    # def get_item(self, item1, item2):
    #     if item1 == item1:
    #         return self.





