import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # group by student_id', 'subject_name'; getting count for each subject
    examinations = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index() 
    # cross join
    students = students.merge(subjects, how='cross')
    # right join
    examinations = examinations.merge(students, on=['student_id', 'subject_name'],how='right')
    # filling null values with 0
    examinations = examinations.fillna(0)
    # sorting by 'student_id', 'subject_name'
    examinations = examinations.sort_values(['student_id', 'subject_name'])
    return examinations[['student_id', 'student_name', 'subject_name', 'attended_exams']]