import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
from aiogram.filters import Command
from aiogram.types import Message
from handlers.handlers import router as handler_router


from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
