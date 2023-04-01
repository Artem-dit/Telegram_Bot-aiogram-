
from aiogram import Bot, types, Dispatcher, executor
import MainMenuButtons as nav

TOKEN_API = '6227338945:AAHfDKPPsqk2fJPHCdWj6e-QTRsrgbFPOok'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_ikb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="wassap",
                           reply_markup=nav.btnTrainning)


@dp.message_handler()
async def bot_choose(message: types.Message):
    if message.text == 'План тренировок':
        await bot.send_message(message.from_user.id, 'Чем могу помочь', reply_markup=nav.btnCalendar)
    elif message.text == 'Недельный календарь':
        await bot.send_message(message.from_user.id, 'Что мы сегодня делаем', reply_markup=nav.btWEEKS)
    elif message.text == 'Годовой отчет':
        await bot.send_message(message.from_user.id, 'Отчеты по месяцам', reply_markup=nav.btnMNTH)
    elif message.text == 'Return':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.btnTrainning)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
