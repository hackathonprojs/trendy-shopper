from browser_use import Agent, Browser, ChatOpenAI
import asyncio


async def main():

    # Connect to your existing Chrome browser
    browser = Browser(
        # executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # user_data_dir='~/Library/Application Support/Google/Chrome',
        # profile_directory='Default',
        cdp_url='http://localhost:9222',
    )

    agent = Agent(
        task='Visit https://duckduckgo.com and search for "browser-use founders"',
        browser=browser,
        llm=ChatOpenAI(model='gpt-4.1-mini'),
    )

    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
