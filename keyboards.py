from aiogram import types
from config import *

welcome_kb = [
    [
        types.KeyboardButton(text=CREATE_MAIL_BUTTON),
    ],
]

WELCOME_KEYBOARD = types.ReplyKeyboardMarkup(
    keyboard=welcome_kb,
    resize_keyboard=True,
    input_field_placeholder="Действие..."
)

check_kb = [
    [
        types.KeyboardButton(text=CHECK_MAIL_BUTTON),
        types.KeyboardButton(text=BACK_BUTTON)
    ],
]

CHECK_MAIL_KEYBOARD = types.ReplyKeyboardMarkup(
    keyboard=check_kb,
    resize_keyboard=True,
    input_field_placeholder="Действие..."
)
