import pandas as pd
from datetime import date, datetime

def strip_percentage(value):
    return float(value.strip('%')) / 100 if isinstance(value,str) else value

def conv_to_float(string):
    return float(string.replace(',',''))

# portfolio['Movement Lc'] = portfolio['Movement Lc'].apply(conv_to_float)

