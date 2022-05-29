import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns
import sklearn as sl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

st.markdown("<h1 style='text-align:center;color:steelblue;background-color:salmon '>INSURANCE PREDICTION MODEL</h1>",unsafe_allow_html=True)
df=pd.read_csv("C:\\Documents\\Pandas\\Projects\\pandas\\Top Mentor\ML\\Insurance.csv")
df=df.drop("id",axis=1)
st.write((df.head()))
st.write(df.shape)
st.write(df.isnull().sum())
df.dropna(inplace=True)
st.write(df.shape)
data=df.copy()
df["Vehicle_Age"]=df.Vehicle_Age.map({"< 1 Year":0,"1-2 Year":1,"> 2 Years":2,})

df["Gender"]=df.Gender.map({"Male":1,"Female":0})

df["Vehicle_Damage"]=df.Vehicle_Damage.map({"Yes":1,"No":0})
plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),annot=True)
st.pyplot()
st.text('"Age","Previously_Insured","Vehicle_Age","Vehicle_Damage","Policy_Sales_Channel" \n are highly correlated with \"Response\"')
# for i in ["Age","Previously_Insured","Vehicle_Age","Vehicle_Damage","Policy_Sales_Channel"]:
#     sns.boxplot(i,data=df)
#     plt.show()
#     st.pyplot()
st.text("no outliers")

st.subheader("# Feature Scaling")
min=MinMaxScaler()
st.write(df.head())
df[df.columns]=min.fit_transform(df)
st.write(df.head())

st.subheader("# Train Test Split")
x=df[["Age","Previously_Insured","Vehicle_Age","Vehicle_Damage","Policy_Sales_Channel"]]
y=df["Response"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1234)
st.write(x_train,x_train.shape,y_train,x_test,x_test.shape,y_test)

st.subheader("# Modelling")
log=LogisticRegression()
mod=log.fit(x_train,y_train)
st.success(mod.score(x_train,y_train))
# st.text(confusion_matrix())


st.subheader("# Prediction")
pred=mod.predict(x_test)
st.success(accuracy_score(y_test,pred))
st.text(confusion_matrix(y_test,pred))

st.subheader("# Testing")
actual_pred=mod.predict(df[["Age","Previously_Insured","Vehicle_Age","Vehicle_Damage","Policy_Sales_Channel"]])
st.success(accuracy_score(df["Response"],actual_pred))
st.text(confusion_matrix(df["Response"],actual_pred))

