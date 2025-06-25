def run(df):
    expected_cols = {"Name", "Alter"}
    if not expected_cols.issubset(df.columns):
        raise ValueError("Erwartete Spalten fehlen")
    return "Daten validiert"