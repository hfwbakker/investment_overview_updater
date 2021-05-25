import pandas as pd

print("Welcome to the Investment Overview Updater Script")

# read excel files
df = pd.read_excel('test_file.xlsx')
# change them in to CSV??

# print(df)

# try:
#     print(df.columns)
# except:
#     print("nope")

columns = df.columns
print(columns)
print(f"length = {len(columns)}")

print(" ")

# df.drop('Account name', inplace=True, axis=1)

columns = columns.drop('Account name')
print(columns)
print(f"length = {len(columns)}")

for i in columns:
    print(f"{i}")