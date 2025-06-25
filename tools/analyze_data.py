def run(df):
    avg_age = df["Alter"].mean()
    return f"Durschnittsalter: {avg_age:.2f} Jahre"