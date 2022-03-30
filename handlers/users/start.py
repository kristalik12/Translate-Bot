import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot

from keyboards.default.lang import menu
from states.tarjima import Translate

from data.config import CHANNELS
from keyboards.inline.obuna import check_button


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n\n"
                        f"{channels_format}",
                        reply_markup=check_button,
                        disable_web_page_preview=True)
    
