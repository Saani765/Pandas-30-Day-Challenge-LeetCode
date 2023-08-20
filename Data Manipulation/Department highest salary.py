import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
        if employee.empty or department.empty:
            return pd.DataFrame(columns=['Department','Employee', 'Salary'])
        merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
        highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
        highest_salary_df = highest_salary_df.reset_index(drop=True)
    
    
        result_df = highest_salary_df[['name_department', 'name_employee', 'salary']]
    
    
        result_df.columns = ['Department','Employee', 'Salary']
    
        return result_df