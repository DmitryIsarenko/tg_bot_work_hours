import aiogram
import aiogram.utils.keyboard
from aiogram import Bot, Dispatcher, types, handlers, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import misc.google_pkg.pushing_to_gsheet
import misc.google_pkg.googleSheets
from misc.time_operations import get_time_now_tuple_H_M
from misc.telegram_pkg.tg_keyboards import kb_main, kb_edit_day, kb_select_day, kb_clear_by_one, kb_settings
from misc.constants import SPREADSHEET_URL

TOKEN = "6705142613:AAG1O41LMRRlbI1LKG454MN3OwBpB6oNcuw"
HELP = """
Данный бот разрабатывается для удобного учета рабочего времени.
    /start - start
    /help - help
Приятного пользования!
"""

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text, Command("help"))
async def help_func(message: Message) -> None:
    await message.answer(text=HELP)


@dp.message(F.text, Command("start"))
async def start_func(message: Message) -> None:
    await message.reply(text="Этот бот для удобного учета рабочего времени")
    # kb = [
    #     [
    #         KeyboardButton(text="/start"),
    #         KeyboardButton(text="/help")
    #         ],
    #     [
    #         KeyboardButton(text="/came_to_work"),
    #         KeyboardButton(text="/end_of_work")
    #         ],
    #     [
    #         KeyboardButton(text="/left_to_gym"),
    #         KeyboardButton(text="/back_to_work")
    #         ],
    #     [
    #         KeyboardButton(text="/clear_today"),
    #         KeyboardButton(text="/select_another_day")
    #         ],
    #     ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_main, resize_keyboard=True)
    await message.answer("Какую команду отправить боту?", reply_markup=keyboard)


# @dp.message(F.text == "/came_to_work")
# async def came_to_work(message: Message) -> None:
#     misc.google_pkg.pushing_to_gsheet.push_came_to_work()
#     print("пришел на работу")
#     await message.reply(text="Пришел на работу")





@dp.message(F.text == "/came_to_work")
async def came_to_work(message: Message) -> None:

    data = {
        "date_obj": ,
        "date_in_str": ,
        "month_in_str": ,
        "sh": ,
        "ws": ,
        "row_of_day": ,
        "col_to_push": ,
        }



    misc.google_pkg.pushing_to_gsheet.push_came_to_work()
    print("пришел на работу")
    today_data = {
        "sh": misc.google_pkg.googleSheets.get_spreadsheet(),
        "ws": misc.google_pkg.googleSheets.get_worksheet_with_title(),
        "today_date":None,
        "today_month_str":None,
        "time_in_tuple_H_M":None,
        "row_of_today":None,
        }
    await message.reply(text="Пришел на работу")


@dp.message(F.text == "/end_of_work")
async def end_of_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_left_work()
    print("ушел с работы")
    await message.reply(text="ушел с работы")


@dp.message(F.text == "/left_to_gym")
async def left_to_gym(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_went_to_gym()
    print("пошел в зал")
    await message.reply(text="пошел в зал")


@dp.message(F.text == "/back_to_work")
async def back_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_got_to_work_after_gym()
    print("вернулся после зала на работу")
    await message.reply(text="вернулся после зала на работу")


@dp.message(F.text == "/clear_today")
async def clear_today(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_clear_all_cells()
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
    misc.google_pkg.pushing_to_gsheet.push_clear_came_to_work()
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_end_of_work")
async def clear_end_of_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_clear_left_work()
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_left_to_gym")
async def clear_left_to_gym(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_clear_left_to_gym()
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/clear_back_to_work")
async def clear_back_to_work(message: Message) -> None:
    misc.google_pkg.pushing_to_gsheet.push_clear_back_to_work()
    print("очистить сегодняшние данные")
    await message.reply(text="очистить сегодняшние данные")


@dp.message(F.text == "/select_another_day")
async def select_another_day(message: Message) -> None:
    print("выбираем другой день")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_select_day, resize_keyboard=True)
    await message.reply(text="выбираем другой день", reply_markup=keyboard)


@dp.message(F.text == "/settings")
async def settings(message: Message) -> None:
    print("настройки")
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text="настройки", reply_markup=keyboard)


@dp.message(F.text == "/today_data")
async def settings(message: Message) -> None:
    print("сегодняшние данные")
    date = str(misc.time_operations.get_today_date())
    timestamp = str(misc.time_operations.get_time_now_tuple_H_M())
    month = str(misc.time_operations.get_current_month_in_ru_str())
    keyboard = ReplyKeyboardMarkup(keyboard=kb_settings)
    await message.reply(text="сегодняшние данные", reply_markup=keyboard)
    await message.reply(text=month, reply_markup=keyboard)
    await message.reply(text=date, reply_markup=keyboard)
    await message.reply(text=timestamp, reply_markup=keyboard)


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
