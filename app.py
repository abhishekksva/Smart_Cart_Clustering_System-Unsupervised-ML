import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("SmartCart - Customer Segmentation")
df = pd.read_csv("smartcart_customers.csv")
st.write("Shape:", df.shape)
