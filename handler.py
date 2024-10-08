# Database of cars with their types, years, and available colors.
cars = {
    'Corolla': {
        'types': ['Sedan', 'Hatch'],
        'years': [2014, 2015, 2017, 2020, 2021, 2022],
        'colors': ['Silver', 'Black', 'Red'],
    },
    'Yaris': {
        'types': ['Hatch'],
        'years': [2014, 2016, 2017, 2019, 2021, 2022],
        'colors': ['Blue', 'Green', 'Yellow'],
    },
    'RAV4': {
        'types': ['SUV'],
        'years': [2013, 2014, 2018, 2019, 2021, 2022],
        'colors': ['White', 'Gray', 'Black'],
    },
    'Civic': {
        'types': ['Sedan', 'Hatch'],
        'years': [2013, 2015, 2016, 2018, 2020, 2022],
        'colors': ['Red', 'Blue', 'White'],
    },
    'Mustang': {
        'types': ['Sport'],
        'years': [2014, 2015, 2017, 2020, 2021, 2022],
        'colors': ['Red', 'Yellow', 'Blue'],
    },
    'Camaro': {
        'types': ['Sport'],
        'years': [2013, 2015, 2017, 2020, 2021, 2022],
        'colors': ['Yellow', 'Black', 'White'],
    },
    'X5': {
        'types': ['SUV'],
        'years': [2014, 2015, 2017, 2018, 2020, 2022],
        'colors': ['White', 'Black', 'Blue'],
    },
    'i8': {
        'types': ['Sport'],
        'years': [2014, 2015, 2016, 2017, 2019, 2021, 2022],
        'colors': ['Blue', 'Black', 'Red'],
    },
    'A3': {
        'types': ['Hatch', 'Sedan'],
        'years': [2014, 2016, 2017, 2018, 2020, 2021, 2022],
        'colors': ['Silver', 'Black', 'Red'],
    },
    'A6': {
        'types': ['Sedan'],
        'years': [2013, 2014, 2016, 2017, 2019, 2021, 2022],
        'colors': ['Blue', 'Black', 'Gray'],
    },
    'Q5': {
        'types': ['SUV'],
        'years': [2014, 2015, 2016, 2018, 2019, 2020, 2022],
        'colors': ['White', 'Gray', 'Black'],
    },
}

def show_options(options_list):
    """Display a list of options with index numbers."""
    for i, option in enumerate(options_list, start=1):
        if isinstance(option, int):  # Check if the option is an integer
            print(f"| {i}. {str(option).ljust(34)}|")
        else:
            print(f"| {i}. {option.ljust(34)}|")  # Display the number and formatted option

def get_user_choice(message, options):
    """Show options and get the user's choice, validating the input."""
    while True:
        print("\n+" + "-" * 38 + "+")  # Top line of the box
        print("|" + "Rapidopolis Cars".center(38) + "|")  # Shop name centered
        print("+" + "-" * 38 + "+")  # Bottom line of the box
        print("|" + message.center(38) + "|")  # Centered message
        show_options(options)  # Display available options
        print("+" + "-" * 38 + "+")  # Bottom line of the box
        choice = input("Enter the number of your choice: ")  # Ask user for input
        print("+" + "-" * 38 + "+")  # Bottom line of the box
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]  # Return the user's choice
        else:
            print("Invalid choice. Please try again.\n")  # Error message for invalid choice

def find_car(car_type, year, color):
    """Find cars that match the user's specifications (type, year, color)."""
    perfect_matches = []  # List to store models that perfectly match the criteria
    for model in cars:
        car = cars[model]
        if car_type in car['types'] and year in car['years'] and color in car['colors']:
            perfect_matches.append(model)  # Add model to the list of perfect matches

    if perfect_matches:
        total_perfect_matches = len(perfect_matches)
        print("\nPerfect matches:")
        for i, model in enumerate(perfect_matches, start=1):
            if i > 3:
                break  # Show a maximum of three perfect matches
            probability = 1 / total_perfect_matches * 100
            print(f"The probability of finding a {model} of type {car_type}, year {year}, in {color} is {probability:.2f}%.")
    else:
        print("Sorry, we don't have cars that match all of your specifications.")

# Create sets with all available car types, years, and colors
car_types = set(car_type for model in cars for car_type in cars[model]['types'])
car_years = set(year for model in cars for year in cars[model]['years'])
car_colors = set(color for model in cars for color in cars[model]['colors'])

# Main program loop
while True:
    # Ask user for their desired car specifications
    user_type = get_user_choice("Select the car type", sorted(list(car_types)))
    user_year = get_user_choice("Select the car year", sorted(list(car_years)))
    user_color = get_user_choice("Select the car color", sorted(list(car_colors)))

    # Find and display matching cars
    find_car(user_type, user_year, user_color)

    # Ask if the user wants to restart the search or exit
    final_choice = get_user_choice("Restart search or exit?", ['Restart search', 'Exit'])
    if final_choice == 'Exit':
        break
