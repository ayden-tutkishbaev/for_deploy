import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import admins, group, chat

TOKEN = '6960108312:AAE5u6VCv6kJtaPKsTBo23KXOnO_kUdKdBM'


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_routers(
        admins.rt,
        chat.rt,
        group.rt
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # stories_table()
    # create_languages_table()
    # eng_stories_table()
    # rus_stories_table()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("THE BOT IS OFF")