# from misc.googleSheets import get_spreadsheet, get_row_of_today, update_cell_with_data
# from misc.time_operations import get_today_date, get_time_tuple_now, get_current_month_in_ru_str
# import constants
import datetime

# import constants
from misc.google_pkg import googleSheets
from misc import time_operations
from pprint import pprint


def push_some_data_to_some_cell(date_in_str: str, time_in_str: str, stage: str) -> None:
    datetime_str = date_in_str + " " + time_in_str
    datetime_obj = datetime.datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
    month_in_str = time_operations.get_month_in_ru_str_from_datetime(date=datetime_obj)

    sh = googleSheets.get_spreadsheet()
    ws = googleSheets.get_worksheet_with_title(title=month_in_str, sh=sh)

    cell_row = googleSheets.get_row_of_day(ws=ws, date_in_str=date_in_str)

    if stage == "came to work":
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_CAME_TO_WORK_H,
                                           cell_row=cell_row,
                                           data=datetime_obj.hour
                                           )
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_CAME_TO_WORK_M,
                                           cell_row=cell_row,
                                           data=datetime_obj.minute
                                           )
    elif stage == "went to gym":
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_H,
                                           cell_row=cell_row,
                                           data=datetime_obj.hour
                                           )
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_LEFT_TO_GYM_M,
                                           cell_row=cell_row,
                                           data=datetime_obj.minute
                                           )
    elif stage == "back_to_work":
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_H,
                                           cell_row=cell_row,
                                           data=datetime_obj.hour
                                           )
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_RETURN_FROM_GYM_M,
                                           cell_row=cell_row,
                                           data=datetime_obj.minute
                                           )
    elif stage == "left work":
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_LEFT_WORK_H,
                                           cell_row=cell_row,
                                           data=datetime_obj.hour
                                           )
        googleSheets.update_cell_with_data(ws=ws,
                                           cell_col=googleSheets.CELL_COL_LEFT_WORK_M,
                                           cell_row=cell_row,
                                           data=datetime_obj.minute
                                           )
    else:
        print("ошибка")


def main():
    pass


if __name__ == '__main__':
    main()
