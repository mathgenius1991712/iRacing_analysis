import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
import re

# Create a file dialog to select the telemetry data file
root = tk.Tk()
root.withdraw()  # Hide the small tk window

# Open the file dialog
file_path = filedialog.askopenfilename()

# Load the data
df = pd.read_csv(file_path, skiprows=14, dtype=str)  # Skip the first 14 rows and read all data as string

# Remove units row (if any)
df = df[~df['Time'].str.contains('s')]

# Convert all data to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Select only the variables we're interested in
variables_of_interest = ['LFshockVel', 'RFshockVel', 'LRshockVel', 'RRshockVel',
                         'LFshockDefl', 'RFshockDefl', 'LRshockDefl', 'RRshockDefl',
                         'LFrideHeight', 'RFrideHeight', 'LRrideHeight', 'RRrideHeight',
                         'LFtempL', 'LFtempM', 'LFtempR',
                         'RFtempL', 'RFtempM', 'RFtempR',
                         'LRtempL', 'LRtempM', 'LRtempR',
                         'RRtempL', 'RRtempM', 'RRtempR',
                         'LapLastLapTime', 'VelocityX', 'VelocityY', 'VelocityZ']

df = df[variables_of_interest]

# Save the correlation matrix to a CSV file.
corr_matrix = df.corr()
df.corr().to_csv(r'C:\Users\Elfrost\Documents\NETproject\iRacing_Engineer\correlation_matrix.csv')

# The following code is commented out to prevent generating a plot for each variable.
# If you want to generate these plots, simply remove the triple quotes before and after this section of code.

'''
# Plot each variable over time
for var in variables_of_interest:
    plt.figure(figsize=(15, 5))
    plt.plot(df[var])
    plt.title(var + ' over time')
    plt.xlabel('Time')
    plt.ylabel(var)
    plt.show()
'''
