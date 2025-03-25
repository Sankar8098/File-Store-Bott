from bot import Bot

app = Bot()

async def main():
    await app.start()
    print("Bot started successfully!")

import asyncio
asyncio.run(main())
