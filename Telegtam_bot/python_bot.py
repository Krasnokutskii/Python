import logging
from aiogram import executor, Dispatcher, Bot, types
import meny as telegram_meny
import ai

#initialization. 
bot = Bot("5952045084:AAFsYKhMPFAWoi4K3z-L_HOpWSIgT44HEQg")
dp = Dispatcher(bot)

#handlers
@dp.message_handler(commands="start")
async def start(message: types.message) -> None:
    await bot.send_message(message.from_user.id, " function start "+ message.from_user.first_name, reply_markup= telegram_meny.mainMeny)

@dp.message_handler()
async def just_message(message: types.Message) -> None:
    if message.text == telegram_meny.btnOne.text:
        await message.reply("отвечаю вам в смс, вы нажали кнопку один")

    elif message.text == telegram_meny.btnTwo.text:
        await bot.send_message(message.from_user.id, "вы нажали кнопку два")

    elif message.text == telegram_meny.btnThree.text:
        await bot.send_message(message.from_user.id, "вы нажали на кнопку три")

    elif message.text == telegram_meny.btnOther.text:
        await bot.send_message(message.from_user.id, "вы нажали другое", reply_markup= telegram_meny.otherMeny)
    
    elif message.text == telegram_meny.btnMain.text:
        await bot.send_message(message.from_user.id, "вы нажали мейн", reply_markup= telegram_meny.mainMeny)

    elif message.text != "a":
        ansver = ai.ask(message.text)
        print(ansver)
        await bot.send_message(message.from_user.id, ansver)

#main loop?
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)