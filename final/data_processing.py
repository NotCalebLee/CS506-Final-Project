import pandas as pd

df = pd.read_csv("rapid_transit_and_bus_prediction_accuracy_data.csv")


df_clean = df[df['num_predictions'] > 0].copy()


df_clean['accuracy_pct'] = (df_clean['num_accurate_predictions'] / df_clean['num_predictions']) * 100


df_clean['weekly'] = pd.to_datetime(df_clean['weekly'])
df_clean['year'] = df_clean['weekly'].dt.year


bus_predictions = df_clean[df_clean['mode'] == 'bus'].copy()
subway_predictions = df_clean[df_clean['mode'] == 'subway'].copy()


yearly_bus_accuracy = bus_predictions.groupby('year').agg(
    total_preds=('num_predictions', 'sum'),
    total_accurate=('num_accurate_predictions', 'sum')
).reset_index()

yearly_bus_accuracy['overall_accuracy_pct'] = (
    yearly_bus_accuracy['total_accurate'] / yearly_bus_accuracy['total_preds'] * 100
).round(2)

print(yearly_bus_accuracy)