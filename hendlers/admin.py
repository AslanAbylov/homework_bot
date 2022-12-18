from config import bot, Dispatcher
from aiogram import types
from config import ADMIN
import random

async def game(massage: types.Message):

        if massage.from_user.id not in ADMIN:
            await massage.answer('Ты не админ!')
        elif massage.text.startswith('game'):
            emo = ['🎲', '🏀', '⚽️', '🎰', '🎳']
            await bot.send_dice(massage.chat.id, emoji=random.choice(emo))

def reqister_admin_hundlers(dp: Dispatcher):
    dp.register_message_handler(game)