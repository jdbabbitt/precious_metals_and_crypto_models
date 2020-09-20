import requests, quandl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
"""
Functions that gather and plot chart data.

plt_num argument represents which chart this is in the plot (chart 1, chart 2, chart3, etc). Defaults to 1
num_of_charts argument is the total number of charts that will be displayed in the plot

Ex) if you have two charts you want to plot side by side,
    btc_price_chart(1,2) plt_num is 1 and num_of_charts is 2 since its the first chart out of 2 charts 
    eth_price_chart(2,2) plt_num is 2 and num_of_charts is 2 since its the second chart out of 2 charts 
"""
def btc_price_chart(plt_num=1, num_of_charts=1):
    btc_data = quandl.get("BITSTAMP/USD", authtoken="_5hJPZAh3B_8J8HzfT8s")
    plt.subplot(1,num_of_charts,plt_num)
    btc_data["Last"].plot(kind="line")
    plt.ylabel("Price (USD)")
    plt.xlabel("Year")
    plt.title("Bitcoin/USD Price Chart")

def btc_supply_chart(plt_num=1, num_of_charts=1):
    supply_data = quandl.get("BCHAIN/TOTBC", authtoken="_5hJPZAh3B_8J8HzfT8s")
    plt.subplot(1,num_of_charts,plt_num)
    supply_data.plot(kind="line")
    plt.ylabel("Supply")
    plt.xlabel("Year")
    plt.title("Bitcoin Supply Chart Price Chart")

def eth_price_chart(plt_num=1, num_of_charts=1):
    eth_data = quandl.get("GDAX/ETH_USD", authtoken="_5hJPZAh3B_8J8HzfT8s")
    plt.subplot(1,num_of_charts,plt_num)
    eth_data["Open"].plot(kind="line")
    plt.ylabel("Price (USD)")
    plt.xlabel("Year")
    plt.title("Ethereum/USD Price Chart")

def gold_price_chart(plt_num=1, num_of_charts=1):
    gold_data = quandl.get("LBMA/GOLD", authtoken="_5hJPZAh3B_8J8HzfT8s")
    plt.subplot(1,num_of_charts,plt_num)
    gold_data["USD (AM)"].plot(kind="line")
    plt.ylabel("Price (USD)")
    plt.xlabel("Year")
    plt.title("Gold/USD Price Chart")

def silver_price_chart(plt_num=1, num_of_charts=1):
    silver_data = quandl.get("LBMA/SILVER", authtoken="_5hJPZAh3B_8J8HzfT8s")
    plt.subplot(1,num_of_charts,plt_num)
    silver_data["USD"].plot(kind="line")
    plt.ylabel("Price (USD)")
    plt.xlabel("Year")
    plt.title("Silver/USD Price Chart")
