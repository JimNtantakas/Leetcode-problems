import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']==101]








data = {'student_id': [101, 102, 103],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [20, 22, 21]}
students=pd.DataFrame(data)
result_df=selectData(students)
print(result_df)