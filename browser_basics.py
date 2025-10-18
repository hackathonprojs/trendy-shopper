from browser_use import Agent, Browser, ChatOpenAI

browser = Browser(
	headless=False,  # Show browser window
	window_size={'width': 1000, 'height': 700},  # Set window size
)

agent = Agent(
	task='Find the number 1 post on Show HN',
	browser=browser,
	llm=ChatOpenAI(model='gpt-4.1-mini'),
)


async def main():
	await agent.run()