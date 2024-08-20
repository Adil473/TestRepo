import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
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
        headers[0] = 'Dates'
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
        # df.columns = df.iloc[0]
        
        # df.columns = ["Sales","Expenses","Operating Profit","OPM" ,"Other Income", "Interest" , "Depreciation" , "Profit before tax" , "Tax" , "Net Profit" , "EPS in Rs" ,  "Dividend Payout" ]
        print(df.columns)
        # df = df[1:]
        print(df)
        # df.to_csv('profit_and_loss.csv' , index=False)
        # for i in df.iloc[:,1:].columns:
        #    df[i] = df[i].str.replace(',','').str.replace('%','').apply(eval)
        #    print("Row data : ",df[i])

        db_string = "postgresql+psycopg2://postgres:password@localhost:5432/sourcedb"
 
        # Create SQLAlchemy engine
        engine = create_engine(db_string)
 
        # Assuming df is your DataFrame
        df.to_sql('profit_loss_table_data', con=engine, index=False, if_exists='replace')
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
