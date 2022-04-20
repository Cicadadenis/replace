import requests
from krd import sborka
import webbrowser
import os, sys
import urllib.parse
import urllib.request
import os, sys
import ssl
import time
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
import ftplib
from aiogram.dispatcher.filters.state import State, StatesGroup
import configparser, time, random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from pathlib import Path
from os.path import exists
from datetime import datetime
import requests, os
from io import BytesIO
import aiohttp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
from klava import menu, izm, otm, domenu, menu2, otm2
from string import ascii_letters, digits
import logging 
token = "5158911825:AAGwiyVjOgZn3VCOAOnpSY2RA-MPnypZF74"
bot = Bot(token=token,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

class PhotoStorage:
    def __init__(self, path: str):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if exists(self.path):
            with open(self.path) as file:
                return file.readlines()


async def upload_document(
    bot, doc: types.photo_size.PhotoSize or types.Document
) -> str:
    with await doc.download(BytesIO()) as file:

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
        )

        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            img_src = await response.json()

    return "http://telegra.ph/" + img_src[0]["src"]
baza = []
class akasil(StatesGroup):
    bot2 = State()
    otziv = State()
    biz = State()
    forum = State()
    bott = State()
    tex = State()
    oper = State()
    img1 = State()
    img2 = State()
    parol = State()




@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    imya = message.chat.first_name
    chat_id = message.chat.id
    if chat_id not in baza:
        await message.answer(
            f"<b>Привет  {imya} </b>\n\n"
            f"<b>Тебя Нет В Базе \nАвторизуйся Для Пользованиям Этим Ботом</b>\n\n")
        time.sleep(3)
        await message.answer("<b>Введи Пароль:  </b>")
        await akasil.parol.set()
    if chat_id in  baza:
        kar = open("otzyvonly.jpg", "rb").read()
        await bot.send_photo(chat_id, photo=kar)
        await message.answer("<b>Главное Меню !</b>", reply_markup=menu)



@dp.message_handler(state=akasil.parol)
async def gig(message: Message, state):
    kod = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    if kod == 'cicada':
        baza.append(message.chat.id)
        kar = open("otzyvonly.jpg", "rb").read()
        await message.answer("<b>Авторизация Подтвержденна</b>")
        time.sleep(3)
        await bot.send_photo(chat_id=message.chat.id, photo=kar)
        await message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !</b>', reply_markup=domenu)
        await state.finish()
    else:
        await message.answer("<b>Пароль Не Верен Отказанно В Доступе</b>")
        await state.finish()


@dp.callback_query_handler(text="oper")
async def oper(call: CallbackQuery):
    oper = open("oper.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ОПЕРАТОР Установлен\n"
        f"‼️ {oper} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.oper.set()

@dp.message_handler(state=akasil.oper)
async def gig(message: Message, state):
    oper = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {oper} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.oper, text="yes")
    async def oper(call: CallbackQuery, state):
        oper = message.text
        with open("oper.txt", "w", encoding="utf-8") as f:
            f.write(oper)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{oper}", reply_markup=menu)
        await state.finish()
        
    @dp.callback_query_handler(state=akasil.oper, text="no")
    async def oper(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()
###############################
@dp.callback_query_handler(text="bbb",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=menu)

########################

@dp.callback_query_handler(text="tex")
async def tex(call: CallbackQuery):
    tex = open("tex.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ТЕХПОДДЕРЖКА Установлен\n"
        f"{tex}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n", reply_markup=otm)
    await akasil.tex.set()

@dp.message_handler(state=akasil.tex)
async def tex(message: Message, state):
    tex = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {tex} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.tex, text="yes")
    async def tex(call: CallbackQuery, state):
        tex = message.text
        with open("tex.txt", "w", encoding="utf-8") as f:
            f.write(tex)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{tex}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.tex, text="no")
    async def tex(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()

########################################


@dp.callback_query_handler(text="bott")
async def bott(call: CallbackQuery):
    bott = open("bott.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку БОТ Установлен\n"
        f"{bott}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bott.set()

@dp.message_handler(state=akasil.bott)
async def bott(message: Message, state):
    bott = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {bott} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.bott, text="yes")
    async def bott(call: CallbackQuery, state):
        bott = message.text
        with open("bott.txt", "w", encoding="utf-8") as f:
            f.write(bott)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{bott}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.bott, text="no")
    async def bott(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()

############################

###############################

@dp.callback_query_handler(text="forum")
async def forum(call: CallbackQuery):
    forum = open("forum.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ФОРУМ Установлен\n"
        f"{forum}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.forum.set()

@dp.message_handler(state=akasil.forum)
async def forum(message: Message, state):
    forum = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {forum} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.forum, text="yes")
    async def forum(call: CallbackQuery, state):
        forum = message.text
        with open("forum.txt", "w", encoding="utf-8") as f:
            f.write(forum)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{forum}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.forum, text="no")
    async def forum(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()

############################
##########################################################

@dp.callback_query_handler(text="biz")
async def biz(call: CallbackQuery):
    biz = open("biz.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Сайт Biz Установлен\n"
        f"{biz}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.biz.set()

@dp.message_handler(state=akasil.biz)
async def biz(message: Message, state):
    biz = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {biz} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.biz, text="yes")
    async def biz(call: CallbackQuery, state):
        biz = message.text
        with open("biz.txt", "w", encoding="utf-8") as f:
            f.write(biz)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{biz}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.biz, text="no")
    async def biz(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()

#############################

#############################

@dp.callback_query_handler(text="otziv")
async def otziv(call: CallbackQuery):
    otziv = open("otziv.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ОТЗЫВЫ Установлен\n"
        f"{otziv}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.otziv.set()

@dp.message_handler(state=akasil.otziv)
async def otziv(message: Message, state):
    otziv = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {otziv} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.otziv, text="yes")
    async def otziv(call: CallbackQuery, state):
        otziv = message.text
        with open("otziv.txt", "w", encoding="utf-8") as f:
            f.write(otziv)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{otziv}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.otziv, text="no")
    async def otziv(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()


##################################################

##################################################
@dp.callback_query_handler(text="bot2")
async def bot2(call: CallbackQuery):
    bot2 = open("bot2.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Bot2 Установлен\n"
        f"{bot2}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bot2.set()

@dp.message_handler(state=akasil.bot2)
async def bot2(message: Message, state):
    bot2 = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {bot2} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.bot2, text="yes")
    async def bot2(call: CallbackQuery, state):
        bot2 = message.text
        with open("bot2.txt", "w", encoding="utf-8") as f:
            f.write(bot2)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{bot2}", reply_markup=menu)
        await state.finish()
    @dp.callback_query_handler(state=akasil.bot2, text="no")
    async def bot2(call: CallbackQuery, state):
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu)
        await state.finish()

###################################

###################################

@dp.callback_query_handler(text="img2")
async def img1(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("img1.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Логотип\n"
        f":Для изменения Логотипа Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img1.set()

@dp.message_handler(state=akasil.img1, content_types=types.ContentTypes.ANY)
async def img1(message: Message, state: FSMContext):
    ch = message.chat.id
    img1 = message.photo[-1]
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    photo_name = "img1.jpg"
    await message.photo[-1].download(f"{photo_name}")
    link = await upload_document(message.bot, img1)
    with open("img1.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("img1.jpg", "rb").read()
    ca = (f"Логотип Изменен  \n")
    sborka()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=menu)

####################################

####################################

@dp.callback_query_handler(text="img1")
async def img2(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("img2.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Фон\n"
        f":Для изменения Фона Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img2.set()

@dp.message_handler(state=akasil.img2, content_types=types.ContentTypes.ANY)
async def img2(message: Message, state: FSMContext):
    ch = message.chat.id
    img2 = message.photo[-1]
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    photo_name = "img2.jpg"
    await message.photo[-1].download(f"{photo_name}")
    link = await upload_document(message.bot, img2)
    with open("img2.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("img2.jpg", "rb").read()
    ca = (f"Фон Изменен  \n")
    sborka()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=menu)

####################################

if __name__ == '__main__':
    executor.start_polling(dp)
