# Claude Chatbot

A simple command-line chatbot application powered by Anthropic's Claude AI.

## Features

- Interactive chat interface with Claude-3
- Conversation history tracking
- Easy-to-use command-line interface
- Environment-based configuration

## Prerequisites

- Python 3.8 or higher
- Anthropic API key

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install anthropic python-dotenv
   ```
3. Create a `.env` file in the project root and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```

## Usage

Run the chatbot using:
```bash
python chatbot.py
```

- Type your messages and press Enter to chat with Claude
- Type 'quit' to exit the application

## Note

Make sure to replace the API key in the `.env` file with your actual Anthropic API key before running the application.