import datetime
from .constants import MONTHLY_DICT


def get_today_date() -> str:
    today = datetime.date.today().strftime("%d.%m.%Y")
    return today


def get_time_now_tuple_H_M() -> tuple:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    now = (hour, minute,)
    # print(now)
    return now


def get_current_month_in_ru_str() -> str:
    month = datetime.datetime.now().strftime("%B")
    month_in_ru = MONTHLY_DICT[month]
    # print(month_in_ru)
    return month_in_ru


if __name__ == "__main__":
    get_current_month_in_ru_str()
    pass
