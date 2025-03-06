"""
Author: Logan Bellamy
Date: 03/06/2025

Warning: If you are using GitHub for version control DO NOT push the input file. It is too big.
         DO NOT push up the output files either. They are also too big. Very inconvenient. Working on a solution.

This is a super inefficient CSV sorting algorithm.
This was created specifically to handle the BCICIV competition files in CSV format.
There is probably a package that could be used to speed this up.
Maybe hashing could help organize this
...but you should definitely expect worst case from any sorting algorithm you might use.
"""


'''
Setup
'''
# Imports
import csv
import os
import time

# Track execution time
start_time = time.time()

# Array of expected gestures (information gathered from observing the input CSV file)
expected_gesture = ["tongue", "foot", "right", "left"]


'''
Function Creation
'''
# Creates directories and CSV files (based on expected format)
def datahandler(i, gesture, row_info):
    base_dir = "Output_Data"

    # Full path for the gesture directory
    gesture_dir = os.path.join(base_dir, gesture)

    # Create gesture directory if it does not exist
    if not os.path.exists(gesture_dir):
        os.makedirs(gesture_dir)

    # Full path for the patient directory
    patient_dir = os.path.join(gesture_dir, f"Patient_{i}")

    # Check if the patient directory exists, if so, raise an error
    if os.path.exists(patient_dir):
        raise FileExistsError(f"Patient directory '{patient_dir}' already exists!")

    # Create the patient directory
    os.makedirs(patient_dir)

    # Path for the CSV file
    csv_path = os.path.join(patient_dir, f"Patient_{i}.csv")

    # Write the row_info to the CSV file
    with open(csv_path, 'w') as csvfile:
        csvfile.write(', '.join(map(str, list(row_info))) + '\n')


'''
Main
'''
# Open the CSV file for reading
with open("C:\\Users\\scott\\OneDrive\\Documents\\GitHub\\myo_ecn\\examples\\classification\\Input_Data\\BCICIV_2a_all_patients.csv",
          'r') as file:

    # Set up readers
    csvreader = csv.reader(file)
    fields = next(csvreader) # Skips header row (can be used if you need to see the header)

    # Go through the patient numbers
    for i in range(1,10):

        # Convert i to string for checking
        str_num = str(i)

        # Go through the gestures
        for x in expected_gesture:

            # Use this to store the raw data
            row_info = []

            # Track gesture time
            gesture_start_time = time.time()

            # Reset the file cursor and reinitialize csvreader
            file.seek(0)
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header row again

            # Go through each row
            for row in csvreader:

                # Check key information (needed to organize data into expected format)
                if row[0] == str_num and row[2] == x:

                    # Get the info we need
                    row_info.append(row[4:22])

            # Creates the directories and CSV files based on expected format
            if row_info:
                datahandler(str_num, x, row_info)
            else:
                print(f"No {x} data found for patient {i}")

    # Notify completion and show execution time
    total_time = time.time() - start_time
    print(f"CSV file has been sorted. Please see Output_Data. Total time: {total_time:.4f} seconds.")