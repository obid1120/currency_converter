import asyncio

import requests
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.chat_action import ChatActionSender

from lesson10.config import currencies, CBU_URL

# from config import

command_handlers = Router()


@command_handlers.message(CommandStart())
async def start_handler(message: Message):
    s = "Welcome to our <b> Currency Convertor Bot </b>\n\n"
    s += "For more information, click /help command"
    await message.answer(text=s)


@command_handlers.message(Command('help'))
async def help_handler(message: Message):
    s = "For using the bot, use these below commands\n\n"
    s += "/courses - for get a list of all courses\n"
    s += "/usd - for get USD courses\n"
    s += "/eur - for get EURO courses\n"
    s += "/rub - for get Russian ruble courses\n\n"

    s += "if you want to convert any sum, send curreny (only digits)"

    await message.reply(text=s)


@command_handlers.message(Command('courses', prefix="!#/"))
async def courses_handler(message: Message):
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        response = requests.get(CBU_URL)

        s = "Today's currency rate:\n\n"

        for currency in response.json():
            if currency['Ccy'] in currencies.keys():
                currencies[currency['Ccy']]['rate'] = currency['Rate']
                s += f"\t- 1 {currency['CcyNm_EN']}: {currency['Rate']} sums\n"

        await message.answer(text=s)


@command_handlers.message(Command('usd', prefix='#/!'))
async def usd_handler(message: Message):
    response = requests.get(f"{CBU_URL}USD/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} USD\n"

    await message.reply(s)


@command_handlers.message(Command('eur', prefix='#/!'))
async def eur_handler(message: Message):
    response = requests.get(f"{CBU_URL}EUR/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} USD\n"

    await message.reply(s)


@command_handlers.message(Command('rub', prefix='#/!'))
async def rub_handler(message: Message):
    response = requests.get(f"{CBU_URL}RUB/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} USD\n"

    await message.reply(s)
