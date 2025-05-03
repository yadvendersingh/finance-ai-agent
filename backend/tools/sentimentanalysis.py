from datetime import datetime, timedelta
import requests
import os

# 2. Sentiment Analysis
def analyze_sentiment(stock_symbol: str) -> dict:
    """Perform sentiment analysis on financial news for a stock."""
    
    currdate = datetime.now().strftime('%Y%m%dT%H%M')
    prevdate = (datetime.now() - timedelta(days=1)).strftime('%Y%m%dT%H%M')
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers='+stock_symbol+'&sort=LATEST&time_from='+prevdate+'&time_to='+currdate+'&apikey='+os.environ["ALPHAVANTAGE_API_KEY"]
    r = requests.get(url)
    data = r.json()
    return data