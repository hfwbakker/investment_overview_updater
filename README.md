# investment_overview_updater

PROJECT:
- Create a script that can take bank statement info in excel and/or pdf format and reorganizes it in a way ready to use for further processing
- Dates should all be on a new line
- Several bank account will be added and listed side by side.
- Python's Pandas (and perhaps openpyxl) should provide all the functionality I need.


NEXT UP:
- Some of the strings inside  columns (especially in 'Narrative') are super long, perhaps need to edit those with regex?
- Use ARGV to input files to filter?
- Perhaps use a for loop or function to filter those files since they have the same format?


LOG:
--- Sunday, May 30th, 2021 ---
- Script now takes both HSBC China account excel sheets and now combines them into an excel sheet sorted by date, with seperate columns for 001 and 011 accounts.
- Installed pprint and tried to apply it to the df printing in terminal but doesnt seem to do much. Is it because some of the long strings (in narrative) include \ which could be read as escape characters or something? Maybe it's the Chinese characters that cause confusion? -> it seems that in terminal chinese characters take up more space than "normal" characters.
- Included os.path and a while loop check to prevent overwriting existing output. Now instead of replacing e.g. "output0.xlsx" it will create "output1.xlsx".
- Input from personal account, 001, 011 account are now combined, filtered, and sorted. Script is essentially fully functional. Will consider adding input from HK accounts as well but those are not used as much and it might simply not be worth the effort.

--- Friday, May 28th, 2021 ---
- Succesfully summed the debit and credit columns. Initially had an issue with them returning NaN (because by default either the credit or debit column is NaN), fixed it with .fillna(0) method, which automatically converts NaN to 0. No for loop was needed.
- Realized that the first column with indices that I couldn't select or rename seems to be automatically added by Pandas when reading the data. Perhaps its a result of reading from excel as excel automatically numbers rows? -> nope, checked with Excel source file and numbers don't match Excel row numbers.
- Succesfully changed column order to match investment overview sheet.

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