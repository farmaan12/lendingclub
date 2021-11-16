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

with st.spinner('Report is being generated! This will not take more than few seconds...'):
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
        <a class="nav-link disabled" href="https://share.streamlit.io/farmaan12/lendingclub/main/app.py">Home <span class="sr-only">(current)</span></a>
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
# **_Overview_**

**_Company Information:_**

Lending Club is a peer to peer lending company based in the United States, in which investors provide funds for potential borrowers and investors earn a profit depending on the risk they take (the borrowers credit score). Lending Club provides the "bridge" between investors and borrowers. For more basic information about the company please check out the wikipedia article about the company.

**Credit:** App built in `Python` + `Streamlit` by _Mohammed Haseeb_

---
''') 

# baloons which will add an effect when you open the page.

st.balloons()



#loading data

st.subheader('**_General information and Preview of dataset which is cleaned and processed:_**')
df = pd.read_csv("pre_processed_data.csv", low_memory=False)
st.write(df)  # visualize my dataframe in the Streamlit app


# displaying html page from local computer
# sweetviz EDA

st.text("")
st.text("")
st.text("")
st.header("**_Data viusualization using SweetViz to understand how the file data is distributed_**")
st.text("")
st.text("")
HtmlFile = open("Report.html", 'r', encoding='utf-8')
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
st.text("")
"""
**_Important Information:_**

- After checking the datasets and performing eda with two famous libraries we were able to understand that this dataset had almost 49% columns with null values which is not beneficial further, hence these columns were removed for further analysis.
- We also have to take csre of the null columns in future and fill them accordingly as per business purposes to see if we can drive more insights out of the data which is null at the moment.
- Below we can see a visual representation to see how the data is filled woith null values.
"""



# heatmap which shows null values in our dataset.

st.text("")
st.text("")
st.text("")
st.subheader("**_Heatmap which represents number of null columns before and after cleaning the data_**")
heatmap = Image.open("heatmap.png")
heatmap1 = Image.open("heatmap1.png")
st.image([heatmap,heatmap1])


# co-relation between the data and the target variable

st.text("")
st.text("")
st.text("")
st.subheader("**_Heatmap which represents co-relation in the data._**")
heatmapcor = Image.open("heatmapcor.png")
st.image(heatmapcor, width=1000)

"""
**_NOTE_**
- Since there are some columns which are highly correlated with the target variable, we decided not to remove these columns from the dataset.

"""

# sales analysis 

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
sales_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Sales Analysis</p>'
st.markdown(sales_title, unsafe_allow_html=True)

# summary for sales analysis

'''
**_Summary:_**

- Most of the loans issued were in the range of 10,000 to 20,000 usd.
- The year of 2015 was the year were most loans were issued.
- Loans were issued in an incremental manner.
- The loans applied by potential borrowers, the amount issued to the borrowers and the amount funded by investors are similarly distributed, meaning that it is most likely that qualified borrowers are going to get the loan they had applied for.
'''


st.text("")
st.text("")

# distplot which shows amount funded is equal to loan applied by customer.

st.text("")
st.subheader("**_Distplot which shows amount funded is equal to loan applied by Customer_**")
distplot = Image.open("distplot.png")
st.image(distplot, width=1500)

# barplot which shows issuance of loan on yearly basis

st.text("")
st.text("")
st.text("")
st.subheader("**_Barplot which displays which year the most loans were issued_**")
barplot = Image.open("barplot.png")
st.image(barplot, width=800)
st.text("")

"""
**_Information:_**
- We can now understand that the most number of loans were issued in the year 2015 compared to all other years and the trend shows that we are increasing in business year by year with more number of Customers.
"""

# countplot which shows Loan status type distribution

st.text("")
st.text("")
st.text("")
st.subheader("**_Countplot which shows Loan status type distribution_**")
countplot = Image.open("countplot.png")
st.image(countplot, width=1500)

# countplot which shows what are the major Client Purposes for Loan Credit

st.text("")
st.text("")
st.text("")
st.subheader("**_Countplot which shows what are the major Client Purposes for Loan Credit_**")
countplot1 = Image.open("countplot1.png")
st.image(countplot1, width=1500)

st.text("")
st.text("")
"""
**_The top 3 purposes are:_**

- 56.5% of the Loans are to Debt Consolidation.4
- 22.87% are to pay Credit Card.
- 6.67% are to buy a Home.
"""



# credit risk analysis 
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
credit_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Credit and Risk Analysis</p>'
st.markdown(credit_title, unsafe_allow_html=True)

# crosstab to display Loan status by Grade 

st.text("")
st.subheader("**_Crosstab to display Loan status by Grade_**")
crosstab = Image.open("crosstab.png")
st.image(crosstab, width=1500)

# determining good loan percentage vs bad loans with pie chart and on yearly basis.


st.text("")
st.text("")
st.text("")
st.subheader("**_Bar plot and Pie chart which shows percentage of good and bad loans_**")
piechart = Image.open("piechart.png")
st.image(piechart, width=1500)


# Loans issued by Region


st.text("")
st.text("")
st.text("")
st.subheader("**_Amount of Loans issued by Region_**")
map = Image.open("map.png")
st.image(map, width=1500)


"""
**_Important Information:_**

- The regions of the West and SouthEast had a higher percentage in most of the BAD loan statuses.
- Based on this small and brief summary we can conclude that the West and SouthEast regions have the most undesirable loan status, but just by a slightly higher percentage compared to the NorthEast region.
- Again, this does not tell us what causes a loan to be a bad loan , but it gives us some idea about the level of risk within the regions across the United States.
"""


# Loan typed based on group and sub groups


st.text("")
st.text("")
st.text("")
st.subheader("**_Type of loans by grade and subgrade_**")
barplot2 = Image.open("barplot2.png")
st.image(barplot2, width=1000)



# ops team analysis 
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
ops_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Operations Analysis</p>'
st.markdown(ops_title, unsafe_allow_html=True)
st.text("")



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
