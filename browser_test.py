import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

from browser_use import Agent, Browser, BrowserConfig

browser = Browser(
    config=BrowserConfig(
        # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    )
)


async def main():
    llm=ChatOpenAI(model='gpt-4o')
    prompt=os.environ.get('AI_PROMPT')
    print(prompt)
    agent = Agent(
        task=prompt,
        llm=llm,
        browser=browser,
    )

    await agent.run()
    await browser.close()

    input('Press Enter to close...')


if __name__ == '__main__':
    asyncio.run(main())
