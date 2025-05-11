import requests
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "TSLA"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

# print(data["Time Series (Daily)"])
close_prices = [value["4. close"] for index, value in data["Time Series (Daily)"].items()]
last_2_days_prices = close_prices[:2]

def check_price_change() -> float:
    #Calculate the percentage of price change by comparing between yesterday and previous day's close price
    percentage = ((float(last_2_days_prices[0]) - float(last_2_days_prices[1])) / float(last_2_days_prices[1])) * 100
    return round(percentage, 2)

