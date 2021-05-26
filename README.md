# investment_overview_updater

PROJECT:
- Create a script that can take bank statement info in excel and/or pdf format and reorganizes it in a way ready to use for further processing
- Dates should all be on a new line
- Several bank account will be added and listed side by side.
- Python's Pandas (and perhaps openpyxl) should provide all the functionality I need.


NEXT UP:
- Continue filtering info from input excel sheet (like too many columns, stick with date, amount, reference, and perhaps other account number)
- Need to merge two columns (credit and debit), perhaps can do like this: for i in column_1: column_3.append(column_1[i] + column_2[i])?
- Combine output file with input from other files (info from multiple bank accounts).
- Some of the strings inside  columns (especially in 'Narrative') are super long, perhaps need to edit those with regex?
- Is it possible to sort by date (column 'Post date')?
- Is it possible to format the excel sheet as you output data to it, like with openpyxl?


LOG:
--- Wednesday, May 26th, 2021 ---
Day 2 of "investment overview updater".
- Filtered columns, now deleting everything except number, narrative, credit amount, debit amount, balance, and post date.
- Reversed order of data (top to bottom direction switched) to match input direction in investment overview file.
- Now succesfully outputting to 'output.xlsx'

--- Tuesday, May 25th, 2021 ---
Day 1 of "investment overview updater".
- Create repository on github
- Created venv
- Started out with openpyxl but switched to pandas upon recommendation
- Successfully read and printed first test excel file
- Succesfully deleted a column