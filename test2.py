import win32com.client

# Create a connection to Microsoft Excel
excel = win32com.client.Dispatch("Excel.Application")

# Open the XLSM file
workbook = excel.Workbooks.Open(r"C:\Users\moham\Desktop\Study\4eme_info\S2\PS\projetS\R.xlsm")

# Get the sheet names
sheet_names = [sheet.Name for sheet in workbook.Sheets]

# Activate the macro function on each sheet
for sheet_name in sheet_names:
    worksheet = workbook.Sheets(sheet_name)
    excel.Application.Run("'" + workbook.Name + "'!" + "clean")
    worksheet.Calculate()

# Save the file and quit Excel
workbook.Save()
workbook.Close()
excel.Quit()
