import datetime

import aiogram
import aiogram.utils.keyboard
from aiogram import Bot, Dispatcher, types, handlers, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import misc.google_pkg.pushing_to_gsheet
import misc.google_pkg.googleSheets
import misc.time_operations
from misc.telegram_pkg.tg_keyboards import kb_main, kb_edit_day, kb_clear_by_one, kb_settings
from misc.constants import SPREADSHEET_URL, STAGES, CLEARING_DATA, TOKEN, HELP

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text, Command("help"))
async def help_func(message: Message) -> None:
    await message.answer(text=HELP)


@dp.message(F.text, Command("start"))
async def start_func(message: Message) -> None:
    await message.reply(text="Этот бот для удобного учета рабочего времени")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_main, resize_keyboard=True)
    await message.answer("Какую команду отправить боту?", reply_markup=keyboard)


@dp.message(F.text == "/came_to_work")
async def came_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=misc.time_operations.get_time_now_in_str(),
        stage="came to work")
    print("пришел на работу")
    await message.reply(text="Пришел на работу")


@dp.message(F.text == "/end_of_work")
async def end_of_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=misc.time_operations.get_time_now_in_str(),
        stage="left work")
    print("ушел с работы")
    await message.reply(text="ушел с работы")


@dp.message(F.text == "/left_to_gym")
async def left_to_gym(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=misc.time_operations.get_time_now_in_str(),
        stage="went to gym")
    print("пошел в зал")
    await message.reply(text="пошел в зал")


@dp.message(F.text == "/back_to_work")
async def back_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=misc.time_operations.get_time_now_in_str(),
        stage="back_to_work")
    print("вернулся после зала на работу")
    await message.reply(text="вернулся после зала на работу")


@dp.message(F.text == "/clear_today")
async def clear_today(message: Message) -> None:
    for stage in STAGES:
        misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
            date_in_str=misc.time_operations.get_today_date_in_str(),
            time_in_str=CLEARING_DATA,
            stage=stage)
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/edit_today")
async def edit_today(message: Message) -> None:
    # misc.google_pkg.pushing_to_gsheet.push_clear_all_cells()
    print("редактировать сегодняшние данные")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_edit_day, resize_keyboard=True)
    await message.reply(text="редактировать сегодняшние данные", reply_markup=keyboard)


@dp.message(F.text == "/clear_by_one")
async def clear_by_one(message: Message) -> None:
    print("очистить данные поштучно")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_clear_by_one, resize_keyboard=True)
    await message.reply(text="очистить данные поштучно", reply_markup=keyboard)


@dp.message(F.text == "/clear_came_to_work")
async def clear_came_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=CLEARING_DATA,
        stage=STAGES[0])
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_left_to_gym")
async def clear_left_to_gym(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=CLEARING_DATA,
        stage=STAGES[1])
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_back_to_work")
async def clear_back_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=CLEARING_DATA,
        stage=STAGES[2])
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_end_of_work")
async def clear_end_of_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_some_data_to_some_cell(
        date_in_str=misc.time_operations.get_today_date_in_str(),
        time_in_str=CLEARING_DATA,
        stage=STAGES[3])
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/settings")
async def settings(message: Message) -> None:
    print("настройки")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text="настройки", reply_markup=keyboard)


@dp.message(F.text == "/today_data")
async def settings(message: Message) -> None:
    date = misc.time_operations.get_today_date_in_str()
    timestamp = misc.time_operations.get_time_now_in_str()
    month = misc.time_operations.get_month_in_ru_str_from_datetime(
        date=datetime.datetime.now())
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text="сегодняшние данные", reply_markup=keyboard)
    await message.answer(text=month, reply_markup=keyboard)
    await message.answer(text=date, reply_markup=keyboard)
    await message.answer(text=timestamp, reply_markup=keyboard)
    print("сегодняшние данные")


@dp.message(F.text == "/to_main_menu")
async def to_main_menu(message: Message) -> None:
    print("в главное меню")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_main)
    await message.reply(text="в главное меню", reply_markup=keyboard)


@dp.message(F.text == "/get_table_url")
async def send_table_url(message: Message) -> None:
    print("отправляем ссылку на таблицу")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text=SPREADSHEET_URL, reply_markup=keyboard)


@dp.message(F.text == "/get_my_id")
async def send_user_id(message: Message) -> None:
    print("отправляем id пользователя")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text=f"Ваш ID: {message.from_user.id}", keyboard=keyboard)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())

if __name__ == '__main__':
    pass
