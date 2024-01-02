import requests
from pprint import pprint
from datetime import date , timedelta


def get_rates(currencies:list,days=30):

    end_at=date.today()
    delta=timedelta(days=days)
    start_at=end_at - delta
    symbols = ','.join(currencies)
    r=requests.get(f"https://api.exchangerate.host/timeseries?start_date={start_at}&end_date={end_at}&symbols={symbols}")
    if not r and not r.json():
        return False,False
    rates=r.json().get("rates")
    dates_list=list(rates.keys())
    all_rates={currency:[] for currency in currencies}
    for each_day in dates_list:
        [all_rates[key].append(value) for key,value in rates[each_day].items()]
    return dates_list,all_rates

