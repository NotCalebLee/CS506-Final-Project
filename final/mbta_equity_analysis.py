import os
import time
import requests
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

TARGET_ROUTES = ['14', '15', '17', '22', '23', '24', '26', '28', '29', '31', '33', '42', '44', '45', '111']

print("--- Step 1: Fetching MBTA Bus Routes via V3 API ---")
routes_url = "https://api-v3.mbta.com/routes?filter[type]=3"
res = requests.get(routes_url)

if res.status_code != 200:
    raise ConnectionError(f"API request failed with status code: {res.status_code}")

routes_data = res.json()['data']

routes_list = []
for r in routes_data:
    r_id = r['id']
    attrs = r['attributes']
    routes_list.append({
        'route_id': r_id,
        'short_name': attrs.get('short_name', r_id),
        'long_name': attrs.get('long_name', ''),
        'direction_names': " / ".join(attrs.get('direction_names', [])),
        'is_target_equity': r_id in TARGET_ROUTES
    })

df_routes = pd.DataFrame(routes_list)
print(f"Retrieved {len(df_routes)} total bus routes.")

print("\n--- Step 2: Querying Stop Counts (Batched & Rate-Limited) ---")
stop_counts = []
for r_id in df_routes['route_id']:
    stops_url = f"https://api-v3.mbta.com/stops?filter[route]={r_id}"
    stops_res = requests.get(stops_url)
    

    if stops_res.status_code == 429:
        print("Rate limit reached. Pausing for 5 seconds...")
        time.sleep(5)
        stops_res = requests.get(stops_url)
        
    if stops_res.status_code == 200:
        stop_counts.append(len(stops_res.json()['data']))
    else:
        stop_counts.append(None)
    

    time.sleep(0.25)

df_routes['total_stops'] = stop_counts


df_priority = df_routes[df_routes['is_target_equity']].copy()
df_priority.drop(columns=['is_target_equity'], inplace=True)


priority_csv_path = os.path.join(script_dir, 'priority_equity_routes_data.csv')
df_priority.to_csv(priority_csv_path, index=False)
print(f"\n[Saved] Priority route data saved to: {priority_csv_path}")


summary_df = df_routes.groupby('is_target_equity').agg(
    total_routes=('route_id', 'count'),
    avg_stops_per_route=('total_stops', 'mean'),
    min_stops=('total_stops', 'min'),
    max_stops=('total_stops', 'max')
).reset_index()

summary_df['category'] = summary_df['is_target_equity'].map({
    True: '15 Priority Equity Corridors',
    False: 'Other Citywide Bus Routes'
})

summary_df = summary_df[['category', 'total_routes', 'avg_stops_per_route', 'min_stops', 'max_stops']]
summary_df['avg_stops_per_route'] = summary_df['avg_stops_per_route'].round(2)


summary_csv_path = os.path.join(script_dir, 'equity_vs_system_summary.csv')
summary_df.to_csv(summary_csv_path, index=False)
print(f"[Saved] Comparative summary data saved to: {summary_csv_path}")

print("\n--- Priority Equity Routes Dataset Preview ---")
print(df_priority[['route_id', 'long_name', 'total_stops']].to_string(index=False))

print("\n--- Aggregated Summary Table ---")
print(summary_df.to_string(index=False))