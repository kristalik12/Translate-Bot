from loader import dp
from aiogram import types
from states.tarjima import Translate
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu2 import ozgar
from googletrans import Translator



@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == "🇺🇿 Uzb - 🇬🇧 Eng":
        tarjima = tarjimon.translate(text, dest="en")
        await message.answer(tarjima.text, reply_markup=ozgar)
    elif lang == "🇬🇧 Eng - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=ozgar)
    elif lang == "🇺🇿 Uzb - 🇷🇺 Rus":
        tarjima = tarjimon.translate(text, dest="ru")
        await message.answer(tarjima.text, reply_markup=ozgar)
    elif lang == "🇷🇺 Rus - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=ozgar)
    await Translate.trans.set()
    # await state.finish()