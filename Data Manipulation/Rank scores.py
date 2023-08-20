import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    result_df = scores.drop('id',axis=1).sort_values(by='score', ascending=False)
    
    return result_df