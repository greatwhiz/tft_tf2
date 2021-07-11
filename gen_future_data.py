import pandas as pd

def main():
    df = pd.read_pickle("outputs/data/future_low/LSTM2048_Future_Prediction_15mins_future_20110101_20210501.pkl")
    df.drop(['volume'], axis=1, inplace=True)
    df.drop(['future_2'], axis=1, inplace=True)
    df.index = df.index.tz_localize(None)
    df["trade_date"] = df.index.strftime("%Y%m%d").astype("category")
    # df["trade_hour"] = df.index.strftime("%Y%m%d%H").astype("category")
    df["year"] = df.index.strftime("%Y").astype("category")
    df["month"] = df.index.strftime("%m").astype("category")
    df["day"] = df.index.strftime("%d").astype("category")
    df["hour"] = df.index.strftime("%H").astype("category")
    df["day_of_week"] = df.index.dayofweek.astype(str).astype("category")
    df["time_idx"] = pd.to_datetime(df.index).astype(int) / 10 ** 9
    df["time_idx"] -= df["time_idx"].min()
    df["time_idx"] /= 15 * 60
    df["time_idx"] = df["time_idx"].astype(int)
    df["type"] = "Forex"
    df.reset_index(inplace=True)
    #df.index.name = None
    df.to_csv("outputs/data/future_low/LSTM2048_Future_Prediction_15mins_future_20110101_20210501.csv")

if __name__ == "__main__":
    main()