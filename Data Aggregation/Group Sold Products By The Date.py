import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    acts = activities.groupby('sell_date')['product'].apply(lambda x: ','.join(sorted(x.unique()))).reset_index()
    acts['num_sold'] = acts['product'].apply(lambda x: len(x.split(',')))
    acts = acts.rename(columns={'product': 'products'}).sort_values(by=['sell_date'], ascending=True)
    return acts[['sell_date', 'num_sold', 'products']]