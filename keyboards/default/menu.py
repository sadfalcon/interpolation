from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Качество воздуха"),
        ],
        [
            KeyboardButton(text="Температура"),
            KeyboardButton(text="Давление воздуха")
        ],
    ],
    resize_keyboard=True
)