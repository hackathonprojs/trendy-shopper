from browser_use import Agent, Browser, ChatOpenAI
import asyncio


async def main():

    # Connect to your existing Chrome browser
    # launch a browser first using this command:
#     /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
#   --remote-debugging-port=9222 \
#   --user-data-dir=/tmp/chrome-debug \
#   --no-first-run --no-default-browser-check
    browser = Browser(
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
