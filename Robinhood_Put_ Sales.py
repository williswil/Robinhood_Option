import Config
import robin_stocks as r
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
import random
import datetime as dt
import time
import scipy.stats as stats
def open_market():
    market = False
    time_now = dt.date.now().time()
    market_open = dt.time(8,00,0)
    market_close = dt.times(15,00,0)
    if time_now > market_open and time_now < market_close:
        maret = True
    else: 
        # print('### market is closed')
        pass
    return(market)

def login_to_account(days):
    # Calculate the time range in seconds
    start = 7 * 60 * 60 + 50 * 60
    end = 15 * 60 * 60 + 50 * 60
    wait_time = random.uniform(start, end)

    # Wait for a random duration within the time range
    print("Waiting for", wait_time, "seconds...")
    time.sleep(wait_time)

    # Perform the login here
    time_logged_in = 60*60*24*days
    r.authentication.login(username=Config.Username,Password=Config.Password,expiresIn=time_logged_in,scope='internal',by_sms=True,store_session=True)
    print("Logging into account...")

def show_stocks():
    my_stocks = r.stocks.get_watchlist_by_name(name="Options_Watchlist")
    for stock in my_stocks:
        print(stock['symbol'])

#def choose_most_profitable_put_option(stock_price, volatility, time_to_expiry, risk_free_rate, strike_prices):
    max_profit = float("-inf")
    r.options.find_options_by_specific_profitability("my_stocks",expirationDate=None,strikePrice=None,optionType="put",typeProfit='chance_of_profit_short',profitFloor=0.75,profitCeiling=1.0,info=None)
    most_profitable_strike_price = None
    for strike_price in strike_prices:
        put_price = sell_put_option(strike_price, stock_price, volatility, time_to_expiry, risk_free_rate)
        profit = put_price + (stock_price - strike_price)
        if profit > max_profit:
            max_profit = profit
            most_profitable_strike_price = strike_price
    if most_profitable_strike_price is not None:
        return most_profitable_strike_price
    else:
        return "No profitable options found"

#def sell_put_option(strike_price, stock_price, volatility, time_to_expiry, risk_free_rate):
    d1 = (np.log(stock_price/strike_price) + (risk_free_rate + 0.5 * volatility**2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)
    put_price = strike_price * np.exp(-risk_free_rate * time_to_expiry) * stats.norm.cdf(-d2) - stock_price * stats.norm.cdf(-d1)
    probability_of_profit = 1 - stats.norm.cdf(d2)
    if probability_of_profit >= 0.75:
        return put_price

#def logout():
    r.authentication.logout()#