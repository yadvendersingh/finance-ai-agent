import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from tools.marketanalysis import fetch_market_data, investment_strategy
from tools.sentimentanalysis import analyze_sentiment

class Agent:
    def __init__(self, useAPI = False, model_name="llama3.2:3b"):
        if useAPI:
            model = ChatOpenAI(model="gpt-4o")
        else:
            model = ChatOllama(
                model=model_name,
                temperature=0,
            )
        # Market Data Agent
        market_data_expert = create_react_agent(
            model=model,
            tools=[fetch_market_data],
            name="market_data_expert",
            prompt="You are an expert in stock market data. Fetch stock data when requested."
        )

        # Sentiment Analysis Agent
        sentiment_expert = create_react_agent(
            model=model,
            tools=[analyze_sentiment],
            name="sentiment_expert",
            prompt="You analyze financial news and social media sentiment for stock symbols."
        )

        # Investment Strategy Agent
        strategy_expert = create_react_agent(
            model=model,
            tools=[investment_strategy],
            name="strategy_expert",
            prompt="You make investment recommendations based on market and news sentiment."
        )

        ### --- SUPERVISOR AGENT --- ###

        market_supervisor = create_supervisor(
            agents=[market_data_expert, sentiment_expert, strategy_expert],
            model=model,
            prompt=(
                "You are a financial market supervisor managing four expert agents: market data, sentiment, "
                "quantitative analysis, and investment strategy. For stock queries and price analysis, use market_data_expert. "
                "For news/social sentiment, use sentiment_expert."
                "For final investment recommendations, use strategy_expert."
            )
        )

        # Compile into an executable workflow
        self.advisor = market_supervisor.compile()