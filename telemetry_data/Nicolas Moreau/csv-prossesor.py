import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def preprocess_and_save(filename):
    full_path = 'C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\' + filename
    df = pd.read_csv(full_path, low_memory=False)  # Add low_memory=False here
    
    # Drop columns that are entirely NaN
    df = df.dropna(axis=1, how='all')
    
    # Numeric columns are imputed with the mean
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    imp_num = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[num_cols] = imp_num.fit_transform(df[num_cols])
    
    # Non-numeric columns are converted to string and then imputed with the most frequent value
    non_num_cols = df.select_dtypes(exclude=np.number).columns.tolist()
    df[non_num_cols] = df[non_num_cols].astype(str)
    imp_non_num = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    df[non_num_cols] = imp_non_num.fit_transform(df[non_num_cols])
    
    df.to_csv('C:\\Users\\Elfrost\\Documents\\NETproject\\iRacing_Engineer\\telemetry_data\\Nicolas Moreau\\processed_' + filename, index=False)

preprocess_and_save('drivers.csv')
preprocess_and_save('runs.csv')
preprocess_and_save('setup_data.csv')
preprocess_and_save('telemetry_data.csv')
