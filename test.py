import xlwings as xw
import openpyxl

wb = xw.Book('R.xlsm')

#wb.macro('macro_name')()

sheet=wb.sheets['Sheet1']
#sheet2=wb.sheets['Sheet2']

#print(sheet)
# Lire les données à partir de la feuille de calcul
# Ouvrir le fichier XLSM
workbook = openpyxl.load_workbook('R.xlsm')

# Accéder à la feuille de calcul souhaitée
worksheet = workbook['Matrice_Risque_Globale']

# Lire les données à partir de la feuille de calcul
for row in worksheet.iter_rows(min_row=5, max_row=30, min_col=5, max_col=30):
    for cell in row:
        print(cell.value)
print("\n----------------------\n")
#print(sheet2)

wb.close()