import pandas as pd


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("files/data.csv")
        result = tuple(df.loc[df["word"] == self.term]["definition"])

        return result