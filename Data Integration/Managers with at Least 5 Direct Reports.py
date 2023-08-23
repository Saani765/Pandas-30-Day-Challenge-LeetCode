import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    required_managers = (
        employee
        .groupby('managerId', as_index=False)
        .agg(reporting=('id', 'count'))
        .query('reporting >= 5')
    )['managerId']

    return employee[employee['id'].isin(required_managers)][['name']]