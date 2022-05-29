import streamlit as st
import pandas as pd



df=pd.read_csv("Master_Table_Updated_new.csv")
x=df[['loan_amount','duration','payments']]
