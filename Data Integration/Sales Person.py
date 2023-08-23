import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge DataFrames to find salespersons with orders related to "RED" companies
    merged_df = pd.merge(orders, company, on='com_id', how='inner')
    red_sales_ids = merged_df[merged_df['name'] == 'RED']['sales_id'].unique()
    
    # Filter salespersons who do not have orders related to "RED" companies
    result_df = sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]
    return result_df