import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].str.capitalize()
    df=users.sort_values(by='user_id',ascending=True)
    return df