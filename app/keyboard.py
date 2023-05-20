from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# приветствующая клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('🎮 Сыграем', '📷 Редактировать фото').add('Код бота')

# клавиатура редактора фото
keyboard_photo_editor = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_photo_editor.add('Каталог')

# клавиатура игр
keyboard_for_games = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_for_games.row('🔢 Угадай число', '👾 Ролевая игра').add('⮉ Назад')


answer_options = ReplyKeyboardMarkup(resize_keyboard=True)
answer_options.row('№1', '№2')


action_with_photo = ReplyKeyboardMarkup(resize_keyboard=True)
action_with_photo.row('p1', 'p2', 'p3').row('p4', 'p5', 'p6').row('p7', 'p8', 'p9')
