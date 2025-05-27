# ### Exercise 1:

# class GamePlayer:
    
#     BOARD_SPACES = [
#     "START",
#     "BROWN_1", "EVENT_1", "BROWN_2", "TAXATION",
#     "STATION_1", "CYAN_1", "CHANCE_1", "CYAN_2", "CYAN_3",
#     "PRISON",
#     "PINK_1", "UTILITY_1", "PINK_2", "PINK_3",
#     "STATION_2", "ORANGE_1", "EVENT_2", "ORANGE_2", "ORANGE_3",
#     "DOG_PARK",
#     "RED_1", "CHANCE_2", "RED_2", "RED_3",
#     "STATION_3", "YELLOW_1", "YELLOW_2", "UTILITY_2", "YELLOW_3",
#     "GO_TO_PRISON",
#     "GREEN_1", "GREEN_2", "COMMUNITY_3", "GREEN_3",
#     "STATION_4", "CHANCE_3", "BLUE_1", "BIG_TAX", "BLUE_2"
#     ]
    
#     def __init__(self, name, token):
#         self.name = name
#         self.token = token
#         self.money = 1500
#         self.position = 0
#         self.owned_properties = []
        
#     def move(self, spaces):
#         self.position = (self.position + spaces) % 40
#         return GamePlayer.BOARD_SPACES[self.position]
        
#     def move_to(self, space_index):
#         self.position = space_index
#         return GamePlayer.BOARD_SPACES[self.position]
        
#     def pay(self, amount):
#         if amount > self.money:
#             return None
#         else:
#             self.money = self.money - amount
#             return amount
    
    
# Jason = GamePlayer("Jason", "racecar")
# Krishna = GamePlayer("Krishna", "puppy")
# Matt = GamePlayer("Matt", "Battleship")
# Maria = GamePlayer("Maria", "Horse")

# location = Jason.move(12)
# print("Jason", location)
# location = Matt.move(12)
# print("Matt", location)
# Maria.move(15)
# Krishna.move(10)

# location = Jason.move(2)
# print(location)
# location = Matt.move(3)
# print(location)



# ### Exercise 2:
import random

class Dice:
    
    def __init__(self, value=None):
        if value == None:
            self.roll()
        else:
            self.value = value
        
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return f'Dice({self.value})'
        
    def __lt__(self, other):
        return self.value < other.value
        
    def roll(self):
        self.value = random.randint(1, 6)
        return self.value
        
dice = [Dice(), Dice(), Dice(), Dice(), Dice()]
# dice = Dice()
print(dice)
dice.sort()
print(dice)