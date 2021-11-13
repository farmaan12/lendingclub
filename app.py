#Importing necessary libraries

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
from scipy import stats
import os
import streamlit.components.v1 as components
from PIL import Image
import time



# web app title
st.set_page_config(page_title="Lending Club", page_icon="🤖", layout="wide")

# spinner bar

with st.spinner('Wait for it...'):
     time.sleep(5)
st.success('Done!')



# title and header 

new_title = '<p style="font-family:Courier;text-align: center; font-weight: bold; color:Teal; font-size: 52px;">Lending Club Data Analysis</p>'
st.markdown(new_title, unsafe_allow_html=True)

# navigation bar 

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #008080;">
  <a class="navbar-brand" href="https://www.instagram.com/md_haseeb_z/" target="_blank"Mohammed Haseeb</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.instagram.com/md_haseeb_z/" target="_blank">Instagram</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/mohammed-haseeb-a57417178" target="_blank">Linked In</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



st.markdown('''
# **Data Analysis using Python**

Company Information:

Lending Club is a peer to peer lending company based in the United States, in which investors provide funds for potential borrowers and investors earn a profit depending on the risk they take (the borrowers credit score). Lending Club provides the "bridge" between investors and borrowers. For more basic information about the company please check out the wikipedia article about the company.

**Credit:** App built in `Python` + `Streamlit` by Mohammed Haseeb

---
''') 

# baloons which will add an effect when you open the page.

st.balloons()



#loading data

st.subheader('Preview of dataset which is cleaned and processed:')
df = pd.read_csv('https://github.com/farmaan12/lendingclub/blob/main/pre_processed_data.csv')
st.write(df)  # visualize my dataframe in the Streamlit app


# displaying html page from local computer
# sweetviz EDA

st.text("")
st.text("")
st.text("")
st.header("Data viusualization using SweetViz to understand how the file data is distributed")
st.text("")
st.text("")
HtmlFile = open("C:/Users/mdhas/Report.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code,height=1000,scrolling=True)


# displaying html page from local computer
# Pandas profiling EDA

# st.text("")
# st.text("")
# st.text("")
# st.header("Data viusualization using Pandas Profiling to understand data in more better way with alerts")
# st.text("")
# st.text("")
# HtmlFile1 = open("C:/Users/mdhas/Loan_Report.html", 'r', encoding='utf-8')
# source_code1 = HtmlFile1.read() 
# print(source_code1)
# components.html(source_code1,height=1000,scrolling=True)

# comments 

st.text("")
st.text("")
st.text("")
st.header("Important Information:")
st.text("")
st.subheader("- After checking the datasets and performing eda with two famous libraries we were able to understand that this dataset had almost 49% columns with null values which is not beneficial further, hence these columns were removed for further analysis.")


# heatmap which shows null values in our dataset.

st.text("")
st.text("")
st.text("")
st.header("Heatmap which represents number of null columns before and after cleaning the data")
st.text("")
heatmap = Image.open("C:/Users/mdhas/heatmap.png")
heatmap1 = Image.open("C:/Users/mdhas/heatmap1.png")
st.image([heatmap,heatmap1])


# co-relation between the data and the target variable

st.text("")
st.text("")
st.text("")
st.header("Heatmap which represents co-relation in the data.")
st.text("")
heatmapcor = Image.open("C:/Users/mdhas/heatmapcor.png")
st.image(heatmapcor, width=1500)

st.header("Important Information:")
st.text("")
st.subheader("- Since there are some columns which are highly correlated with the target variable, we decided not to remove these columns from the dataset.")


# distplot which shows amount funded is equal to loan applied by customer.

st.text("")
st.text("")
st.text("")
st.header("Distplot which shows amount funded is equal to loan applied by Customer")
st.text("")
distplot = Image.open("C:/Users/mdhas/distplot.png")
st.image(distplot, width=1500)

# barplot which shows issuance of loan on yearly basis

st.text("")
st.text("")
st.text("")
st.header("Barplot which displays which year the most loans were issued")
st.text("")
barplot = Image.open("C:/Users/mdhas/barplot.png")
st.image(barplot, width=800)

st.header("Information:")
st.text("")
st.subheader("- We can now understand that the most number of loans were issued in the year 2015 compared to all other years and the trend shows that we are increasing in business year by year with more number of Customers.")

# countplot which shows Loan status type distribution

st.text("")
st.text("")
st.text("")
st.header("Countplot which shows Loan status type distribution")
st.text("")
countplot = Image.open("C:/Users/mdhas/countplot.png")
st.image(countplot, width=1500)

# countplot which shows what are the major Client Purposes for Loan Credit

st.text("")
st.text("")
st.text("")
st.header("Countplot which shows what are the major Client Purposes for Loan Credit")
st.text("")
countplot1 = Image.open("C:/Users/mdhas/countplot1.png")
st.image(countplot1, width=1500)

st.text("")
st.text("")
st.header("The top 3 purposes are:")
st.text("")
st.text("56.5% of the Loans are to Debt Consolidation")
st.text("22.87% are to pay Credit Card")
st.text("6.67% are to buy a Home")

# crosstab to display Loan status by Grade 

st.text("")
st.text("")
st.text("")
st.header("Crosstab to display Loan status by Grade ")
st.text("")
crosstab = Image.open("C:/Users/mdhas/crosstab.png")
st.image(crosstab, width=1500)

# determining good loan percentage vs bad loans with pie chart and on yearly basis.


st.text("")
st.text("")
st.text("")
st.header("Bar plot and Pie chart which shows percentage of good and bad loans.")
st.text("")
piechart = Image.open("C:/Users/mdhas/piechart.png")
st.image(piechart, width=1500)


# Loans issued by Region


st.text("")
st.text("")
st.text("")
st.header("Amount of Loans issued by Region.")
st.text("")
map = Image.open("C:/Users/mdhas/map.png")
st.image(map, width=1500)


st.header("Important Information:")
st.text("")
st.subheader("-The regions of the West and SouthEast had a higher percentage in most of the BAD loan statuses.")
st.subheader("-Based on this small and brief summary we can conclude that the West and SouthEast regions have the most undesirable loan status, but just by a slightly higher percentage compared to the NorthEast region.")
st.subheader("-Again, this does not tell us what causes a loan to be a bad loan , but it gives us some idea about the level of risk within the regions across the United States.")
st.text("")
st.text("")

# Loan typed based on group and sub groups


st.text("")
st.text("")
st.text("")
st.header("Type of loans by grade and subgrade.")
st.text("")
barplot2 = Image.open("C:/Users/mdhas/barplot2.png")
st.image(barplot2, width=1000)


# footer

footer="""<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: black;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: Teal;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center; color:black;' href="https://www.linkedin.com/in/mohammed-haseeb-a57417178" target="_blank">Mohammed Haseeb</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


# signoff

st.text("")
st.text("")
st.text("")
signoff = '<p style="font-family:Courier;text-align: center; font-weight: bold; color:Teal; font-size: 52px;">Thank You</p>'
st.markdown(signoff, unsafe_allow_html=True)
