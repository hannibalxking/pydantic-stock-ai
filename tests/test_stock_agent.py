"""
Tests for the stock price AI agent.
"""
import pytest
from src.stock_agent import get_stock_info, create_stock_agent

def test_get_stock_info_valid_query():
    """Test that a valid stock query returns expected format."""
    result = get_stock_info("What is Apple's stock price?")
    assert isinstance(result, str)
    assert "Stock:" in result
    assert "Price: $" in result
    assert "USD" in result

def test_get_stock_info_invalid_query():
    """Test that an invalid query returns an error message."""
    result = get_stock_info("What is the meaning of life?")
    assert "Error:" in result

def test_create_stock_agent():
    """Test that stock agent creation is successful."""
    agent = create_stock_agent()
    assert agent is not None
    assert hasattr(agent, 'run_sync')