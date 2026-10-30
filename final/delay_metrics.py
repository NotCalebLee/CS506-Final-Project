import os
import zipfile
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
zip_file = os.path.join(script_dir, "MBTA_Bus_Arrival_Departure_Times_2024.zip")

TARGET_ROUTES = ['14', '15', '17', '22', '23', '24', '26', '28', '29', '31', '33', '42', '44', '45', '111']

if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as z:
        print("Files in archive:", z.namelist()[:5])
        csv_name = [f for f in z.namelist() if f.endswith('.csv')][0]
        df_perf = pd.read_csv(z.open(csv_name))
        df_equity_perf = df_perf[df_perf['route_id'].astype(str).isin(TARGET_ROUTES)]
        print("Filtered performance rows:", len(df_equity_perf))