# Import the necessary libraries
import mysql.connector
import pandas as pd

# Set the path where all files are located
#path = "C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau"

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\telemetry_data.csv")
# Clean up column names
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('-', '_')
df.columns = df.columns.str.replace('[^a-zA-Z0-9_]', '')


# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MM_iRacing"
)

# Create a cursor object
cursor = connection.cursor()

# Define the table name
table_name = "telemetry_data"

# Iterate over each row in the DataFrame
for i, row in df.iterrows():
    # Generate the SQL query for this particular row
    query = f"""INSERT INTO {table_name} ({', '.join(row.index)}) VALUES ({', '.join("'" + str(x).replace("'", "''") + "'" for x in row.values)})"""
    # Print the query for debugging
    print(query)
    # Execute the query
    cursor.execute(query)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
