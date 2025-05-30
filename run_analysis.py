from data_loader import load_intraday_data
from indicators import compute_indicators
from heikin_ashi import heikin_ashi
from simulation import monte_carlo_simulation
from ml_model import prepare_ml_data, train_ml
from signal_generator import generate_signal

def run_analysis(ticker, interval, period):
    df, msg = load_intraday_data(ticker, interval, period)
    if df.empty:
        print("❌", msg)
        return
    df = compute_indicators(df)
    ha_df = heikin_ashi(df)
    X, y, features = prepare_ml_data(df)
    model, scaler, acc = train_ml(X, y)
    decision, pred, conf = generate_signal(df, ha_df, model, scaler, features)
    print(f"📈 {ticker} -> {decision} ({conf:.2%} confidence)")
