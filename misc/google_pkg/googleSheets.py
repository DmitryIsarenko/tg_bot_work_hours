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


def get_row_of_day(ws: Worksheet, date_in_str: str) -> int:
    cell_coords = ws.find(date_in_str)
    return cell_coords.row


def get_worksheet_with_title(sh: Spreadsheet, title: str) -> Worksheet:
    ws = sh.worksheet(title=title)
    return ws


if __name__ == "__main__":
    pass
