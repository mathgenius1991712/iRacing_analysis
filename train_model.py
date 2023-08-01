import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from joblib import dump

# Load data from CSV files into DataFrames
telemetry_data = pd.read_csv('C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\processed_telemetry_data.csv')
setup_data = pd.read_csv('C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\processed_setup_data.csv')
runs = pd.read_csv('C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\processed_runs.csv')
drivers = pd.read_csv('C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\processed_drivers.csv')

# Convert 'run_id' and 'driver_id' to int if they exist and are of float type
for df in [telemetry_data, setup_data, runs, drivers]:
    if 'run_id' in df.columns and df['run_id'].dtype == 'float64':
        df['run_id'] = df['run_id'].fillna(-1).astype(int)
    if 'driver_id' in df.columns and df['driver_id'].dtype == 'float64':
        df['driver_id'] = df['driver_id'].fillna(-1).astype(int)

# Merge the data into a single DataFrame
df = telemetry_data
for other_df, id_col in zip([setup_data, runs, drivers], ['run_id', 'run_id', 'driver_id']):
    if id_col in df.columns and id_col in other_df.columns:
        df = pd.merge(df, other_df, on=id_col)

# Drop rows with missing target
df = df.dropna(subset=['RF HS reb slope'])

# Split the data into input variables (X) and the target variable (y)
X = df.drop('RF HS reb slope', axis=1)
y = df['RF HS reb slope']

# Handle non-numeric columns and NaN values
for col in X.columns:
    if np.issubdtype(X[col].dtype, np.number):
        X[col] = X[col].astype(float)
        X[col].fillna(X[col].mean(), inplace=True)
    else:
        X = X.drop(col, axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to a file
dump(model, 'shock_settings_predictor.joblib')

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate and print the root mean squared error (RMSE) of our predictions
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")