import xlwings as xw

# Connect to the Excel application
app = xw.App()

# Open the XLSM file
wb = app.books.open(r"C:\Users\moham\Desktop\Study\4eme_info\S2\PS\projetS\R.xlsm")

# Get the names of all macro functions in the file
macro_names = [procedure.name for procedure in wb.macros]

# Print the names of all macro functions in the file
print("Macro functions in the file:")
print(*macro_names, sep="\n")

# Close the workbook and quit Excel
wb.close()
app.quit()