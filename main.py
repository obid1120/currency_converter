import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers.command_handlers import command_handlers
from handlers.message_handler import message_handlers


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start/restart bor"),
            BotCommand(command="help", description="Manual for using the bot"),
            BotCommand(command="courses", description="Currency courses"),
            BotCommand(command="usd", description="USD currency"),
            BotCommand(command="eur", description="EURO currency"),
            BotCommand(command="rub", description="Russian ruble currency"),
            BotCommand(command="/week", description="A week report")
        ]
    )
    dp = Dispatcher()
    dp.include_routers(command_handlers, message_handlers)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
