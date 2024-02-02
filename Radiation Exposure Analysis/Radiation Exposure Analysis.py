import math

# Radiation levels in different locations
locations = {'City Centre': [22, 19, 20, 31, 28],
             'Industrial Zone': [35, 32, 30, 37, 40],
             'Residential District': [15, 12, 18, 20, 14],
             'Rural Outskirts': [9, 13, 16, 14, 7],
             'Downtown': [25, 18, 22, 21, 26]}

# Function to calculate the average radiation level
def calc_avg(rad_levels):
    return sum(rad_levels) / len(rad_levels)

# Function to calculate the standard deviation of radiation levels
def calc_std_dev(rad_levels):
    mean = calc_avg(rad_level)
    var = sum((i - mean) ** 2 for i in rad_levels) / len(rad_levels)
    std_dev = math.sqrt(var)
    return std_dev

# Iterate over locations and their radiation levels
for locations, rad_level in locations.items():
    print(f"Debug: Processing location {locations} with levels {rad_level}")
    avg = calc_avg(rad_level)
    std_dev = calc_std_dev(rad_level)
    print(f"{locations} Average Radiation Level: {avg:.2f}, Standard Deviation: {std_dev:.2f} \n")


# -----------------------------------------------
    

# Another method that allows continuous data input to calculate average radiation levels

measurements = []

# Debugging: Inform the user that the data entry process is starting

print("Begin entering new radiation levels. Type 'done' to finish.")

# This loop runs indefinitely until 'done' is entered
while True:
    level = input("Enter radiation level or 'done' to finish: ")
    if level.lower() == 'done':
        # Debugging: Confirm that the loop exit condition has been met
        print("Debug: Exiting input loop.")
        break
    try:
        # Convert the input to an integer and add to the measurements list
        new_level = int(level)
        measurements.append(new_level)
        # Debugging: Confirm that a new level has been added
        print(f"Debug: Added level {new_level}")
    except ValueError:
        # Debugging: Inform the user of an invalid input
        print("Invalid input. Please enter a valid number or 'done'.")


# Calculate and display the average of measurements entered by user
if measurements:
    average = sum(measurements) / len(measurements)
    print(f"New Measurements Average Radiation Level: {average}")
else:
    # Inform the user that no new measurements were entered
    print("Debug: No new measurements were entered.")