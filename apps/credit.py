# credit risk analysis 
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
credit_title = '<p style="font-family:Courier; font-weight: bold; color:Teal; font-size: 40px;">Credit and Risk Analysis</p>'
st.markdown(credit_title, unsafe_allow_html=True)
st.text("")
st.text("")

'''
**_A Deeper Look into Bad Loans:_**
What we need to know: The number of loans that were classified as bad loans for each region by its loan status. (This will be shown in a dataframe below.) This won't give us the exact reasons why a loan is categorized as a bad loan (other variables that might have influence the condition of the loan) but it will give us a deeper insight on the level of risk in a particular region.
**_Summary:_**
- The regions of the West and SouthEast had a higher percentage in most of the b "bad" loan statuses.
- The NorthEast region had a higher percentage in Grace Period and Does not meet Credit Policy loan status. However, both of these are not considered as bad as default for instance. 
- Based on this small and brief summary we can conclude that the West and SouthEast regions have the most undesirable loan status, but just by a slightly higher percentage compared to the NorthEast region.
- Again, this does not tell us what causes a loan to be a bad loan , but it gives us some idea about the level of risk within the regions across the United States.
'''


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


# Loan typed based on group and sub groups


st.text("")
st.text("")
st.text("")
st.subheader("**_Type of loans by grade and subgrade_**")
barplot2 = Image.open("barplot2.png")
st.image(barplot2, width=1000)

"""
**_Important Information:_**
- The regions of the West and SouthEast had a higher percentage in most of the BAD loan statuses.
- Based on this small and brief summary we can conclude that the West and SouthEast regions have the most undesirable loan status, but just by a slightly higher percentage compared to the NorthEast region.
- Again, this does not tell us what causes a loan to be a bad loan , but it gives us some idea about the level of risk within the regions across the United States.
"""
