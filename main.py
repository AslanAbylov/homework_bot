from aiogram import Bot, Dispatcher, types
import logging
from aiogram import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['quiz'])
async def quiz_1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button_number_1 = InlineKeyboardButton('NEXT', callback_data='button_number_1')
    markup.add(button_number_1)
    questions = 'сколько будет 5 + 5 ?'
    answers = [
        '55',
        '5',
        '10',
        '15'
    ]
    await bot.send_poll(
        massage.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        type='quiz',
        reply_markup=markup
    )

@dp.callback_query_handler(text='button_number_1')
async def quiz_2(call: types.CallbackQuery):
    questions = 'кто президент Кр'
    answers = [
        'Жапаров',
        'Путин',
        'Байдон',
        'Обама'
    ]
    await bot.send_poll(
        call.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        correct_option_id=0,
        type='quiz'
    )
@dp.message_handler(commands=['mem'])
async def mem_commands(massage: types.Message):
    photo = open('media/images.jfif', 'rb')
    await bot.send_photo(massage.from_user.id, photo=photo)


@dp.message_handler()
async def extra_echo(massage: types.Message):
    if massage.text.isnumeric():
        await bot.send_message(massage.from_user.id, int(massage.text) ** 2)
    else:
        await bot.send_message(massage.from_user.id, massage.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
