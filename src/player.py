# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, items):

        self.name = name
        self.current_room = starting_room
        self.current_item = items
        
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")


    def pickup(self, item):
        desired_item = self.current_item.get_item(item)
        if desired_item is not None:
            self.current_item = desired_item
            print(self.current_item)
        else:
            print("That item does not exist")

