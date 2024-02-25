import datetime
from misc.constants import MONTHLY_DICT


def get_today_date_in_str() -> str:
    today = datetime.date.today().strftime("%d.%m.%Y")
    return today

#
# def get_time_now_tuple_H_M() -> tuple:
#     hour = datetime.datetime.now().hour
#     minute = datetime.datetime.now().minute
#     now = (hour, minute,)
#     # print(now)
#     return now
#


def get_time_now_in_str() -> str:
    return datetime.datetime.now().strftime("%H:%M")


def get_month_in_ru_str_from_datetime(date: datetime.datetime) -> str:
    month_in_eng = date.strftime("%B")
    month_in_ru = MONTHLY_DICT[month_in_eng]
    return month_in_ru


def get_date_obj_by_date(*, date: str) -> datetime.datetime:
    return datetime.datetime.strptime(date, "%d.%m.%Y %H:%M")


if __name__ == "__main__":
    date = get_date_obj_by_date(date="23.02.2022 11:22")
    print(date)
    print(type(date))
    date_str = date.strftime("%d.%m.%Y %H:%M")
    print(date_str)
    print(type(date_str))
    print(get_time_now_in_str())
    pass
