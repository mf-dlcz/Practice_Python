import logging

# Set up logging to write to 'weather_diary.log'
# Include the time and level in the format
logging.basicConfig(
    filename='weather_diary.log',  # Fill this in!
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' # Fill this in!
)
# Log these weather events:
# - Sunny day
# - Cloudy with chance of rain
# - Thunder storm warning!