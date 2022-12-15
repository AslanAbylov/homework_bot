import logging
from aiogram import executor
from config import dp
from hendlers import client, callback, extra, admin

client.reqister_hendler_client(dp)
admin.reqister_admin_hundlers(dp)
callback.reqister_hundler_callback(dp)

# extra.reqister_hundlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)