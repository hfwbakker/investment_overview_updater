import pandas as pd
import os.path
from datetime import datetime
from functools import partial

print("Welcome to the Investment Overview Updater Script")

### READ DATA ###
df1 = pd.read_excel('data/001_account.xlsx')
df2 = pd.read_excel('data/011_account.xlsx')
df3 = pd.read_excel('/Users/henribakker/OneDrive/WORK/3. Frying Dutchman/Chapter 1/2. Legal & Finance/DMF Finance/Investment overview/gemaakte kosten.xlsx')


### FILTER & MODIFY DATA ###
df1['001 Cash flow'] = df1['Credit amount'].fillna(0) + df1['Debit amount'].fillna(0)
df1['Post date'] = df1['Post date'].astype('datetime64')
df2['011 Cash flow'] = df2['Credit amount'].fillna(0) + df2['Debit amount'].fillna(0)
df2['Post date'] = df2['Post date'].astype('datetime64')


df1.drop(['Account name', 'Bank name', 'Currency', 'Location', 'BIC', 'IBAN',
       'Account status', 'Account type', 'Closing ledger balance',
       'Closing ledger brought forward from', 'Closing available balance',
       'Closing available brought forward from', 'Current ledger balance',
       'Current ledger as at', 'Current available balance',
       'Current available as at', 'Bank reference',
       'Customer reference', 'TRN type', 'Credit amount', 'Debit amount'], inplace=True, axis=1)

df2.drop(['Account name', 'Bank name', 'Currency', 'Location', 'BIC', 'IBAN',
       'Account status', 'Account type', 'Closing ledger balance',
       'Closing ledger brought forward from', 'Closing available balance',
       'Closing available brought forward from', 'Current ledger balance',
       'Current ledger as at', 'Current available balance',
       'Current available as at', 'Bank reference',
       'Customer reference', 'TRN type', 'Credit amount', 'Debit amount'], inplace=True, axis=1)

df3.drop(['How much', 'in'], inplace=True, axis=1)


### MERGING DATAFRAMES & SORTING ###
print("attempting to merge df1 and df2")
final_df = pd.concat([df1, df2, df3])
# final_df = pd.concat([df1, df2])
final_df = final_df[['Post date', 'Narrative', 'Balance Henri', '001 Cash flow', '011 Cash flow', 'Account number']]
# final_df = final_df[['Post date', 'Narrative', '001 Cash flow', '011 Cash flow', 'Account number']]

final_df = final_df.sort_values('Post date')

print("df1")
print(df1.dtypes)
print("\n\ndf2")
print(df2.dtypes)
print("\n\ndf3")
print(df3.dtypes)


### OUTPUT ###
# output files, while ensuring to not remove existing output files.
filecount = 0
while os.path.isfile(f"ouput/output{filecount}.xlsx") == True:
    filecount += 1
final_df.to_excel(f"output/output{filecount}.xlsx")
print(f"Output to 'output/output{filecount}.xlsx'")
