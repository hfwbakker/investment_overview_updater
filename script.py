import pandas as pd

print("Welcome to the Investment Overview Updater Script")

### READ DATA ###
df = pd.read_excel('data/test_file.xlsx')

### FILTER & MODIFY DATA ###
df['cash_flow'] = df['Credit amount'].fillna(0) + df['Debit amount'].fillna(0)
print(df['cash_flow'])

print(df.head())

df.drop(['Account name', 'Account number', 'Bank name', 'Currency', 'Location', 'BIC', 'IBAN',
       'Account status', 'Account type', 'Closing ledger balance',
       'Closing ledger brought forward from', 'Closing available balance',
       'Closing available brought forward from', 'Current ledger balance',
       'Current ledger as at', 'Current available balance',
       'Current available as at', 'Bank reference',
       'Customer reference', 'TRN type', 'Credit amount', 'Debit amount'], inplace=True, axis=1)

df = df[::-1] # reverses row order

df = df[['Post date', 'Narrative', 'cash_flow']]

# change column order to date > narrative > amount

### OUTPUT ###
print(df.columns)
print(df)

df.to_excel('output.xlsx')
