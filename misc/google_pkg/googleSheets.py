import gspread
from gspread import Spreadsheet, Client, Worksheet
from gspread.utils import rowcol_to_a1
from gspread.utils import a1_to_rowcol

from misc import constants


CELL_COL_CAME_TO_WORK_H = a1_to_rowcol(constants.CELL_A1_HEADER_CAME_TO_WORK_H)[1]
CELL_COL_CAME_TO_WORK_M = a1_to_rowcol(constants.CELL_A1_HEADER_CAME_TO_WORK_M)[1]
CELL_COL_LEFT_TO_GYM_H = a1_to_rowcol(constants.CELL_A1_HEADER_LEFT_TO_GYM_H)[1]
CELL_COL_LEFT_TO_GYM_M = a1_to_rowcol(constants.CELL_A1_HEADER_LEFT_TO_GYM_M)[1]
CELL_COL_RETURN_FROM_GYM_H = a1_to_rowcol(constants.CELL_A1_HEADER_RETURN_FROM_GYM_H)[1]
CELL_COL_RETURN_FROM_GYM_M = a1_to_rowcol(constants.CELL_A1_HEADER_RETURN_FROM_GYM_M)[1]
CELL_COL_LEFT_WORK_H = a1_to_rowcol(constants.CELL_A1_HEADER_LEFT_WORK_H)[1]
CELL_COL_LEFT_WORK_M = a1_to_rowcol(constants.CELL_A1_HEADER_LEFT_WORK_M)[1]


def get_spreadsheet() -> Spreadsheet:
    gc: Client = gspread.service_account(filename="service_account.json")
    sh: Spreadsheet = gc.open_by_url(url=constants.SPREADSHEET_URL)
    return sh


def update_cell_with_data(ws: Worksheet, cell_row: int, cell_col: int, data):
    ws.update_cell(row=cell_row, col=cell_col, value=data)


def get_row_of_today(ws: Worksheet, today: str) -> int:
    cell_coords = ws.find(today)
    return cell_coords.row


def get_worksheet_with_title(sh: Spreadsheet, title: str) -> Worksheet:
    ws = sh.worksheet(title=title)
    return ws


# __________________________________________________________
"""def get_titles_worksheets(sh: Spreadsheet) -> list:
    ws_titles = []
    for ws in sh.worksheets():
        ws_titles.append(ws.title)
        print(ws.title)
        print(type(ws.title))
    return ws_titles


def get_cell_data(ws: Worksheet, cell_a1: str):
    cell_val = ws.acell(label=cell_a1).value
    print(cell_val)
    return cell_val


# def get_index_of_ws_with_title(sh:Spreadsheet, title: str) -> int:
#     for ws in sh.worksheets():
#         if ws.title == title:
#


def del_ws_with_title(sh: Spreadsheet, title: str):
    for ws in sh.worksheets():
        if ws.title == title:
            sh.del_worksheet(ws)


def add_ws_write_data_del_ws(sh: Spreadsheet):
    new_ws = sh.add_worksheet(title="Title", cols=5, rows=6)
    input("press enter")
    new_ws.insert_row(values=["hello", "world"])
    input("press enter")
    new_ws.insert_note(cell="B2", content="some text")
    input("press enter")
    sh.del_worksheet(new_ws)


def show_all_ws(worksheets: Worksheet):
    for ws in worksheets:
        print(ws)


def get_url(sh: Spreadsheet) -> str:
    return str(sh.url)


def update_data_by_cell(ws: Worksheet, cell: list[int, int], data):
    ws.update_cell(row=cell[0], col=cell[1], value=data)
"""


if __name__ == "__main__":
    sh = get_spreadsheet()
    get_worksheet_with_title(sh, title="Январь")
