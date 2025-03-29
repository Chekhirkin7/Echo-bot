import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()

from app.handlers import router


async def main():
    bot = Bot(token=os.getenv("TELEGRAM_BOT_API"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot closed")
