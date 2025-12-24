import pandas as pd

class CsvWriter:

    def write_transactions(self, data, filename):
        df = pd.DataFrame(
            data,
            columns=["Date", "Description", "Currency", "Amount"]
        )
        df.to_csv(filename, index=False)

    def write_customer(self, data, filename):
        df = pd.DataFrame([data])
        df.to_csv(filename, index=False)
