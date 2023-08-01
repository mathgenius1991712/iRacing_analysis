import pandas as pd
from bs4 import BeautifulSoup
import re
import os

def parse_setup_html(file_path):
    # Extract driver name from the directory structure
    driver_name = os.path.basename(os.path.dirname(file_path))

    # Open and parse the HTML file
    with open(file_path, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')

    # Extract the session info
    session_info = soup.h2.text.split('\n')[1].strip()

    # Extract car and setup name from the session info
    car_name = re.findall(r'(.*?) setup:', session_info)[0]
    setup_name = re.findall(r'setup: (.*?)$', session_info)[0]

    # Extract track name from the setup name
    track_name = setup_name.split("\\")[0]

    # Initialize an empty dictionary to hold the parsed data
    parsed_data = {}

    # Loop through each line in the body
    for line in soup.body.stripped_strings:
        # Split the line into a label and a value
        parts = line.split(':')
        if len(parts) == 2:
            label, value = parts

            # Remove any leading/trailing whitespace from the label and value
            label = label.strip()
            value = value.strip()

            # Add the label and value to the dictionary
            parsed_data[label] = value

    # Add car, track, and driver name to the parameters
    parsed_data['car_name'] = car_name
    parsed_data['track_name'] = track_name
    parsed_data['driver_name'] = driver_name

    return parsed_data

def save_to_csv(data, csv_file_path):
    # Create a DataFrame from the parsed data
    setup_data = pd.DataFrame(data, index=[0])

    # Save the DataFrame to a CSV file
    setup_data.to_csv(csv_file_path, index=False)


# Usage:
file_path = 'P2W_23S3_Richmond_RaceV2_4th_Gear-Wshocks.htm'  # replace with your file path
csv_file_path = 'P2W_23S3_Richmond_RaceV2_4th_Gear-Wshocks_1.csv'  # replace with your desired CSV file path

data = parse_setup_html(file_path)
save_to_csv(data, csv_file_path)
