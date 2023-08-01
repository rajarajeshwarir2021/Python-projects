import pandas as pd

df = pd.read_csv("data/TG_STAID000015.txt", skiprows=20, parse_dates=["    DATE"])