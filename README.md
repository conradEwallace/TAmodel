# Tekashi-Alexander Cash Flow Forecasting Model
The Tekashi-Alexander Cash Flow Forecasting Model predicts the cash flow for private assets, helping investors to make informed decisions.

## Getting Started

### Prerequisites
•	Python 3.x installed on your computer

•	Required libraries: pandas


### Installation
1. Download the Project
   
  	•	Clone the repository: git clone https://github.com/conradEwallace/TAmodel
   
  	•	Or download the ZIP and extract it.

3. Install Dependencies
   
  	•	Navigate to the project directory and run: pip install pandas


### Creating Input File
1. Open Portfolio_Data_Template.csv in Excel.
2. Replace the example data with your portfolio details.
3. Save the file as Portfolio_Data.csv in the project directory.

### Running the Script
1. Open the terminal in the project directory.
2. Run the script: python main.py (or python3 main.py if necessary)
3. The script will generate forecasted_data.csv with the forecasted cash flows.

### Parameters
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



### Methodology
The model starts by defining the current cashflow year for the investment as the current date minus the vintage. This allows the model to understand the current year in relation to the vintage and the investment life.

Capital call (ct) in a given period (cf_year), is the uncalled commitment multiplied by the rate of contribution in that period. 

Distributions (dt) are a product of the previous year NAV multiplied with a growth rate and a rate of distribution function RD. 

dt = NAVt * (1 + growth_rate) * RD

Where:
RD = max(bow_component, yield_rate)
bow_component = function of the current year, investment life and bow_factor. 

The cumulative cash flow for each year is calculated and multiplied by the commitment value to get the expected cash flow for that year.


### Output

The output file forecasted_data.csv contains the asseet-level cumulative cash flow from Year 1 (next year) to the maximum investment life.


### Sources
Takashi Alexander Model (aka Yale model) by Dean Tekashi and Seth Alexander of the Yale University Investments Office.
https://www.hbs.edu/faculty/Pages/item.aspx?num=64173

The Takashi and Alexander Model by Christoph Jackel
https://www.christoph-jaeckel.com/posts/2023-02-05-the-takahashi-and-alexander-model/

## Contributing
Your contributions are welcome! Please fork the repository and create a pull request to contribute.
