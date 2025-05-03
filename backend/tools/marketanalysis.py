import os
import requests

# 1. Fetching Market Data
def fetch_market_data(stock_symbol: str) -> dict:
    """Simulate fetching stock market data for a given symbol."""
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+stock_symbol+'&apikey='+os.environ["ALPHAVANTAGE_API_KEY"]
    r = requests.get(url)
    data = r.json()
    del data['Description']
    del data['Address']
    del data['OfficialSite']
    return data

def investment_strategy(stock_symbol, stock_data, news_feed):
    """Generate a recommendation based on the stock market data and news sentiment."""
    recommendations = []

    # Criteria 1: P/E Ratio
    pe_ratio = float(stock_data["PERatio"])
    if pe_ratio < 20:
        recommendations.append("Buy (Low P/E Ratio)")
    elif pe_ratio > 30:
        recommendations.append("Sell (High P/E Ratio)")

    # Criteria 2: Dividend Yield
    dividend_yield = float(stock_data["DividendYield"])
    if dividend_yield > 0.02:
        recommendations.append("Buy (High Dividend Yield)")
    elif dividend_yield < 0.01:
        recommendations.append("Sell (Low Dividend Yield)")

    # Criteria 3: Analyst Ratings
    strong_buy = int(stock_data["AnalystRatingStrongBuy"])
    buy = int(stock_data["AnalystRatingBuy"])
    hold = int(stock_data["AnalystRatingHold"])
    sell = int(stock_data["AnalystRatingSell"])
    strong_sell = int(stock_data["AnalystRatingStrongSell"])

    if strong_buy + buy > hold + sell + strong_sell:
        recommendations.append("Buy (Positive Analyst Ratings)")
    else:
        recommendations.append("Sell (Negative Analyst Ratings)")

    # Criteria 4: 52-Week High/Low
    current_price = float(stock_data["50DayMovingAverage"])
    week_52_high = float(stock_data["52WeekHigh"])
    week_52_low = float(stock_data["52WeekLow"])

    if current_price < (week_52_low + (week_52_high - week_52_low) * 0.25):
        recommendations.append("Buy (Near 52-Week Low)")
    elif current_price > (week_52_high - (week_52_high - week_52_low) * 0.25):
        recommendations.append("Sell (Near 52-Week High)")

    sentiment_scores = [item["ticker_sentiment_score"] for item in news_feed["feed"] if item["ticker_sentiment"][0]["ticker"] == stock_symbol]
    if sentiment_scores:
        avg_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
        if avg_sentiment_score >= 0.35:
            recommendations.append("Buy (Bullish News Sentiment)")
        elif avg_sentiment_score >= 0.15:
            recommendations.append("Buy (Somewhat-Bullish News Sentiment)")
        elif avg_sentiment_score <= -0.35:
            recommendations.append("Sell (Bearish News Sentiment)")
        elif avg_sentiment_score <= -0.15:
            recommendations.append("Sell (Somewhat-Bearish News Sentiment)")
    return f"Recommendation for {stock_symbol}: {recommendations}"