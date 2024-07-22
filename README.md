# Tekashi-Alexander Cash Flow Forecasting Model
This is a script which provides a cash flow forecasting for private assets. It is based on the Yale model by Dean Tekashi and Seth Alexander, who built a deterministic model for estimating future cash flows and valuations for the Yale endowment's private equity portfolio. 

## Getting Started

## Step 1. Download CW-TAmodel and any dependencies
1. Download Python for you computer
2. Download CW-TAmodel by using git clone or clicking on the green Code button and clicking Download Zip
3. Extract and open the folder in any terminal app
4. Run pip install pandas

## Step 2. Create your input file
1. Open the file "Portfolio_Data_Template.csv" in excel. It is already loaded with an example portfolio and parameters.
2. Replace the content with your assets, portfolio, commitment date, etc. Please see below "Parameters" section for a full detailed breakdown of each required parameter.
3. Save this file as "Portfolio_Data.csv", overwriting the example one.

## Step 3. CW-TAmodel script
1. Open the folder in any terminal
2. Run python main.py. - (try python3 main.py if it doesnt work)
3. It will take your input file and output a "forecasted_data.csv"

## Parameters
Please see the below parameters required to be defined in the Portfolio_Data input file. You can also find a "default" or suggested parameters here:

CCY1: 25%, CCY2: 33%, CCY3+, 50%, Bow Factor: 5, Growth Rate: 10%, Yield: 5%, Life:10 

1. CC Y1 - Expected amount of contributions in the first year of it's investment life (%). 
2. CC Y2 - Expected amount of contributions to the remaining commitment in the second year (%).
3. CC Y3+ - Expected amount of contributions to the remaining commitment in the third year and onwards (%).
4. Bow Factor - The rate of distribution towards the tail end of the investment life. The "steepness" of the J-curve. The higher the bow factor, the lower the rate of distribution in the earlier years, and the higher of that in the later years. A valid input is between 0 and 20.
![image](https://github.com/user-attachments/assets/1ddd8b95-6584-4385-b94c-ffe2a77de8eb)
5. Growth Rate - The fixed annual growth rate of an investment valuation. A valid input is between -100 and 100% 
6. Yield - Sets a minimum distribution level for the period. A valid input is between 0 and 100%
7. Investment Life - The projected lifetime of the investment in years. A valid input is between 1 and 100.


## Methodology
The TA model starts by defining the capital call (ct) in a given period (cf_year), as the uncalled commitment at the end of the previous period (1-cum_ct), multiplied by the rate of contribution in that period. 



## Output


## Sources


## Contributing
