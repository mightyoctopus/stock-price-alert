import requests
from dotenv import load_dotenv
import os

load_dotenv()
#---------------------------------------------- News API -------------------------------------------------#
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_LANG = "en"


response = requests.get(NEWS_ENDPOINT + f"?qInTitle=(tesla%20OR%20Elon%20musk%20)&from=2025-05-07&sortBy=publishedAt&language={NEWS_LANG}&qInTitle=%E2%80%9Ctesla%E2%80%9D&apiKey={NEWS_API_KEY}")
data = response.json()
latest_articles = data["articles"][:3]

def get_title(num: int):
    return latest_articles[num]["title"]

def get_brief(num: int):
    return latest_articles[num]["description"]

# print(get_title(1))
# print(get_brief(1))