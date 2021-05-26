import pandas as pd

print("Welcome to the Investment Overview Updater Script")

# read excel files
df = pd.read_excel('data/test_file.xlsx')
# change them in to CSV??

print(df)

# try:
#     print(df.columns)
# except:
#     print("nope")

# columns = df.columns
# print(columns)
# print(f"length = {len(columns)}")
# print(" ")

df.drop(['Account name', 'Account number', 'Bank name', 'Currency', 'Location', 'BIC', 'IBAN',
       'Account status', 'Account type', 'Closing ledger balance',
       'Closing ledger brought forward from', 'Closing available balance',
       'Closing available brought forward from', 'Current ledger balance',
       'Current ledger as at', 'Current available balance',
       'Current available as at', 'Bank reference',
       'Customer reference', 'TRN type'], inplace=True, axis=1)

print(type(df['Narrative'][1]))

df = df[::-1]

print (df)

df.to_excel('output.xlsx')

# columns = columns.drop('Account number', 'Account name')
# print(columns)
# print(f"length = {len(columns)}")

# for i in columns:
#     print(f"{i}")
