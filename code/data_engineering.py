import os
import sys
import subprocess
import pickle
import pandas as pd

class DataDownloader:
    def __init__(self, pickle_dir='../data', csv_dir='../data/csv'):
        self.pickle_dir = pickle_dir
        self.csv_dir = csv_dir
        self.ensure_yfinance()
        self.data_dict = {}

        # Create directories if they don't exist
        os.makedirs(self.pickle_dir, exist_ok=True)
        os.makedirs(self.csv_dir, exist_ok=True)

    @staticmethod
    def ensure_yfinance():
        try:
            import yfinance
        except ImportError:
            print("📦 yfinance not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])

    @staticmethod
    def convert_ticker_name(ticker):
        return ticker.replace('^', '').replace('=', '').replace('-', '').lower()

    def load_or_download_data(self, tickers, start, end):
        import yfinance as yf  # Safe after ensure_yfinance()

        try:
            data = yf.download(tickers, start=start, end=end, group_by='ticker')

            for ticker in tickers:
                if data[ticker].isnull().all().all():
                    raise ValueError(f"No data downloaded for {ticker}")

            for ticker in tickers:
                base_name = self.convert_ticker_name(ticker)
                df = data[ticker].copy()
                df.index.name = 'Date'
                self.data_dict[base_name] = df

                # Save as pickle
                with open(os.path.join(self.pickle_dir, f'{base_name}.pkl'), 'wb') as f:
                    pickle.dump(df, f)

                # Save as CSV
                df.to_csv(os.path.join(self.csv_dir, f'{base_name}.csv'))

            print("✅ Data downloaded and saved successfully.")

        except Exception as e:
            print(f"⚠️ Download failed. Loading from CSV instead. Reason: {e}")
            for ticker in tickers:
                base_name = self.convert_ticker_name(ticker)
                file_path = os.path.join(self.csv_dir, f'{base_name}.csv')
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
                    df.index.name = 'Date'
                    self.data_dict[base_name] = df
                else:
                    print(f"❌ Missing local file: {file_path}")

        return self.data_dict
