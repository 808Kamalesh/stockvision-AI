import pandas as pd
import numpy as np

def compute_indicators(df):
    df['Momentum'] = df['Close'].diff(3)
    df['Acceleration'] = df['Momentum'].diff(3)
    df['ROC'] = df['Close'].pct_change(8) * 100
    df['MACD'] = df['Close'].ewm(8).mean() - df['Close'].ewm(20).mean()
    df['Signal'] = df['MACD'].ewm(6).mean()
    rolling_mean = df['Close'].rolling(15).mean()
    rolling_std = df['Close'].rolling(15).std()
    df['Boll_Upper'] = rolling_mean + 1.5 * rolling_std
    df['Boll_Lower'] = rolling_mean - 1.5 * rolling_std
    df['RSI'] = 100 - (100 / (1 + df['Close'].diff().clip(lower=0).rolling(10).mean() /
                                      df['Close'].diff().clip(upper=0).abs().rolling(10).mean()))
    df = df.fillna(0)
    return df
