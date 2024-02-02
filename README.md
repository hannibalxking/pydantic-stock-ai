# 🚀 Pydantic Stock AI Assistant

A magical stock price assistant powered by GROQ LLM and Pydantic AI! This enchanted tool helps you fetch real-time stock prices using natural language queries, wrapped in a beautiful Gradio interface.

## 🌟 Overview

This mystical creation combines the power of:
- 🤖 GROQ's LLaMA 3 70B model for natural language understanding
- 📊 Yahoo Finance for real-time stock data
- 🎯 Pydantic for type safety
- 🌈 Gradio for a user-friendly interface

Ask about any stock price in plain English, and watch as the AI assistant fetches the latest market data for you!

## 🏰 Installation

First, summon the project to your local realm:

```bash
git clone https://github.com/${GITHUB_REPOSITORY}.git
cd pydantic-stock-ai
```

Create a mystical Python environment:

```bash
python -m venv venv
# On Windows
.\venv\Scripts\Activate
# On Unix or MacOS
source venv/bin/activate
```

Install the magical dependencies:

```bash
pip install -r requirements.txt
```

## 🔮 Setup

1. Obtain your GROQ API key from [Groq Cloud](https://console.groq.com)
2. Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and add your GROQ API key

## ⚔️ Usage

### Command Line Interface

Run the simple CLI version:

```python
from src.stock_agent import get_stock_info

result = get_stock_info("What is Apple's current stock price?")
print(result)
```

### Web Interface

Launch the enchanted web interface:

```bash
python src/app.py
```

Then visit `http://localhost:7860` in your browser to interact with the magical assistant!

## 🎭 Features

- 🗣️ Natural language queries for stock prices
- 📈 Real-time stock data fetching
- 🛡️ Type-safe responses with Pydantic
- 🎨 Beautiful web interface with Gradio
- 🔄 Automatic currency conversion (USD)

## 📜 Example Queries

- "What is Tesla's stock price right now?"
- "How much does one share of AAPL cost?"
- "Tell me the current price of Microsoft stock"
- "What's the latest price for Amazon shares?"

## 🧙‍♂️ Advanced Configuration

The stock agent can be customized by modifying the system prompt in `src/stock_agent.py`:

```python
system_prompt="You are a helpful financial assistant that can look up stock prices. Use the get_stock_price tool to fetch current data."
```

## ⚡ Performance Notes

The application uses GROQ's LLaMA 3 70B model, which provides fast and accurate responses. The stock data is fetched in real-time from Yahoo Finance, ensuring up-to-date information.

May your stocks always rise and your queries be answered swiftly! 🌟