import requests

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.chat_action import ChatActionSender

from lesson10.config import currencies, CBU_URL


message_handlers = Router()


@message_handlers.message(F.text.isdigit())
async def message_handler(message: Message):
    x = int(message.text)
    s = f"{x} sums:\n"
    s += f"\t -{x / int(currencies['USD']['rate']): .2f} UD dollar\n"
    s += f"\t -{x / int(currencies['EUR']['rate']): .2f} Euro\n"
    s += f"\t -{x / int(currencies['RUB']['rate']): .2f} Russian ruble\n\n"

    s += f"Currency rates fetched from the below source"
    await message.reply(
        text=s,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Source',
                        url=CBU_URL
                    )
                ],
                [
                    InlineKeyboardButton(
                        text='Teacher',
                        url='https://t.me/SarvarAzim'
                    ),
                    InlineKeyboardButton(
                        text='Pupil',
                        url='https://t.me/Obidjon_Yoqubov'
                    ),
                ],
            ]
        )
    )
