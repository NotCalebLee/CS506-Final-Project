import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))


priority_csv = os.path.join(script_dir, 'priority_equity_routes_data.csv')
accuracy_csv = os.path.join(script_dir, 'rapid_transit_and_bus_prediction_accuracy_data.csv')

df_priority = pd.read_csv(priority_csv)


if os.path.exists(accuracy_csv):
    df_accuracy = pd.read_csv(accuracy_csv)
    df_priority['route_id'] = df_priority['route_id'].astype(str)
    
    route_col = next((c for c in ['route_id', 'route', 'gtfs_route_id', 'Route'] if c in df_accuracy.columns), None)
    
    if route_col:
        df_accuracy[route_col] = df_accuracy[route_col].astype(str)
        df_merged = pd.merge(df_priority, df_accuracy, left_on='route_id', right_on=route_col, how='left')
        
        master_path = os.path.join(script_dir, 'master_bus_equity_dataset.csv')
        df_merged.to_csv(master_path, index=False)
        print(f"[Success] Created master dataset: {master_path}")
    else:
        print("Could not locate route column in prediction accuracy CSV.")
else:
    master_path = os.path.join(script_dir, 'master_bus_equity_dataset.csv')
    df_priority.to_csv(master_path, index=False)
    print(f"[Notice] Historical accuracy file missing; saved priority API data to: {master_path}")