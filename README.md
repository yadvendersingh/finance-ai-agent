# Finance AI Agent

Welcome! This project provides a conversational AI agent, similar to chatbots like Gemini or ChatGPT, but focused on providing financial market information. You can ask it about stocks, get recent news sentiment, and receive basic investment recommendations through a simple chat interface.

## What it Does (Features)

* **Chat Interface:** Easy-to-use web chat to talk to the agent.
* **Stock Data:** Fetches current overview data for requested stock symbols (e.g., AAPL, GOOG).
* **News Sentiment:** Analyzes recent news sentiment related to specific stocks.
* **Basic Recommendations:** Offers simple buy/sell/hold suggestions based on common financial metrics and news sentiment.

## Getting Started: Setup Instructions

Follow these steps to get the Finance AI Agent running on your own computer.

### Prerequisites

1.  **Python:** You need Python installed (version 3.9 or newer is recommended). You can download it from [python.org](https://www.python.org/).
2.  **Node.js & npm:** Needed for the chat interface. Download from [nodejs.org](https://nodejs.org/).
3.  **Alpha Vantage API Key:** The agent uses Alpha Vantage for financial data. Get a free API key here: [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key). **You will need this key!**
4.  **Git:** To download the project files. ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)).

### Steps

1.  **Download the Code:**
    Open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/yadvendersingh/finance-ai-agent.git with the actual URL
    cd finance-ai-agent          # Navigate into the downloaded folder
    ```

2.  **Set up the Backend (The "Brain"):**
    * Navigate to the backend folder:
        ```bash
        cd backend
        ```
    * Create a Python virtual environment (keeps things tidy):
        ```bash
        python -m venv venv
        ```
    * Activate the virtual environment:
        * **macOS / Linux:** `source venv/bin/activate`
        * **Windows:** `venv\Scripts\activate`
    * Install the required Python packages:
        ```bash
        pip install -r requirements.txt
        ```
    * **IMPORTANT: Add your API Key:** Create a file named `.env` (just `.env`, no name before the dot) inside the `backend` folder. Open this file in a text editor and add your Alpha Vantage API key like this:
        ```env
        ALPHAVANTAGE_API_KEY=YOUR_ACTUAL_API_KEY_HERE
        ```
        Replace `YOUR_ACTUAL_API_KEY_HERE` with the key you got from Alpha Vantage. Save the file.

3.  **Set up the Frontend (The Chat Window):**
    * Navigate to the frontend folder from the main project directory:
        ```bash
        cd ../frontend
        ```
    * Install the required Node.js packages:
        ```bash
        npm install
        ```

## Running the Finance AI Agent

You need to run both the backend and the frontend simultaneously.

1.  **Start the Backend:**
    * Make sure you are in the `backend` directory in your terminal.
    * Make sure your virtual environment is activated (you should see `(venv)` at the start of your terminal prompt).
    * Run the backend server:
        ```bash
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
        ```
    * Leave this terminal running.

2.  **Start the Frontend:**
    * Open a **new** terminal window or tab.
    * Navigate to the `frontend` directory:
        ```bash
        cd path/to/your/finance-ai-agent/frontend # Adjust path if needed
        ```
    * Run the frontend application:
        ```bash
        npm start
        ```
    * This should automatically open the chat interface in your web browser (usually at `http://localhost:3000`). If not, open your browser and go to that address.

## How to Use

Once the frontend opens in your browser, you can start typing questions into the chatbox at the bottom. Try asking things like:

* "What is the stock overview for GOOG?"
* "Analyze news sentiment for NVDA"
* "Give me an investment recommendation for AMZN"

The agent will process your request and provide a response in the chat window.
