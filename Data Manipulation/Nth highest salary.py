import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df=employee['salary'].drop_duplicates()
    sorted_df=df.sort_values(ascending=False)
    if(N>len(sorted_df)):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    nth=sorted_df.iloc[N-1]
    return pd.DataFrame({'Nth Highest Salary':[nth]})
