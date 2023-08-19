import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views['author_id']==views['viewer_id']]
    udf=df['author_id'].unique()
    udf=sorted(udf)
    result=pd.DataFrame({'id': udf})
    return result