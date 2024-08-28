import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy import text
def read_profit_and_loss_tab(file_name):   
    if file_name:
        try:
            profit_and_loss_df = pd.read_excel(file_name, sheet_name="Data Sheet" , usecols='A:K' , skiprows=15 , nrows=15)
            profit_and_loss_df.set_index("Report Date" , inplace=True)
            profit_and_loss_df = profit_and_loss_df.transpose()
            profit_and_loss_df["company"] = file_name.strip(".xlsx")

            print(f"Profit and Loss Data {file_name}:")
            print(profit_and_loss_df)

            profit_and_loss_df.to_sql('profit_loss' , con=engine , if_exists='append' , index=True , index_label='Report Date')
            print("data written to postrges")

        except Exception as e:
            print(f"Error reading Excel file or extracting Profit and Loss tab: {e}")
    else:
        print(f"File {file_name} not found")
if __name__ == '__main__':
    company_names = ["Reliance Industr.xlsx" , "HDFC Bank.xlsx" , "Nestle India.xlsx" , "Adani Enterp.xlsx"]
    db_string = "postgresql+psycopg2://postgres:password@192.168.1.103:5432/sourcedb"
    engine = create_engine(db_string)
    # company_names = ["HDFC Bank.xlsx"]
    for file_name in company_names:
        read_profit_and_loss_tab(file_name)


