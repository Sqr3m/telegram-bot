import Token
import Text
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = Token.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Приветсвенное сообщение пользователю
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(Text.commands)


# Требования к кандидату
@dp.message_handler(commands=['requirements'])
async def requirements(message: types.Message):
    await message.answer(Text.need)


# Информация о нас
@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.answer("{0}\n\n{1}\n\n{2}".format(Text.info, Text.chat, 
    Text.channel))


# Анкета для вступления в команду
@dp.message_handler(commands=['work'])
async def work(message: types.Message):
    await message.answer(Text.work)
    await message.answer(Text.work_anket_example)


# Предложения
@dp.message_handler(commands=['suggestion'])
async def suggestion(message: types.Message):
    await message.answer(Text.suggestion)
    await message.answer(Text.suggest_anket_example)


# Отправка анкеты
@dp.message_handler(commands=['anket'])
async def anket(message: types.Message):
    await message.forward()
    await message.answer("🎉 Твоя анкета на рассмотрении")


# Отправка предложения по улучшению/идея
@dp.message_handler(commands=['suggest'])
async def suggest(message: types.Message):
    await message.forward()
    await message.reply("🎉 Спасибо, {0}. Нам будет интересно почитать!"
    .format(message.from_user.first_name))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
