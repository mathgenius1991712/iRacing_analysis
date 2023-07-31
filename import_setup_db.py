from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy.sql import insert
import os

# Create a connection to the database
engine = create_engine('mysql+pymysql://ezwebcjt_telm:X#KB}sBU;I]F@207.174.213.166/ezwebcjt_ez1')

metadata = MetaData()

# Reference the table
car_setup = Table('car_setup', metadata, autoload_with=engine)

# Extract driver name from the directory structure
file_path = 'C:/Users/Elfrost/Documents/NETproject/iRacing_Engineer/telemetry_data/Nicolas Moreau/P2W_23S3_Richmond_RaceV2_4th_Gear-Wshocks.txt'
driver_name = os.path.basename(os.path.dirname(file_path))

# Prepare the data for insertion
data = [
    {
        'setup': 'Richmond\\23S3\\P2W_23S3_Richmond_RaceV2_4th_Gear-Wshocks',
        'track': 'richmond',
        'car': 'stockcars chevycamarozl12022',
        'driver': driver_name,
        'lf_cold_pressure': 10.0,
        'lr_cold_pressure': 14.0,
        'rf_cold_pressure': 28.0,
        'rr_cold_pressure': 28.0,
        'nose_weight': 50.8,
        'cross_weight': 59.0,
        'steering_pinion': 2.87,
        'steering_offset': 0.0,
        'front_mc': '15/16',
        'rear_mc': '27/32',
        'front_brake_bias': 39.2,
        'lf_corner_weight': 824,
        'lf_ride_height': 1.726,
        'lf_shock_collar_offset': 4.188,
        'lf_spring_rate': 3900,
        'lf_ls_compression': 2,
        'lf_hs_compression': 2,
        'lf_hs_comp_slope': 3,
        'lf_ls_rebound': 6,
        'lf_hs_rebound': 1,
        'lf_hs_reb_slope': 3,
        'lf_camber': 4.4,
        'lf_caster': 10.9,
        'lf_toe_in': '0/32',
        'lr_corner_weight': 1115,
        'lr_shock_collar_offset': 5.844,
        'lr_spring_rate': 750,
        'lr_ls_compression': 4,
        'lr_hs_compression': 5,
        'lr_hs_comp_slope': 3,
        'lr_ls_rebound': 5,
        'lr_hs_rebound': 5,
        'lr_hs_reb_slope': 3,
        'lr_camber': 3.1,
        'lr_toe_in': '0/32',
        'front_arb_diameter': 2.0,
        'front_arb_arm': 'P5 (stiff)',
        'front_arb_preload': -15.6,
        'front_arb_attach': 'Yes',
        'rf_corner_weight': 1001,
        'rf_ride_height': 2.169,
        'rf_shock_collar_offset': 3.125,
        'rf_spring_rate': 3900,
        'rf_ls_compression': 1,
        'rf_hs_compression': 2,
        'rf_hs_comp_slope': 3,
        'rf_ls_rebound': 6,
        'rf_hs_rebound': 1,
        'rf_hs_reb_slope': 3,
        'rf_camber': -4.4,
        'rf_caster': 10.9,
        'rf_toe_in': '0/32',
        'rr_corner_weight': 648,
        'rr_ride_height': 1.899,
        'rr_shock_collar_offset': 4.0,
        'rr_spring_rate': 4600,
        'rr_ls_compression': 4,
        'rr_hs_compression': 5,
        'rr_hs_comp_slope': 3,
        'rr_ls_rebound': 5,
        'rr_hs_rebound': 4,
        'rr_hs_reb_slope': 3,
        'rr_camber': -3.1,
        'rr_toe_in': '0/32',
        'gear_ratio': 4.691,
        'diff_preload': 0.0,
        'rear_arb_diameter': 2.0,
        'rear_arb_arm': 'P5 (stiff)',
        'rear_arb_preload': 1.2,
        'rear_arb_attach': 'Yes',
        'notes': '',
    },
]

# Insert the data and commit the transaction
with engine.connect() as connection:
    result = connection.execute(insert(car_setup), data)
    connection.commit()
