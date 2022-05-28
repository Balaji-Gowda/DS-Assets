import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from PIL import Image
# st.markdown("<h1 style='text-align:center;color:black;background-color:brown'>BITCOIN PRICE PREDICTION MODEL</h1>",unsafe_allow_html=True)
# st.markdown("<p>A Meaningful Page Title</p>",unsafe_allow_html=True)
st.set_page_config(page_title="ML based Capstone Project",page_icon='https://img.icons8.com/external-wanicon-lineal-color-wanicon/2x/external-machine-learning-smart-industry-wanicon-lineal-color-wanicon.png')
st.markdown("<h1 style='width:1800;text-align:center;color:orange;background-color:steelblue;width:1500'>CAPSTONE PROJECT</h1>",unsafe_allow_html=True)
st.write('\n')
st.markdown("<p>Note: Click &nbsp; &#8801; &nbsp; on top right corner and check in &#10003; the wide mode for enhanced view</p>",unsafe_allow_html=True)
st.write("\n")


st.markdown("<h3 style='width:1800;text-align:center;color:orange;background-color:steelblue;width:1500'>Clustering Based On Loan_Amount and Balance</h3>",unsafe_allow_html=True)

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
st.write("Given Input Data")
st.write(test_df)
new_pred=m2.predict(test_df)
st.write("Detected Clusters: ",pd.DataFrame(clusters).nunique()[0],(list(pd.DataFrame(clusters)[0].unique())))
st.write("Client ID",int(acc)," falls into cluster: ","'",(new_pred[0]),"'")
test_df.insert(0,"Account ID",acc)
# new_df=pd.concat([pd.DataFrame({"Account_ID":acc}),test_df,pd.DataFrame({"Predicted_Cluster":new_pred})])
test_df['Predicted Cluster']=new_pred
st.write("<h3>\nClustered Output:</h3>",unsafe_allow_html=True)
st.write(test_df)
st.write("\n")
st.write("\n")

#Classification
st.markdown("<h3 style='width:1800;text-align:center;color:orange;background-color:steelblue;width:1500'>Classification Based On Loan_Amount,Payments and Duration</h3>",unsafe_allow_html=True)
df=pd.read_csv("Master_Table_Updated_new.csv")
x=df[['loan_amount','payments','duration']]
y=df[['status']]
rf=RandomForestClassifier(criterion='gini')
mRF=rf.fit(x,y)
accnt=st.number_input("Please Enter Account Number")
loan_amt=st.number_input("Enter Loan Amount:")
pay=st.number_input("Enter Payment")
dur=st.number_input("Enter Duration")
t_x=pd.DataFrame([{"Loan Amount":loan_amt,"Payments":pay,"Duration":dur}])
pred_RF=mRF.predict(t_x)
st.write("Predicted",int(accnt),"Status is: "," '",pred_RF[0],"'")
t_x.insert(0,"Account ID",accnt)
t_x["Predicted Status"]=pred_RF
st.write("<h3>\nClassification Output:</h3>",unsafe_allow_html=True)
st.write(t_x)




st.write("\n")
st.write("\n")
#Reports
st.markdown("<h2 style='width:1800;text-align:center;color:orange;background-color:steelblue;width:1500'>BANK CUSTOMERS DATA ANALYSIS</h2>",unsafe_allow_html=True)
st.title("Loan Report")
html_temp = """<div class='tableauPlaceholder' id='viz1635666782714' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_loan_report&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CapStone_loan_report&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_loan_report&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div><script type='text/javascript'>var divElement = document.getElementById('viz1635666782714');var vizElement = divElement.getElementsByTagName('object')[0];vizElement.style.width='1500px';vizElement.style.height='1350px';var scriptElement = document.createElement('script');scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>"""
components.html(html_temp,width=1500,height=1550)
st.title("Balance Report")
html_temp = """<div class='tableauPlaceholder' id='viz1635657859629' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_balance_report&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CapStone_balance_report&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_balance_report&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1635657859629');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1485px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1485px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='2150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp,width=1500,height=1550)
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.title("Payments Report")
html_temp = """<div class='tableauPlaceholder' id='viz1635666727153' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_payments_report&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CapStone_payments_report&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CapStone_payments_report&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1635666727153');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='1511px';vizElement.style.maxWidth='1611px';vizElement.style.width='100%';vizElement.style.height='1250px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp,width=1550,height=1550)


