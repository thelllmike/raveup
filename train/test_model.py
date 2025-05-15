import argparse
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error

def main(data_path, model_path, scaler_path):
    # 1) Load data
    df = pd.read_csv(data_path)
    # 2) Load model + scaler
    model  = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # 3) Prepare features exactly as in training
    X = df[['points', 'best_lap_time', 'total_wins']].copy()
    X['inv_lap_time'] = -X.pop('best_lap_time')
    X_scaled = scaler.transform(X)

    # 4) Predict
    preds = model.predict(X_scaled)
    # (optional) round to nearest int
    df['predicted_pos'] = preds.round().astype(int)
    df['error'] = (df['predicted_pos'] - df['finishing_position']).abs()

    # 5) Print a few rows
    print(df[['race_id','driver_id','points','total_wins',
              'finishing_position','predicted_pos','error']].head(10))

    # 6) Overall MAE
    mae = mean_absolute_error(df['finishing_position'], preds)
    print(f"\nOverall MAE on this dataset: {mae:.2f}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data_path",   type=str, default="season_data_100.csv",
                   help="CSV used for testing")
    p.add_argument("--model_path",  type=str, default="ranker_model.joblib",
                   help="Trained model file")
    p.add_argument("--scaler_path", type=str, default="scaler.joblib",
                   help="Feature scaler file")
    args = p.parse_args()
    main(args.data_path, args.model_path, args.scaler_path)
