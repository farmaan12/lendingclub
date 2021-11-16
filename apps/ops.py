# ops team analysis 
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
ops_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Operations Analysis (Business Perspective)</p>'
st.markdown(ops_title, unsafe_allow_html=True)
st.text("")

'''
**_Summary:_**
- Below visualization will help the operational team to understand which audience has to be targeted in order to increase revenue.
- We can see that there are approximately 45% unverified customers. We can verify their source of income which in turn will be helpful for future business purposes.
- Top Experience employees plot describes the experience of employees which tells us that there are many eligible customers who can drive more business to our company.
- We can target the mid range experienced employees who will be the best revenue generators to our company as they will still work in the organization for a long time.
'''

# verified status

st.text("")
st.text("")
st.text("")
st.subheader("**_Loan verification status types distribution to see_**")
barplot33 = Image.open("barplot33.png")
st.image(barplot33, width=1000)

# top experience employees

st.text("")
st.text("")
st.text("")
st.subheader("**_Employment Experience in total years_**")
barplot44 = Image.open("exp-emp.png")
st.image(barplot44, width=1500)


'''
**_Important Information to increase revenue with the help of data:_**
- Company have to collect the data from website which provides information stating engagement time of the customer which will help us to understand what is the best time to contact guest to drive a sale and revenue to the company.
- We have to fill null values with some meaningful information so we can analyse and gain more insights out of the data.
- Website traffic data can help us reach out to potential employee who requires a loan and increase in our sales and revenue.
- There are many other factors which can be driven from the data to make more helpful decisions in future.
'''
