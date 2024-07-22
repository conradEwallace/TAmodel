import os
import time
import pandas as pd
from datetime import date, datetime
from data_processing import strip_percentage
from TA_model import capital_call_algo, distribution_algo

def clear_terminal():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()
print('Hello, welcome to CW Private Assets Cash Flow Forecasting Model')
time.sleep(2)
print('This model is based on the Tekashi Alexander model AKA the Yale model')
time.sleep(2)
print('Please ensure you read the read_me file which will give you the step by step process on how to use this script')
time.sleep(4)
print('If you have read the read_me file, and have done the necessary steps required for this script to work, then we can proceed.')
time.sleep(3)
start_script = input('Would you like to start the script? (Y/N): ').strip().upper()

if start_script == 'Y':
    clear_terminal()
    #Importing the commitment data
    print('Importing Portfolio Data...')
    portfolio = pd.read_csv('Portfolio_Data.csv')

    print('Cleaning Data and preparing for processing...')

    #Removing all leading and trialling white spaces from column names
    portfolio.columns = portfolio.columns.str.strip()

    #Changing date to a datetime object
    portfolio['Date'] = pd.to_datetime(portfolio['Date'],format='%d/%m/%Y')

    #Stripping percentage and assigning these values as floats
    portfolio['CC Y1'] = portfolio['CC Y1'].apply(strip_percentage)
    portfolio['CC Y2'] = portfolio['CC Y2'].apply(strip_percentage)
    portfolio['CC Y3+'] = portfolio['CC Y3+'].apply(strip_percentage)
    portfolio['Growth Rate'] = portfolio['Growth Rate'].apply(strip_percentage)
    portfolio['Yield'] = portfolio['Yield'].apply(strip_percentage)

    #Creating a new dataframe which could contain the forecasted values
    forecasted_data = portfolio


    #We can create a function that loops through each index, calculates the CF year,
    for i, row in portfolio.iterrows():
        cf_year = datetime.now().year - row['Date'].year + 1
        ccy_values = {1: row['CC Y1'], 2: row['CC Y2'], 3: row['CC Y3+']}
        bow_factor = row['Bow Factor']
        growth_rate = row['Growth Rate']
        yield_rate = row['Yield']
        investment_life = row['Life']
        commitment_value = row['Commitment']

        # Skip the row if cf_year is greater than investment_life
        if cf_year > investment_life:
            print(f"Skipping row {i} as cf_year > investment_life")  # Debug statement
            continue

        for j in range(1, investment_life + 1):
            print(f"Processing row {i}: cf_year = {j}")
            cum_capital_call, yearly_ct_dict = capital_call_algo(ccy_values, cf_year, investment_life)
            cum_distributions = distribution_algo(yearly_ct_dict, cf_year, bow_factor, growth_rate, yield_rate, investment_life)
            cum_cash_cfyear = cum_distributions - cum_capital_call
            cum_cash_cfyear_value = int((cum_cash_cfyear) * commitment_value)

            if j not in forecasted_data.columns:
                forecasted_data[j] = 0
            forecasted_data.at[i,j] = cum_cash_cfyear_value
            cf_year += 1
    print("Processing complete, please access table 'forecasted_data'")

    #Renaming Columns
    rename_dict = {int(i): f'Year {i}' for i in range (1,11)}
    forecasted_data = forecasted_data.rename(columns=rename_dict)

    #Exporting forecasted data to csv
    forecasted_data.to_csv('forecasted_data.csv')
else:
    print("Script terminated.")