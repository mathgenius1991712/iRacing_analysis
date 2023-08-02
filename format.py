import os
import setup_converter_json
telemetry_data_path = "./telemetry_data"
#convert setup htm files to csv files 
def format():
  for root, driver_dirs, files_level_1 in os.walk(telemetry_data_path):
    for driver_dir in driver_dirs:
      driver_dir = root + '/'+ driver_dir
      for root_driver_dir, season_dirs, files_level_2 in os.walk(driver_dir):
        for season_dir in season_dirs:
          season_dir = driver_dir + '/'+  season_dir
          for root_season_dir, track_dirs, files_level_3 in os.walk(season_dir):
            for track_dir in track_dirs:
              track_dir = season_dir + '/'+  track_dir
              for file in os.listdir(track_dir):
                if file.endswith(".htm"):
                  file = track_dir + '/' + file
                  setup_converter_json.setup_converter_json(file)
  


