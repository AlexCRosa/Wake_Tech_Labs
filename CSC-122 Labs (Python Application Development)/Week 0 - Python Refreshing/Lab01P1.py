# 
# Alex Cesar Rosa
# 8/21/2024
# This program prompts the user to enter daily temperature information
# and then provides analysis of the data.
#

def collect_data(days):
    """Collects temperature data for a given number of days."""
    temperatures = []

    # Enter code here that will ask the user for the temperature for
    # Each of the days and add that data to the temperature list.
    # Temperature data is a number so make sure to catch if the user
    # doesn't enter a proper floating point number.

    i = 0
    while i < days:
        try:
            temperature = float(input(f"Enter the temperature for day {i + 1}: "))
            temperatures.append(temperature)
            i += 1
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return temperatures

def calculate_average(temperatures):
    """Calculates and returns the average temperature."""
    average = sum(temperatures) / len(temperatures)
    return average

def find_max(temperatures):
    """Finds and returns the highest temperature."""
    return max(temperatures)

def find_min(temperatures):
    """Finds and returns the lowest temperature."""
    return min(temperatures)

def above_threshold(temperatures, threshold):
    """Returns a list of temperatures above the given threshold."""
    new_list = []

    for item in temperatures:
        if item > threshold:
            new_list.append(item)
        else:
            continue

    return new_list

def main():
    days = int(input("How many days of temperature data do you want to analyze? "))
    temps = collect_data(days)

    print("\nWeather Data Analysis")
    print("1. Average Temperature")
    print("2. Highest Temperature")
    print("3. Lowest Temperature")
    print("4. Temperatures Above Threshold")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1':
            print(f"Average Temperature: {calculate_average(temps)}")
        elif choice == '2':
            print(f"Highest Temperature: {find_max(temps)}")
        elif choice == '3':
            print(f"Lowest Temperature: {find_min(temps)}")
        elif choice == '4':
            threshold = float(input("Enter the temperature threshold: "))
            print(f"Temperatures above {threshold}: {above_threshold(temps, threshold)}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
