# sales analysis 

st.text("")
st.text("")
st.text("")
st.text("")
sales_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Sales Analysis</p>'
st.markdown(sales_title, unsafe_allow_html=True)
st.text("")
st.text("")


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
- 56.5% of the Loans are to Debt Consolidation.
- 22.87% are to pay Credit Card.
- 6.67% are to buy a Home.
- Thus we can conclude that the person who applies for such purposes on the website is more likely to drive revenue for the organization in terms of sales.
"""