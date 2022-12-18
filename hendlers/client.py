from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot




# @dp.message_handler(commands=['mem'])
async def mem_commands(massage: types.Message):
    photo = open('media/images.jfif', 'rb')
    await bot.send_photo(massage.from_user.id, photo=photo)

# @dp.message_handler(commands=['quiz'])
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

async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('сообщение должно быть ответом')

def reqister_hendler_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_commands, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')

