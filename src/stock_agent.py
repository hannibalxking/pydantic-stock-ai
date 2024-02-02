"""
A Pydantic-based AI agent for fetching real-time stock prices using GROQ LLM.
"""
from pydantic_ai import Agent
from pydantic import BaseModel
import yfinance as yf

class StockPriceResult(BaseModel):
    symbol: str
    price: float
    currency: str = "USD"
    message: str

def create_stock_agent():
    """Create and configure the stock price AI agent."""
    stock_agent = Agent(
        "groq:llama3-groq-70b-8192-tool-use-preview",
        result_type=StockPriceResult,
        system_prompt="You are a helpful financial assistant that can look up stock prices. Use the get_stock_price tool to fetch current data."
    )

    @stock_agent.tool_plain
    def get_stock_price(symbol: str) -> dict:
        """
        Fetch the current stock price for a given symbol.
        
        Args:
            symbol (str): The stock symbol to look up

        Returns:
            dict: Dictionary containing price and currency information
        """
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info.last_price
        return {
            "price": round(price, 2),
            "currency": "USD"
        }

    return stock_agent

def get_stock_info(query: str) -> str:
    """
    Process a natural language query about stock prices.
    
    Args:
        query (str): Natural language question about stock prices

    Returns:
        str: Formatted response with stock information
    """
    try:
        stock_agent = create_stock_agent()
        result = stock_agent.run_sync(query)
        response = f"Stock: {result.data.symbol}\n"
        response += f"Price: ${result.data.price:.2f} {result.data.currency}\n"
        response += f"\n{result.data.message}"
        return response
    except Exception as e:
        return f"Error: {str(e)}"