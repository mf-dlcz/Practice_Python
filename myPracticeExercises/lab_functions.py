import json

"""
    CHECKING NUMBERS:
"""

"""                     TASKS:
-   Create two number-checker functions, isEven and isOdd. 
The isEven function should return True if the argument passed 
into it is an even number, and False if the argument is an odd 
number. The isOdd function should return True if the argument 
passed into it is odd, and False if the argument is even. Test 
each function by using a loop to evaluate numbers zero through nine.
"""

def isEven(number):
    return number % 2 == 0


def isOdd(number):
    return number % 2 != 0


for numb in range(10):
    even = isEven(numb)
    odd = isOdd(numb)
    # print(f'{numb} is even: {even} \t odd: {odd}')


#       ######################################################                          TRACKING GAME SCORES:
"""
-   Create a score-tracking system that can do the following:
1.  Calculate round scores considering base points, multipliers, and bonus points
2.  Track and update the all-time high score
3.  Record individual player statistics, including games played, wins, and losses
4.  Generate detailed player reports with performance metrics
"""

# Global variables for tracking game statistics
high_score = 0
current_score = 0
player_stats = {}

#       Task 1: Create a function that calculates player's round score
def calculate_round_score(base_points, multiplier = 1, *bonus_points):
#     # Parameters: base_points, multiplier=1, *bonus_points
#     # Use pow() for multiplier and add sum of bonus points
#     # Return the total round score
        score = pow(base_points, multiplier)
        if bonus_points:
            score += sum(bonus_points)
        return score

# print(calculate_round_score(100))
# print(calculate_round_score(100, 2))
# print(calculate_round_score(100, 2, 10, 20, 30))

#       ************************************************************

#       Task 2: Update the high score if necessary
def update_high_score():
    # Use global keyword for high_score and current_score
    # Use max() to compare current_score with high_score
    # Update high_score if current_score is higher
    global high_score, current_score
    high_score = max(current_score, high_score)
    return high_score

# print(update_high_score())

#       ************************************************************

#       Task 3: Track player statistics
def record_player_stats(player_name, **stats):
    # Parameters: player_name, **stats
    # Stats should include: rounds_played, wins, losses
    # Use abs() to ensure all stats are positive numbers
    # Store in player_stats dictionary
    positive_stats = {}
    for key, value in stats.items():
        positive = abs(value)
        positive_stats[key] = positive
    player_stats[player_name] = positive_stats
    return player_stats

# result = record_player_stats("Maria",rounds_played = 10, wins = 7, losses = 3)
# print(json.dumps(result, indent = 4))

#       ************************************************************

#       Task 4: Generate player report
#               PARAMETER
def generate_report(player_name):
    # Parameter: player_name
    # Return None if player not found
    # Calculate win percentage (wins / rounds_played)
    # Return formatted string with player stats
    if player_name not in player_stats:
        return None
    
    stats = player_stats[player_name]
    wins = stats.get('wins', 0)
    rounds = stats.get('rounds_played', 0)
    losses = stats.get('losses', 0)
    if rounds > 0:     
        win_percentage = (wins / rounds * 100)
    else:
        win_percentage = 0

    return f"""
        Player: {player_name}
        Rounds Player: {rounds}
        Wins: {wins}
        Losses: {losses}
        Win Percentage = {win_percentage}%
        """

#                           ARGUMENT                        
# result_2 = generate_report('Maria')
# print(result_2)

print("Testing round score calculation:")
print(calculate_round_score(100))  # Base points only
print(calculate_round_score(100, 2))  # With multiplier
print(calculate_round_score(100, 2, 10, 20, 30))  # With bonus points

print("\nTesting high score update:")
current_score = 1000
print(f"New high score: {update_high_score()}")

print("\nTesting player stats recording and reporting:")
record_player_stats("Player1", rounds_played=10, wins=7, losses=3)
print(generate_report("Player1"))