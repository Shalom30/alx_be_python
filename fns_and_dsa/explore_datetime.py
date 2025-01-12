from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)



def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)


display_current_datetime()
calculate_future_date()
