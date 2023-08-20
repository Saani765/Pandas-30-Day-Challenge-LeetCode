import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee['salary'].drop_duplicates()
    sorted_df=df.sort_values(ascending=False)
    if(len(sorted_df)<2):
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else :
        return pd.DataFrame({'SecondHighestSalary' :[sorted_df.iloc[1]]})

