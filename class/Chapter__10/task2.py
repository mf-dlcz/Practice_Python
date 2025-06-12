import random
import logging
from datetime import datetime

# TODO: Set up logging configuration here
logging.basicConfig(
    filename=f'weather_forecast_{datetime.now().strftime("%Y%m%d")}.log',
    # Add logging configuration parameters
)

def get_temperature():
    # TODO: Generate random temperatures for morning, afternoon, and evening
    # Morning temperature should be between 65-70
    # Afternoon temperature should be between 70-75
    # Evening temperature should be between 66-71
    
    # TODO: Add a logging.info statement
    pass
    #uncomment this return statement!
    #return morning, afternoon, evening

def get_weather_condition():
    conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Scattered Showers']
    # TODO: Implement input validation loop
    # - Get user input for a number between 0 and 4
    # - Validate the input
    # - Return the corresponding weather condition
    # - Handle possible errors
    pass

def generate_daily_forecast(day_number):
    morning_temp, afternoon_temp, evening_temp = get_temperature()
    condition = get_weather_condition()
    
    forecast = f"""
Day {day_number}:
Morning:   {morning_temp}°C, {condition}
Afternoon: {afternoon_temp}°C, {condition}
Evening:   {evening_temp}°C, {condition}
{'-' * 40}"""
    
    # TODO: Add logging statement
    
    return forecast

def display_weekly_forecast():
    print("\n 7-Day Weather Forecast ")
    print("-" * 40)
    
    # TODO: Implement loop to generate and display 7 days of forecasts
    # Add logging statement for successful completion

if __name__ == "__main__":
    print("Welcome to Weather Forecast!")
    display_weekly_forecast()