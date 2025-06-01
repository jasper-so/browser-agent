#!/usr/bin/env python3
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import asyncio
import argparse
import os
import sys

load_dotenv()

def parse_args():
    parser = argparse.ArgumentParser(description='Browser Agent CLI')
    parser.add_argument('--url', type=str, required=True,
                      help='URL to open in the browser')
    parser.add_argument('--task', type=str, required=True,
                      help='Task description for the agent')
    parser.add_argument('--logs-path', type=str, default='./logs/conversation',
                      help='Path to save conversation logs (default: ./logs/conversation)')
    parser.add_argument('--model', type=str, default='gpt-4',
                      help='OpenAI model to use (default: gpt-4)')
    parser.add_argument('--use-vision', action='store_true',
                      help='Enable vision capabilities')
    return parser.parse_args()

async def run_agent(url: str, task: str, logs_path: str, model: str, use_vision: bool):
    llm = ChatOpenAI(model=model)
    
    initial_actions = [
        {'open_tab': {'url': url}},
    ]

    # Ensure logs directory exists
    os.makedirs(os.path.dirname(logs_path), exist_ok=True)

    agent = Agent(
        task=task,
        llm=llm,
        initial_actions=initial_actions,
        use_vision=use_vision,
        save_conversation_path=logs_path,
    )
    result = await agent.run()
    print(result)

def main():
    try:
        args = parse_args()
        asyncio.run(run_agent(
            url=args.url,
            task=args.task,
            logs_path=args.logs_path,
            model=args.model,
            use_vision=args.use_vision
        ))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 