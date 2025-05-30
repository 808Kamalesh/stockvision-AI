import yfinance as yf
import pandas as pd
from datetime import datetime, time
import pytz
from config import TIMEZONE, MARKET_OPEN, MARKET_CLOSE

def is_market_open():
    now = datetime.now(pytz.timezone(TIMEZONE)).time()
    open_time = time(*MARKET_OPEN)
    close_time = time(*MARKET_CLOSE)
    weekday = datetime.now().weekday() < 5
    return weekday and open_time <= now <= close_time

def load_intraday_data(ticker, interval, period):
    if not is_market_open():
        return pd.DataFrame(), "Market is closed. Data may be stale."

    data = yf.download(ticker, interval=interval, period=period, progress=False)
    if data.empty:
        return pd.DataFrame(), f"No data for {ticker}."

    data = data[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
    if len(data) < 120:
        return pd.DataFrame(), "Not enough data (min 120 points)."
    
    return data, "Success"
