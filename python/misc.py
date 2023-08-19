import pandas as pd

def label_end_timestamp(df_loc='data/labels.csv'):
    df = pd.read_csv(df_loc)
    df['end_timestamp'] = df['timestamp'] + 5
    df.to_csv(df_loc, index=False)