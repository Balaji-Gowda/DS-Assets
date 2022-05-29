import pandas as pd
import streamlit as st
import sklearn as sl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

st.header("Machine Learning Application")
st.subheader("Predicting the profit with different Variables")
df=pd.read_csv("C:\\Users\\894524\\Downloads\\1000_Companies.csv")
# print(df.head())
# print(df.columns)
# print(df.dtypes)
cols=list(df.drop(["Profit","State"],axis=1).columns)
# print(cols)
m=st.multiselect("columns:",["R&D_Spend","Administration","Marketing_Spend"])
# x=df[cols]
# s=st.selectbox
x=pd.DataFrame(df["Administration"])

# x=pd.DataFrame(df.iloc[:1].values)
y=df["Profit"]

# print((x,y))

params=dict()
ratio=st.slider('test_size',0.1,0.35)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=ratio,random_state=1234)
# st.write(x_train.shape,y_train.shape)


ln=LinearRegression()
mod=ln.fit(x_train,y_train)
pred=mod.predict(x_test)

st.write("accuracy of model is",round((r2_score(y_test,pred))*100,2),'%%')
st.write("Error Score: ",mean_absolute_error(y_test,pred))
st.write("Mean sqrd Error: ",mean_squared_error(y_test,pred))
st.dataframe({"Actual":y_test,"Predicted":pred})
