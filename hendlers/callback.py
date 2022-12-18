from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_number_2 = InlineKeyboardButton('next', callback_data='button_number_2')
    markup.add(button_number_2)
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
        type='quiz',
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Next', callback_data='button_number_3')
    markup.add(button)

    questions = 'колько будет 7 + 7'
    answers = [
        '14',
        '15',
        '13',
        '16'
    ]
    await bot.send_poll(
        call.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        correct_option_id=1,
        type='quiz',
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    question = 'кто?'
    answers = [
        'tesla',
        'pattison',
        'edvsrd'
        'enshtain'
    ]
    await bot.send_poll(
        call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        type='quiz'
    )


def reqister_hundler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_number_1')
    dp.register_callback_query_handler(quiz_3, text='button_number_2')
    dp.register_callback_query_handler(quiz_4, text='button_number_3')


