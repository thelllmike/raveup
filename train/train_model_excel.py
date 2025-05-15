import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

def load_data(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in ('.xls', '.xlsx'):
        return pd.read_excel(path)
    elif ext == '.csv':
        return pd.read_csv(path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def main(data_path, model_path, scaler_path):
    # 1) Load your Excel/CSV
    df = load_data(data_path)
    # must have: race_id, driver_id, points, best_lap_time, total_wins, finishing_position

    # 2) Build feature matrix & target
    X = df[['points', 'best_lap_time', 'total_wins']].copy()
    y = df['finishing_position']

    # 2a) invert lap time so higher → better
    X['inv_lap_time'] = -X.pop('best_lap_time')

    # 3) Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # 4) Train/Test split
    Xtr, Xte, ytr, yte = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # 5) Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(Xtr, ytr)

    # 6) Evaluate
    preds = model.predict(Xte)
    mae = mean_absolute_error(yte, preds)
    print(f"Test MAE on finishing_position: {mae:.2f}")

    # 7) Save artifacts
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Saved model → {model_path}")
    print(f"Saved scaler → {scaler_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Train driver-ranking regressor from Excel/CSV")
    p.add_argument("--data_path",   type=str, default="season_data_100.xlsx",
                   help="Path to your .xlsx/.xls/.csv file with columns: points,best_lap_time,total_wins,finishing_position")
    p.add_argument("--model_path",  type=str, default="ranker_model.joblib",
                   help="Where to save the trained model")
    p.add_argument("--scaler_path", type=str, default="scaler.joblib",
                   help="Where to save the feature scaler")
    args = p.parse_args()
    main(args.data_path, args.model_path, args.scaler_path)
