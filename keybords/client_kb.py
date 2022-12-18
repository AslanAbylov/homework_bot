from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



cancel_button = KeyboardButton('CANCEL')
cancel_murcup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)


dir_python_button = KeyboardButton('python')
dir_java_button = KeyboardButton('java')
dir_cotlin_button = KeyboardButton('cotlin')

dir_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
dir_markup.add(dir_python_button, dir_cotlin_button, dir_java_button, cancel_button)

group_1_python = KeyboardButton('python_1')
group_1_cotlin = KeyboardButton('cotlin_1')
group_1_java = KeyboardButton('java_1')
group_2_python = KeyboardButton('python_2')
group_2_cotlin = KeyboardButton('cotlin_2')
group_2_java = KeyboardButton('java_2')

group_murkup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(group_2_java,group_2_cotlin,group_1_java,group_2_python,group_1_cotlin,group_1_python, cancel_button)


submit_button_1 = KeyboardButton('Да')
submit_button_2 = KeyboardButton('Нет')
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(submit_button_1, submit_button_2)