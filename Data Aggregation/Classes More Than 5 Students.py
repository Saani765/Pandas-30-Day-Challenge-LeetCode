import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    c=courses.groupby('class')['student'].count().reset_index()
    df=c[c['student']>=5][["class"]]
    return df