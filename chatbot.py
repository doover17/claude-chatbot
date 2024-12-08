import os
from dotenv import load_dotenv
from anthropic import Anthropic
import sys

def initialize_claude():
    load_dotenv()
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)
    return Anthropic(api_key=api_key)

def chat_with_claude():
    client = initialize_claude()
    conversation_history = []
    
    print("Welcome to Claude Chatbot! (Type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            # Create the messages list with conversation history
            messages = [
                {"role": "user", "content": msg["content"]} if msg["role"] == "user" else
                {"role": "assistant", "content": msg["content"]}
                for msg in conversation_history
            ]
            messages.append({"role": "user", "content": user_input})
            
            # Send the message to Claude
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                messages=messages
            )
            
            # Get Claude's response
            assistant_message = response.content[0].text
            print("\nClaude:", assistant_message)
            
            # Update conversation history
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": assistant_message})
            
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    chat_with_claude()