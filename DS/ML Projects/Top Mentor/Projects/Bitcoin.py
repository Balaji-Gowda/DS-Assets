import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns
import sklearn as sl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
st.markdown("<h1 style='text-align:center;color:black;background-color:brown'>BITCOIN PRICE PREDICTION MODEL</h1>",unsafe_allow_html=True)
st.markdown("<title>A Meaningful Page Title</title>",unsafe_allow_html=True)
st.write('\n')
 # st.header("BitCoin Prediction")
df=pd.read_csv("C:\\Documents\\Pandas\\Projects\\pandas\\Top Mentor\ML\\bitcoin_dataset.csv")
print(df.head())
st.write(df.head())
st.text(df.shape)
df=df.dropna()
st.write(df.isnull().sum())
st.text(df.shape)
cols=["btc_estimated_transaction_volume_usd","btc_cost_per_transaction","btc_transaction_fees","btc_miners_revenue","btc_difficulty","btc_hash_rate",
"btc_trade_volume","btc_market_cap","btc_blocks_size","btc_n_unique_addresses","btc_n_transactions_total","btc_n_transactions_excluding_popular",
"btc_n_transactions_excluding_chains_longer_than_100","btc_market_price"]
df1=df[cols]
st.write(df1.head())
st.text(df1.shape)
# for col in cols:
#     sns.distplot(df1[col])
#     plt.show()
#     st.pyplot()

st.subheader("#1 Feature scaling")
rob=RobustScaler()
df1[df1.columns]=rob.fit_transform(df1)
st.write(df1.head())
st.write(df1.tail())
x=df1.drop("btc_market_price",axis=1)
y=df1["btc_market_price"]

st.subheader("#2 Train Test Split")
# st.write(train)
# st.write(test)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1234)
st.write(x_train,x_train.shape,y_train,x_test,x_test.shape,y_test)

st.subheader("#3 Modelling")
lin=LinearRegression()
mod = lin.fit(x_train,y_train)
st.success(mod.score(x_train,y_train))

st.subheader("#4 Testing")
pred=mod.predict(x_test)
st.success(r2_score(y_test,pred))

st.subheader("#5 Actual Prediction")
actual_pred=mod.predict(df1.drop("btc_market_price",axis=1))
st.success(r2_score(df1["btc_market_price"],actual_pred))

