from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start")],
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/about")],
        [KeyboardButton(text="/register")],
        [KeyboardButton(text="/echo")],
        [KeyboardButton(text="/stop")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select a menu item...",
)

help = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Start", callback_data="/start")],
        [InlineKeyboardButton(text="Help", callback_data="help")],
        [InlineKeyboardButton(text="About", callback_data="about")],
        [InlineKeyboardButton(text="Echo", callback_data="echo")],
    ]
)

get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Send phone", request_contact=True)]],
    resize_keyboard=True,
)
