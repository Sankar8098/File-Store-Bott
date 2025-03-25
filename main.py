import asyncio
from bot import Bot

app = Bot()

async def main():
    await app.start()
    print("Bot started successfully!")
    await asyncio.Event().wait()  # Keeps the bot running

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
