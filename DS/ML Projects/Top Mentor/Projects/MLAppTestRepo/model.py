import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score


df=pd.read_csv("Master_Table_Updated_new.csv")
# st.write(df.head())
print(df.columns)
xx=df[['loan_amount','balance']]

#Finding number of clusters using Elbow Method
wcss=[]
for i in range(1,15):
    k1=KMeans(n_clusters=i)
    m1=k1.fit(xx)
    wcss.append(k1.inertia_)

#modelling
k2=KMeans(n_clusters=2)
m2=k2.fit(xx)
clusters=m2.predict(xx)

#accuracy score
# st.write("Accuracy Score",silhouette_score(xx,k2.labels_)*100)

DS_clustered=xx
DS_clustered.insert(0,"Account_id",df['account_id'])
DS_clustered['Cluster']=clusters


acc=st.number_input("Enter Account Number")
ln_amt=st.number_input("Enter Loan Amount")
bal=st.number_input("Enter Balance")
test_df=pd.DataFrame([{"Amount":ln_amt,"Balance":bal}])
st.write("Input Data")

st.write(test_df)
new_pred=m2.predict(test_df)
st.write("Detected Clusters: ",pd.DataFrame(clusters).nunique()[0],(list(pd.DataFrame(clusters)[0].unique())))
st.write("Client ID",int(acc)," falls into cluster: ","'",(new_pred[0]),"'")
test_df.insert(0,"Account ID",acc)
# new_df=pd.concat([pd.DataFrame({"Account_ID":acc}),test_df,pd.DataFrame({"Predicted_Cluster":new_pred})])
test_df['Predicted Cluster']=new_pred
st.write("<h3>\nClustered Output:</h3>",unsafe_allow_html=True)
st.write(test_df)





