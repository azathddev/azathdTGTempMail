import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import *
from keyboards import *
import mail

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

mails = dict()
ids = list()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(WELCOME_MESSAGE, reply_markup=WELCOME_KEYBOARD)


@dp.message(F.text == BACK_BUTTON)
async def back_button(message: types.Message):
    if mails.get(message.from_user.id):
        mail.delete(mails[message.from_user.id])
    await message.reply(BACK_MESSAGE, reply_markup=WELCOME_KEYBOARD)


@dp.message(F.text == CREATE_MAIL_BUTTON)
async def create_mail_button(message: types.Message):
    email = mail.create()
    mails[message.from_user.id] = email
    await message.reply(CREATED_MAIL_MESSAGE + email, reply_markup=CHECK_MAIL_KEYBOARD)


@dp.message(F.text == CHECK_MAIL_BUTTON)
async def check_mail_button(message: types.Message):
    if mails[message.from_user.id]:
        respond = mail.check(mails[message.from_user.id])
        if respond[1]:
            await message.reply(respond[0])
            for i in respond[1]:
                await message.reply(i)
        else:
            await message.reply(respond[0])


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
