import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich=store[store['amount']>500]
    n=rich['customer_id'].nunique()
    df=pd.DataFrame({'rich_count':[n]})
    return df
