import streamlit as st
import pandas as pd
from simple_salesforce import Salesforce

st.title("Hello World")

sfUsername = 'michael.zozulia@almalasers.com'
sfPassword = 'EverlyQuinn#7665'
sfToken = '8VY2ZFvXya0eyI1oGCMOZeVc'

sf = Salesforce(username=sfUsername, password=sfPassword, security_token=sfToken)

query = "SELECT Id, Name, Owner.Name FROM Account WHERE CreatedDate = LAST_N_DAYS:30"

data = sf.query(query=query)
records = data['records']
rows = []
for record in records:
    newrow = {
        'id' : record['Id'],
        'name' : record['Name'],
        'owner' : record['Owner']['Name']
        }
    rows.append(newrow)

df = pd.DataFrame(rows)
print(df)

st.dataframe(data=df)