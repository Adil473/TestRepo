import pandas as pd
import os
import win32com.client
import xlwings as xw

def read_profit_and_loss_tab(file_name):
   if file_name:
       # Read the Excel file
       try:
           # xlapp = win32com.client.DispatchEx("Excel.Application")
           # wb = xlapp.Workbooks.Open("Reliance Industr.xlsx")
           # wb.RefreshAll()
           # wb.Save()
           #  # Quit
           # xlapp.Quit()

           workbook = xw.Book("Reliance Industr.xlsx")
           # Refresh all data connections in the workbook
           for connection in workbook.api.Connections:
               connection.refresh()

           # Save and close the updated workbook
           workbook.save("Reliance Industr.xlsx")
           workbook.close()
           # Load only the "Profit and Loss" sheet
           profit_and_loss_df = pd.read_excel(file_name, sheet_name="Profit & Loss")
           # Perform any additional processing here if needed
           print("Profit and Loss Data:")
           print(profit_and_loss_df.head())
       except Exception as e:
           print(f"Error reading Excel file or extracting Profit and Loss tab: {e}")
   else:
       print(f"File {file_name} not found")
if __name__ == '__main__':
   file_name = "Reliance Industr.xlsx"
   read_profit_and_loss_tab(file_name)
