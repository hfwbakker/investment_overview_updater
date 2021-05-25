# investment_overview_updater

PROJECT:
- Create a script that can take bank statement info in excel and/or pdf format and reorganizes it in a way ready to use for further processing
- Dates should all be on a new line
- Several bank account will be added and listed side by side.
- Switched to using Pandas instead of Open

NEXT UP:
- Continue filtering info from input excel sheet (like too many columns, stick with date, amount, reference, and perhaps other account number)
- Output to Excel sheet (or other format)


LOG:
--- Tuesday, May 25th, 2021 ---
Day 1 of "investment overview updater".
- Create repository on github
- Created venv
- Started out with openpyxl but switched to pandas upon recommendation
- Successfully read and printed first test excel file
- Succesfully deleted a column