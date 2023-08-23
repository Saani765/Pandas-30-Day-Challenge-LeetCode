import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees
        .rename(columns={'event_day':'day'})
        .assign(total_time=employees['out_time'] - employees['in_time'])
        .groupby(['day', 'emp_id'])['total_time'].sum()
        .reset_index()
        )