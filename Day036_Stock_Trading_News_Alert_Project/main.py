import requests
from smtp import send_mail


STOCK_NAME = "TSLA"
STOCK_API = "AQBNRF11BL6VT3X9"
NEWS_API = "0dd56424487e4306b656165723e96b97"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API,
}
response = requests.get("https://www.alphavantage.co/query", params=parameters_stock)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
stock_data = [v for (k, v) in stock_data.items()]

yesterday_close = stock_data[0]['4. close']
day_before_yesterday_close = stock_data[1]['4. close']

difference = abs(float(yesterday_close) - float(day_before_yesterday_close))

diff_percent = (difference / float(day_before_yesterday_close) * 100)

if diff_percent > 0:
    parameters_news = {
        "apiKey": NEWS_API,
        "q": STOCK_NAME,
    }

    response2 = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    response2.raise_for_status()
    news_data = response2.json()['articles'][:3]
    news_list = [{'title': f"{article['title']}", 'content': f"{article['content']}"} for article in news_data]

    for news in news_list:
        body = news['content'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u2026", "...")
        msg = f"Subject: {news['title']}\n\nBrief: {body}"
        send_mail("mcnmunoz@gmail.com", msg)
