from aiogram import Router, types
from aiogram.filters import CommandStart

from handlers.keyboards import start_button

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text="Assalomu aleykom!\n"
                              "Valyuta ayirboshlash",
                         reply_markup=start_button)