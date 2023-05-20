from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from app import keyboard as kb
from PIL import Image, ImageFilter
import requests
import random
import time
import io
import os


TOKEN_API = '5656352107:AAHqbDVULliROBC_kVKk_fbBITtdliVmQ58'

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

secret_number = random.randint(0, 10)
print(secret_number)
game_ended = False


async def on_startup(_):
    print("Бот вышел в онлайн")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=kb.keyboard)


@dp.message_handler(lambda message: message.text == "🎮 Сыграем")
async def game(message: types.Message):
    await message.answer("Во что сыграем?", reply_markup=kb.keyboard_for_games)


@dp.message_handler(lambda message: message.text == "⮉ Назад")
async def back(message: types.Message):
    await message.answer("Изначальное меню.", reply_markup=kb.keyboard)


@dp.message_handler(lambda message: message.text == "🔢 Угадай число")
async def guess_the_number(message: types.Message):
    await message.answer("Я загадал число от 0 до 10.")
    await message.reply("Пожалуйста, введите число от 0 до 10.")


@dp.message_handler(lambda message: message.text == "👾 Ролевая игра")
async def role_playing_game(message: types.Message):
    await message.answer('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй —
жадный и голодный дракон, который мигом вас съест.
''')
    await message.answer('В какую пещеру вы войдете? (нажмите клавишу №1 или №2)', reply_markup=kb.answer_options)


@dp.message_handler(commands=['1', '2'], commands_prefix=['№'])
async def answer_options(message: types.Message):
    await message.answer('Вы приближаетесь к пещере...')
    time.sleep(2)
    await message.answer('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    await message.answer('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if message.text == '№' + str(friendlyCave):
        await message.answer('...делится с вами своими сокровищами!', reply_markup=kb.keyboard)
    else:
        await message.answer('...моментально вас съедает!', reply_markup=kb.keyboard)


@dp.message_handler(lambda message: message.text == "📷 Редактировать фото")
async def edit_photo(message: types.Message):
    await message.reply("Пришлите фото которое вам надо изменить.")


@dp.message_handler(commands=['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SMOOTH', '#SMOOTH_MORE', 'SHARPEN'], commands_prefix=['#'])
async def answer_options(message: types.Message):
    if message.text == '#BLUR':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.BLUR)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#CONTOUR':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.CONTOUR)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#DETAIL':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.DETAIL)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#EDGE_ENHANCE':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.EDGE_ENHANCE)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#EDGE_ENHANCE_MORE':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#EMBOSS':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.EMBOSS)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#FIND_EDGES':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.FIND_EDGES)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#SMOOTH':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.SMOOTH)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#SMOOTH_MORE':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.SMOOTH_MORE)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)

    if message.text == '#SHARPEN':
        img = Image.open('static/photo.png')

        treatment = img.filter(ImageFilter.SHARPEN)
        treatment.save('static/modified photo.png')
        await bot.send_photo(chat_id=message.chat.id, photo=open('static/modified photo.png', 'rb'), reply_markup=kb.keyboard)


@dp.message_handler(lambda message: message.text == "Код бота")
async def edit_photo(message: types.Message):
    await message.reply('''Код бота можно посмотреть на моём Get Hub:
https://github.com/rafael-917854632/bot''')


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def game(message: types.Message):
    text = message.text
    if text.isdigit():
        global secret_number, game_ended

        if game_ended:
            return

        try:
            guess = int(message.text)

            if guess == secret_number:
                await message.answer("Поздравляю, вы угадали число!", reply_markup=kb.keyboard)
                game_ended = True
            elif guess < secret_number:
                await message.answer("Загаданное число больше вашего.")
            else:
                await message.answer("Загаданное число меньше вашего.")
        except ValueError:
            await message.answer("Пожалуйста, введите число от 0 до 10.")

    else:
        await message.answer("""Я вас не понимаю.
Просьба пользоваться клавиатурой.""")


URI_INFO = f'https://api.telegram.org/bot{TOKEN_API}/getFile?file_id='
URI = f'https://api.telegram.org/file/bot{TOKEN_API}/'


@dp.message_handler(content_types=['photo'])
async def process_photo(msg: types.Message):
    file_id = msg.photo[3].file_id
    resp = requests.get(URI_INFO + file_id)
    img_path = resp.json()['result']['file_path']
    img = requests.get(URI+img_path)
    img = Image.open(io.BytesIO(img.content))
    if not os.path.exists('static'):
        os.mkdir('static')
    img.save(f'static/photo.png', format='PNG')

    await msg.answer('Выберите что надо сделать:', reply_markup=kb.action_with_photo)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
