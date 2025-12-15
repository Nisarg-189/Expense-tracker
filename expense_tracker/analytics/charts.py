import pandas as pd
import matplotlib.pyplot as plt
import os

def show_monthly_trend(expenses):
    if not expenses:
        print("No data to show")
        return

    os.makedirs("data/charts", exist_ok=True)

    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    monthly = df.groupby("month")["amount"].sum()

    plt.figure()
    monthly.plot(title="Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    filepath = "data/charts/monthly_spending.png"
    plt.savefig(filepath)
    plt.close()

    print(f"📊 Chart saved at: {filepath}")
