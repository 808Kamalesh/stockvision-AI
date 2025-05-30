def generate_signal(df, ha_df, model, scaler, features):
    latest = df.iloc[-1:][features]
    scaled = scaler.transform(latest)
    pred = model.predict(scaled)[0]
    conf = max(model.predict_proba(scaled)[0])
    score = 0

    if pred == 1: score += 2
    if df['MACD'].iloc[-1] > df['Signal'].iloc[-1]: score += 1
    if df['RSI'].iloc[-1] < 30: score += 1
    if ha_df['HA_Trend'].iloc[-1] == 1: score += 1

    if score >= 4:
        return "STRONG BUY", pred, conf
    elif score >= 2:
        return "BUY", pred, conf
    elif score >= 0:
        return "HOLD", pred, conf
    else:
        return "SELL", pred, conf
