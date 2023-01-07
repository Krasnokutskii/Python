from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("Главное меню")

# --- Main meny ---
btnOne = KeyboardButton("Кнопка один")
btnOther = KeyboardButton("📚 Другое")
mainMeny = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnOther)

# --- Other meny --- 
btnTwo = KeyboardButton("Кнопка два")
btnThree = KeyboardButton("Кнопка три")
otherMeny = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTwo,btnThree, btnMain)