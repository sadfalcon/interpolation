from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
import requests

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Введите число")

@dp.message_handler()
async def echo(message: Message):
    coeff = [{5: 1, 6: 0.51, 9: 0.38, 12: 0.32, 15: 0.29, 18: 0.26, 24: 0.24, 40: 0.2, 60: 0.18, 100: 0.16, 200: 0.14,
              400: 0.13}]
    x1 = message.text
    x1=int(x1)
    def opred(x1):
        if 6 < x1 < 9:
            x0 = 6
            x2 = 9
            y0 = 0.51
            y2 = 0.38
        elif 9 < x1 < 12:
            x0 = 9
            x2 = 12
            y0 = 0.38
            y2 = 0.32
        elif 12 < x1 < 15:
            x0 = 12
            x2 = 15
            y0 = 0.32
            y2 = 0.29
        elif 15 < x1 < 18:
            x0 = 15
            x2 = 18
            y0 = 0.29
            y2 = 0.26
        elif 18 < x1 < 24:
            x0 = 18
            x2 = 24
            y0 = 0.26
            y2 = 0.24
        elif 24 < x1 < 40:
            x0 = 24
            x2 = 40
            y0 = 0.24
            y2 = 0.2
        elif 40 < x1 < 60:
            x0 = 40
            x2 = 60
            y0 = 0.2
            y2 = 0.18
        elif 60 < x1 < 100:
            x0 = 60
            x2 = 100
            y0 = 0.18
            y2 = 0.16
        elif 100 < x1 < 200:
            x0 = 100
            x2 = 200
            y0 = 0.16
            y2 = 0.14
        elif 200 < x1 < 400:
            x0 = 200
            x2 = 400
            y0 = 0.14
            y2 = 0.13
        print(x0)
        print(x2)
        print(y0)
        print(y2)
        print(((int(x1) - int(x0)) / (int(x2) - int(x0)) * (y2 - y0)) + y0)
        return (((int(x1) - int(x0)) / (int(x2) - int(x0)) * (y2 - y0)) + y0)

    def inter(x1):
        if x1 in coeff[0]:
            print(coeff[0][x1])
            return (coeff[0][x1])
        else:
            return opred(x1)


    y1=inter(x1)
    await message.reply(text=y1)