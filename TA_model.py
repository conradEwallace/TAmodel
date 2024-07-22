import pandas as pd

#Finding Cumulative Capital Calls
def capital_call_algo (ccy_values, cf_year,investment_life):
    if cf_year > investment_life:
        cf_year = investment_life
        
    forecast_start_year = 1
    cum_year = forecast_start_year
    cum_ct = 0
    ct = 0
    yearly_ct_dict = {}
    cum_ct_list = []
    
    for j in range (1,investment_life+1):
        
        for i in range(1, cum_year+1):
            if i in ccy_values:
                ct = (1-cum_ct)*ccy_values[i]
            else:
                ct = (1-cum_ct)*ccy_values[3]
        cum_ct += ct   
        cum_year+=1
        yearly_ct_dict[j] = ct
        cum_ct_list.append(cum_ct)

    return cum_ct_list[cf_year-1], yearly_ct_dict



# Finding Distributions Using Ct 
def distribution_algo(ct2, cf_year,bow_factor,growth_rate,yield_rate,investment_life):

    if cf_year > investment_life:
        cf_year = investment_life
        
    dt = 0
    bow_component = 0
    RD = 0
    NAVt = 0
    cum_dt_list = []
    yearly_dt_dict = {}
    cum_dt = 0
    
    for i in range(1, cf_year + 1):
        if i == 1:
            NAVt = ct2[i] - dt
        else:
            bow_component = (i / investment_life) ** bow_factor if i <= cf_year else 1
            RD = max(bow_component, yield_rate)
            dt = NAVt * (1 + growth_rate) * RD
            NAVt = NAVt * (1 + growth_rate) + ct2[i] - dt
        
        cum_dt += dt
        cum_dt_list.insert(i,cum_dt)
        yearly_dt_dict[i] = dt

    return cum_dt_list[cf_year-1]