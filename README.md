# Rapidopolis Car Finder

This Python script is a simple program that helps users find cars based on specific criteria such as car type, year, and color. The program allows users to interactively select options and provides matching results from a predefined car database. It also calculates the probability of finding the exact car based on the available matches.

## Features

- **Car Database**: A built-in dictionary (`cars`) contains a variety of car models with attributes such as `types`, `years`, and `colors`.
- **User Interaction**: The program prompts users to select a car type, year, and color from available options, and provides feedback on whether the selection matches any cars in the database.
- **Matching Results**: The program looks for "perfect matches" based on the user’s selection, showing up to three results with the probability of finding each match.
- **Loop for Multiple Searches**: After finding a result, the user can choose to either restart the search or exit the program.

## How it Works

1. **Display Options**: The script displays lists of available car types, years, and colors.
2. **User Selection**: The user selects the desired specifications for a car by choosing from numbered lists.
3. **Search for Matches**: The program searches the `cars` database for cars that match the user’s chosen type, year, and color.
4. **Display Results**: If matches are found, it shows up to three matching cars along with the probability of finding each. If no match is found, the program informs the user.
5. **Restart or Exit**: After showing the results, the program asks if the user wants to restart the search or exit.

## Functions

- `show_options(options_list)`: Displays a list of options for the user to choose from, with formatting.
- `get_user_choice(message, options)`: Prompts the user to make a selection from the displayed options and returns the choice.
- `find_car(car_type, year, color)`: Finds cars in the database that match the selected type, year, and color, and displays the matching results along with probabilities.

## Car Database

The car database (`cars`) is a dictionary that contains information about various car models. Each model has the following attributes:

- `types`: The available body types for the car (e.g., `Sedan`, `SUV`, `Sport`, etc.).
- `years`: The production years available in the database.
- `colors`: The available colors for each car model.

Example entry from the database:

```python
'Corolla': {
    'types': ['Sedan', 'Hatch'],
    'years': [2014, 2015, 2017, 2020, 2021, 2022],
    'colors': ['Silver', 'Black', 'Red'],
}




python car_finder.py





+--------------------------------------+
|         Rapidopolis Cars             |
+--------------------------------------+
|      Select the car type             |
| 1. Sedan                             |
| 2. SUV                               |
| 3. Hatch                             |
| 4. Sport                             |
+--------------------------------------+
Enter the number of your choice: 2
+--------------------------------------+
| The probability of finding a RAV4 of type SUV, year 2019 in White is 33.33%. |





### Explanation:
- The `README.md` includes a **description of the program** and how it works.
- The **features**, **how it works**, and **functions** sections give a high-level understanding of what each part does.
- There’s an **example entry** of the car database to show how the data is structured.
- **Running the Program** provides a simple way to execute the script.
- The **example output** gives a preview of what the program looks like when run.
