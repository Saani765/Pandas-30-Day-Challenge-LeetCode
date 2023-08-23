import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
  groups = daily_sales.groupby(['date_id', 'make_name'])
  df = groups.agg({
    'lead_id': pd.Series.nunique,
    'partner_id': pd.Series.nunique
  }).reset_index()
  return df.rename(columns={
    'lead_id': 'unique_leads',
    'partner_id': 'unique_partners'
  })