import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Table , Column , Integer , String , MetaData

# Replace with your Screener.in login credentials
email = "vgjmunq5q@rskfc.com"
password = "2B00A2E5"
# Start a session
session = requests.Session()
# Get the login page to retrieve the CSRF token
login_url = "https://www.screener.in/login/?"
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')
# Find the CSRF token in the login form (usually in a hidden input field)
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
# Prepare the login payload
login_payload = {
   'username': email,
   'password': password,
   'csrfmiddlewaretoken': csrf_token
}
# Include the Referer header as required
headers = {
   'Referer': login_url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
# Send the login request
response = session.post(login_url, data=login_payload, headers=headers)
print(response.url)
# Check if login was successful

if response.url == "https://www.screener.in/dash/":
    print("Login successful")
   # Now navigate to the Reliance company page
    search_url = "https://www.screener.in/company/RELIANCE/consolidated/"
    search_response = session.get(search_url)
    if search_response.status_code == 200:
        
        print("Reliance data retrieved successfully")
        soup = BeautifulSoup(search_response.content, 'html.parser')

        section = soup.find('section' , {'id': 'profit-loss'})
        table = section.find('table' , {'class': 'data-table responsive-text-nowrap'})

        headers = [th.text.strip() for th in table.find_all('th')]
        headers[0] = 'year'
        print(headers)
        rows = table.find_all('tr')
        row_data = []

        for row in rows[1:]:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            row_data.append(cols)
        print(row_data)

        df = pd.DataFrame(row_data , columns=headers)
        # print(df)
        df = df.transpose()
        df.columns = df.iloc[0]
        
        # df.columns = ["Sales","Expenses","Operating Profit","OPM" ,"Other Income", "Interest" , "Depreciation" , "Profit before tax" , "Tax" , "Net Profit" , "EPS in Rs" ,  "Dividend Payout" ]
        print(df.columns)
        df = df[1:]
        df["stock name"] = "reliance"
        print(df)
        # df.to_csv('profit_and_loss.csv' , index=False)
        # for i in df.iloc[:,1:].columns:
        #    df[i] = df[i].str.replace(',','').str.replace('%','').apply(eval)
        #    print("Row data : ",df[i])

        db_string = "postgresql+psycopg2://postgres:password@192.168.1.103:5432/reliance"
 
        # Create SQLAlchemy engine
        engine = create_engine(db_string)

        # create table before inserting
        metadata = MetaData()
        my_table = Table('profit_loss' , metadata , 
                        Column('year',  Integer, primary_key=True ) , 
                        Column('Sales +' , String),
                        Column('Expenses +' , String),
                        Column('Operating Profit' , String),
                        Column('OPM %' , String),
                        Column('Other Income +' , String),
                        Column('Interest' , String),
                        Column('Depreciation' , String),
                        Column('Profit before tax' , String),
                        Column('Tax %' , String),
                        Column('Net Profit +' , String),
                        Column('EPS in Rs' , String),
                        Column('Dividend Payout %' , String),
                        Column('stock name' , String),
        )
        metadata.create_all(engine)
        # write into table
        df.to_sql('profit_loss' , engine , if_exists='append' , index=False)

        try:
           df.to_sql('profit_loss_data', con=engine, index=True, if_exists='replace', index_label='year')
           with engine.connect() as connection:
              alter_table_sql = """
               ALTER TABLE profit_loss_data ADD PRIMARY KEY (year);
              """
              connection.execute(text(alter_table_sql))
           print("Data saved to MySQL with id column set as primary key")
        except SQLAlchemyError as e:
           print(f"Error: {e}")
        finally:
           engine.dispose()
       
        # Assuming df is your DataFrame
        # df.to_sql('profit_loss_data', con=engine, index=True, if_exists='replace')
        print("data written successfully")

        
        




    #    # Find the Excel download link
    #     excel_link = soup.find('button',{'aria-label' : 'Export to Excel'} )
    #     print(excel_link)
    #     if excel_link:
    #         excel_url = "https://www.screener.in" + excel_link['formaction']
    #         print(excel_url)
    #         excel_response = session.get(excel_url,headers=headers)
    #        # Save the Excel file
    #         with open("Reliance.xlsx", "wb") as excel_file:
    #            excel_file.write(excel_response.content)
    #         print("Excel file downloaded successfully")
    #     else:
    #         print("Failed to find the Excel download link.")
    # else:
    #    print("Failed to retrieve Reliance data. Status Code:", search_response.status_code)
else:
   print("Login failed. Response URL:", response.url)
