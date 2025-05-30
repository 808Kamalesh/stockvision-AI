import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def prepare_ml_data(df):
    df['Label'] = np.where(df['Close'].shift(-1) > df['Open'], 1, -1)
    df = df.dropna()
    features = ['MACD', 'Signal', 'RSI', 'Boll_Upper', 'Boll_Lower']
    return df[features], df['Label'], features

def train_ml(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    model = RandomForestClassifier(n_estimators=50, max_depth=5)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    return model, scaler, acc
