import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_data(path):
    return pd.read_csv(path)

if __name__ == '__main__':

    df = load_data("data.csv")
    df = df[["country", "views"]]
    df = df.sort_values("views", ascending=False).head(10)

    plt.style.use("ggplot")

    ax = plt.bar(df.country, df.views)

    date = datetime.today().strftime('%Y-%m-%d')

    plt.title(f"Eurovision 2021, Youtube views per country, {date}")

    plt.show()