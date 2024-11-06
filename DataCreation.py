import random as rd
import pandas as pd
data1=[rd.randint(0,24) for i in range(200)]
data2=[rd.randint(30,85) for j in range(200)]
data3={
        "Study_Time":data1,
        "Exam_Score":data2
      }
dataframe=pd.DataFrame(data3)
dataframe.to_csv("StudyTimeData.csv",index=False)