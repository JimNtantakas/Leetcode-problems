import pandas as pd

def createDataframe(student_data):
    df=pd.DataFrame(student_data,columns=['student_id','age'])    
    return df
    
    
"""
student_data = [
    [1, 20],
    [2, 22],
    [3, 21],
    [4, 23]
]
result_df = createDataframe(student_data)
print(result_df)
"""