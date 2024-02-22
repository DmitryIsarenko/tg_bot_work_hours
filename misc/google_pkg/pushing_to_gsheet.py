# from misc.googleSheets import get_spreadsheet, get_row_of_today, update_cell_with_data
# from misc.time_operations import get_today_date, get_time_tuple_now, get_current_month_in_ru_str
# import constants

# import constants
from misc.google_pkg import googleSheets
from misc import time_operations

sh = googleSheets.get_spreadsheet()
ws = sh.worksheet(title=time_operations.get_current_month_in_ru_str())
today_date = time_operations.get_today_date()
today_month_str = time_operations.get_current_month_in_ru_str()
time_in_tuple_H_M = time_operations.get_time_now_tuple_H_M()
row_of_today = googleSheets.get_row_of_today(ws=ws, today=today_date)

print(sh)
print(ws)
print(today_date)
print(today_month_str)
print(time_in_tuple_H_M)
print(row_of_today)
clearing_data = ("", "",)


def push_time_came_to_work(*, data: tuple):
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_CAME_TO_WORK_H,
                                       cell_row=row_of_today,
                                       data=data[0]
                                       )
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_CAME_TO_WORK_M,
                                       cell_row=row_of_today,
                                       data=data[1]
                                       )


def push_time_went_to_gym(*, data: tuple):
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_H,
                                       cell_row=row_of_today,
                                       data=data[0]
                                       )
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_M,
                                       cell_row=row_of_today,
                                       data=data[1]
                                       )


def push_time_get_to_work_after_gym(*, data: tuple):
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_H,
                                       cell_row=row_of_today,
                                       data=data[0]
                                       )
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_M,
                                       cell_row=row_of_today,
                                       data=data[1]
                                       )


def push_time_left_work(*, data: tuple):
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_LEFT_WORK_H,
                                       cell_row=row_of_today,
                                       data=data[0]
                                       )
    googleSheets.update_cell_with_data(ws=ws,
                                       cell_col=googleSheets.CELL_COL_LEFT_WORK_M,
                                       cell_row=row_of_today,
                                       data=data[1]
                                       )


def push_clear_all_cells():
    push_time_came_to_work(data=clearing_data)
    push_time_went_to_gym(data=clearing_data)
    push_time_get_to_work_after_gym(data=clearing_data)
    push_time_left_work(data=clearing_data)


def push_clear_came_to_work():
    push_time_came_to_work(data=clearing_data)


def push_clear_left_to_gym():
    push_time_went_to_gym(data=clearing_data)


def push_clear_back_to_work():
    push_time_get_to_work_after_gym(data=clearing_data)


def push_clear_left_work():
    push_time_left_work(data=clearing_data)


def main():
    pass


if __name__ == '__main__':
    main()
