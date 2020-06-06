import xlrd
loc = ("/home/brijesh/Downloads/Q3AzurepresslacStrings.xlsx")
#loc = ("/home/brijesh/Downloads/Timesheet_Brijesh.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#sheet.cell_value(1, 1)
for row in range(0,sheet.nrows):
    print(sheet.row_values(row))
#print(sheet.row_values(1))
