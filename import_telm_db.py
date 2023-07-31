import os
from sqlalchemy import create_engine
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root widget
root = tk.Tk()
# Hide the main window
root.withdraw()

# Open a file selection dialog and get the file path
file_path = filedialog.askopenfilename()

# Extract the driver's name from the file path
driver_name = os.path.dirname(file_path).split('/')[-1]

# Read the telemetry data
telemetry_data = pd.read_csv(file_path)

# Add the driver's name to the DataFrame
telemetry_data['driver_name'] = driver_name

# Manually set the setup ID for now
setup_id = 5

# Add the setup ID to the DataFrame
telemetry_data['setup_id'] = setup_id

# Import the necessary libraries
engine = create_engine('mysql+pymysql://ezwebcjt_telm:X#KB}sBU;I]F@207.174.213.166/ezwebcjt_ez1')

# Insert the data into the database
telemetry_data.to_sql('lap_data', con=engine, if_exists='append', index=False)
