# from misc.googleSheets import get_spreadsheet, get_row_of_today, update_cell_with_data
# from misc.time_operations import get_today_date, get_time_tuple_now, get_current_month_in_ru_str
# import constants

# import constants
from misc.google_pkg import googleSheets
from misc import time_operations
from pprint import pprint


clearing_data = ("", "",)

today_data = {
    # "sh":None,
    # "ws":None,
    # "today_date":None,
    # "today_month_str":None,
    # "time_in_tuple_H_M":None,
    # "row_of_today":None,
    }



"""
создать словарь, придумать его наполнение
методы наполнения словаря от даты и времени
sh
date > имя месяца > ws > дата в str > row >  >
"""



def get_sh_data():
    pass



def get_now_data() -> dict:
    sh = googleSheets.get_spreadsheet()
    ws = sh.worksheet(title=time_operations.get_current_month_in_ru_str())
    today_date = time_operations.get_today_date()
    today_month_str = time_operations.get_current_month_in_ru_str()
    time_in_tuple_H_M = time_operations.get_time_now_tuple_H_M()
    row_of_today = googleSheets.get_row_of_today(ws=ws, today=today_date)

    today_data["sh"] = sh
    today_data["ws"] = ws
    today_data["today_date"] = today_date
    today_data["today_month_str"] = today_month_str
    today_data["time_in_tuple_H_M"] = time_in_tuple_H_M
    today_data["row_of_today"] = row_of_today

    pprint(today_data)

    return today_data


def get_data(date: str) -> dict:
    sh = googleSheets.get_spreadsheet()
    ws = sh.worksheet(title=time_operations.get_current_month_in_ru_str())
    today_date = time_operations.get_today_date()
    today_month_str = time_operations.get_current_month_in_ru_str()
    time_in_tuple_H_M = time_operations.get_time_now_tuple_H_M()
    row_of_today = googleSheets.get_row_of_today(ws=ws, today=today_date)

    today_data["sh"] = sh
    today_data["ws"] = ws
    today_data["today_date"] = today_date
    today_data["today_month_str"] = today_month_str
    today_data["time_in_tuple_H_M"] = time_in_tuple_H_M
    today_data["row_of_today"] = row_of_today

    pprint(today_data)

    return today_data


def push_came_to_work(*, day_data: dict = get_now_data()):
    # day_data = get_now_data()
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_CAME_TO_WORK_H,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][0]
                                       )
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_CAME_TO_WORK_M,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][1]
                                       )


def push_went_to_gym(*, day_data: dict = get_now_data()):
    # day_data = get_now_data()
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_H,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][0]
                                       )
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_M,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][1]
                                       )


def push_got_to_work_after_gym(*, day_data: dict = get_now_data()):
    # day_data = get_now_data()
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_H,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][0]
                                       )
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_M,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][1]
                                       )


def push_left_work(*, day_data: dict = get_now_data()):
    # day_data = get_now_data()
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_LEFT_WORK_H,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][0]
                                       )
    googleSheets.update_cell_with_data(ws=day_data["ws"],
                                       cell_col=googleSheets.CELL_COL_LEFT_WORK_M,
                                       cell_row=day_data["row_of_today"],
                                       data=day_data["time_in_tuple_H_M"][1]
                                       )


def push_clear_all_cells():
    clearing_day_data = get_now_data()
    clearing_day_data["time_in_tuple_H_M"] = clearing_data
    push_came_to_work(day_data=clearing_day_data)
    push_went_to_gym(day_data=clearing_day_data)
    push_got_to_work_after_gym(day_data=clearing_day_data)
    push_left_work(day_data=clearing_day_data)


def push_clear_came_to_work():
    clearing_day_data = get_now_data()
    clearing_day_data["time_in_tuple_H_M"] = clearing_data
    pprint(clearing_day_data)
    push_came_to_work(day_data=clearing_day_data)


def push_clear_left_to_gym():
    clearing_day_data = get_now_data()
    clearing_day_data["time_in_tuple_H_M"] = clearing_data
    pprint(clearing_day_data)
    push_went_to_gym(day_data=clearing_day_data)


def push_clear_back_to_work():
    clearing_day_data = get_now_data()
    clearing_day_data["time_in_tuple_H_M"] = clearing_data
    push_got_to_work_after_gym(day_data=clearing_day_data)
    pprint(clearing_day_data)


def push_clear_left_work():
    clearing_day_data = get_now_data()
    clearing_day_data["time_in_tuple_H_M"] = clearing_data
    pprint(clearing_day_data)
    push_left_work(day_data=clearing_day_data)


def main():
    pass


if __name__ == '__main__':
    main()
