from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

kb_main = [
    [
        KeyboardButton(text="/came_to_work"),
        KeyboardButton(text="/end_of_work")
        ],
    [
        KeyboardButton(text="/left_to_gym"),
        KeyboardButton(text="/back_to_work")
        ],
    [
        KeyboardButton(text="/edit_today"),
        KeyboardButton(text="/select_another_day")
        ],
    [
        KeyboardButton(text="/settings"),
        KeyboardButton(text="/help")
        ],
    ]

kb_edit_day = [
    [
        KeyboardButton(text="/edit_came_to_work"),
        KeyboardButton(text="/edit_end_of_work")
        ],
    [
        KeyboardButton(text="/edit_left_to_gym"),
        KeyboardButton(text="/edit_back_to_work")
        ],
    [
        KeyboardButton(text="/clear_today"),
        KeyboardButton(text="/clear_by_one")
        ],
    [
        KeyboardButton(text="/select_another_day"),
        KeyboardButton(text="/to_main_menu"),
        ],
    ]

kb_clear_by_one = [
    [
        KeyboardButton(text="/clear_came_to_work"),
        KeyboardButton(text="/clear_end_of_work")
        ],
    [
        KeyboardButton(text="/clear_left_to_gym"),
        KeyboardButton(text="/clear_back_to_work")
        ],
    [
        KeyboardButton(text="/select_another_day"),
        KeyboardButton(text="/to_main_menu"),
        ],
    ]

kb_settings = [
    [
        KeyboardButton(text="/start"),
        KeyboardButton(text="/help")
        ],
    [
        KeyboardButton(text="/get_my_id"),
        KeyboardButton(text="/get_table_url")
        ],
    [
        KeyboardButton(text="/to_main_menu"),
        KeyboardButton(text="/today_data"),
        ],
    ]

kb_select_day = [
    [
        KeyboardButton(text="/select_previous_month"),
        KeyboardButton(text=f"current_month"),
        KeyboardButton(text="/select_next_month")
        ],
    [
        KeyboardButton(text="pass"),
        KeyboardButton(text="pass")
        ],
    [
        KeyboardButton(text="/to_main_menu"),
        ],
    ]




def main():
    pass


if __name__ == '__main__':
    main()
