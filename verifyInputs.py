from datetime import datetime

# symbol: capitalized, 1-7 alpha characters
def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and (1 <= len(symbol) <= 7)

# chart type: 1 numeric character, 1 or 2
def is_valid_chart_type(chart_type):
    try: 
        return int(chart_type) in [1, 2]
    except:
        return False

# time series: 1 numeric character, 1 - 4
def is_valid_time_series(time_series):
    try: 
        return int(time_series) in [1, 2, 3, 4]
    except:
        return False

# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD
def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

print(is_valid_chart_type('1'))
