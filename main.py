from run_analysis import run_analysis
from config import DEFAULT_TICKER, DEFAULT_INTERVAL, DEFAULT_PERIOD

if __name__ == "__main__":
    ticker = input(f"Ticker ({DEFAULT_TICKER}): ") or DEFAULT_TICKER
    interval = input(f"Interval ({DEFAULT_INTERVAL}): ") or DEFAULT_INTERVAL
    period = input(f"Period ({DEFAULT_PERIOD}): ") or DEFAULT_PERIOD
    run_analysis(ticker, interval, period)
