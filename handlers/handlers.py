from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Valyuta ayirboshlash botiga xush kelibsiz!")