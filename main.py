import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel

data=pd.read_csv("StudyTimeData.csv")

def gradient_descent(w_now,b_now,learning_rate,Data):
    w_gradient=0
    b_gradient=0
    total_summations=len(Data)
    for i in range(len(Data)):
        current_x = Data.iloc[i].Study_Time
        current_y = Data.iloc[i].Exam_Score
        w_gradient=(-2/total_summations) * current_x * (current_y -((w_now * current_x) - b_now))
        b_gradient = (-2 / total_summations) * (current_y - ((w_now * current_x) - b_now))
    w=w_now - (learning_rate * w_gradient)
    b=b_now - (learning_rate * b_gradient)
    return w,b
weight=0
bias=0
learn_rate=0.01
epochs=10000
for j in range(epochs):
    weight,bias=gradient_descent(weight,bias,learn_rate,data)
print(f"Optimal weight={weight} , bias={bias}")
plt.style.use("ggplot")
plt.scatter(data.Study_Time,data.Exam_Score,color="r",marker="*")
plt.plot(list(range(10,20)),[((weight * x) + bias) for x in range(10,20)],color="g",marker="*",label="Predictive plot")
plt.xlabel("Student Study Time In Hours")
plt.ylabel("Exam Score")
plt.title("Predictive plot in a graph of Student's Exam Score versus Student's study time")
plt.legend()
plt.show()






