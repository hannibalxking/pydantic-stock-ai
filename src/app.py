"""
Gradio web interface for the stock price AI agent.
"""
import gradio as gr
from stock_agent import get_stock_info

# Create the Gradio interface
demo = gr.Interface(
    fn=get_stock_info,
    inputs=gr.Textbox(
        label="Ask about any stock price",
        placeholder="What is Apple's current stock price?"
    ),
    outputs=gr.Textbox(label="Stock Information"),
    title="Stock Price AI Assistant",
    description="Ask me about any stock price and I'll fetch the latest information for you!"
)

if __name__ == "__main__":
    demo.launch()