from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.utils.db_api.db import get_or_create_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    user, created = await get_or_create_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        language_code=message.from_user.language_code
    )

    if created:
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n"
            "Botimizga xush kelibsiz!\n"
            "Bot orqali siz bizga ma'lumotlaringizni yuborishingiz mumkin.\n"
        )
    else:
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n"
            "Sizni yana ko'rib turganimizdan xursandmiz\n"
        )


