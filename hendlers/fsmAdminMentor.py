from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import ADMIN
from keybords import client_kb
from aiogram.dispatcher.filters import Text

class FsmAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()

async def start_fsm(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('не хватает прав')
        else:
            await FsmAdmin.id.set()
            await message.answer('Введите айди: ', reply_markup=client_kb.cancel_murcup)
    else:
        await message.answer('пиши в личке')

async def load_id(massage: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = massage.text
    await FsmAdmin.next()
    await massage.answer('введите имя: ')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FsmAdmin.next()
    await message.answer('Выберите направление: ', reply_markup=client_kb.dir_markup)


async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in ['python', 'java', 'cotlin']:
        await message.answer('Выбери что то из списка')
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FsmAdmin.next()
        await message.answer('Введите возраст: ', reply_markup=client_kb.cancel_murcup)

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('пиши тольео числа! ')
    elif int(message.text) < 9 or int(message.text) > 90:
        await message.answer('Ограничение! от 9 до 90')
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FsmAdmin.next()
        await message.answer('Введите группу: ', reply_markup=client_kb.group_murkup)

async def load_group(message: types.Message, state: FSMContext):
    if message.text not in ['python_1','python_2','java_1','java_2','cotlin_1','cotlin_2',]:
        await message.answer('Выберите группу из списка! ')
    else:
        async with state.proxy() as data:
            data['group'] = message.text
        await FsmAdmin.next()
        await message.answer('Хотите сохранить?', reply_markup=client_kb.submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await state.finish()
        await message.answer('Сохранено!')
    elif message.text == 'Нет':
        await state.finish()
        await message.answer('Удалено!')
    else:
        await message.answer('Что то не так :(')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_fsm = state.get_state()
    if current_fsm is not None:
        await state.finish()
        await message.answer('Отменено!')







def register_hundlers_FsmAdmin(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_fsm,Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm, commands=['add_mentor'])
    dp.register_message_handler(load_id, state=FsmAdmin.id)
    dp.register_message_handler(load_name, state=FsmAdmin.name)
    dp.register_message_handler(load_direction, state=FsmAdmin.direction)
    dp.register_message_handler(load_age, state=FsmAdmin.age)
    dp.register_message_handler(load_group, state=FsmAdmin.group)
    dp.register_message_handler(submit, state=FsmAdmin.submit)



