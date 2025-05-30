import numpy as np

def monte_carlo_simulation(df, runs=1000, window=20):
    returns = df['Close'].pct_change().dropna()
    if len(returns) < window:
        return 0.0, 0.015, "Insufficient data"
    simulated = [(np.prod(1 + np.random.choice(returns, window)) - 1) * 100 for _ in range(runs)]
    return np.mean(simulated), np.std(simulated), "Success"
