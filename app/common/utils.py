import random
import datetime


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def clamp(n: int = 0, min: int = 0, max: int = 0):
    if n < min:
        return min
    if n > max:
        return max
    return n


def generate_random_range(max_value: int):
    start = random.randint(0, max_value - 1)
    end = random.randint(start + 1, max_value)
    return start, end


def date_to_timestamp(date_obj: datetime.date) -> int:
    unix_epoch = datetime.datetime(1970, 1, 1)
    delta = date_obj - unix_epoch.date()
    timestamp = int(delta.total_seconds())
    return timestamp


def generate_random_date(min_year: int, max_year: int, min_month: int = 1, max_month: int = 12, min_day: int = 1, max_day=28) -> datetime.datetime:
    min_month = clamp(n=min_month, min=1, max=12)
    max_month = clamp(n=max_month, min=1, max=12)
    min_day = clamp(n=min_day, min=1, max=28)
    max_day = clamp(n=max_day, min=1, max=28)
    year = random.randint(min_year, max_year)
    month = random.randint(min_month, max_month)
    day = random.randint(min_day, max_day)
    random_date = datetime.date(year, month, day)
    time_stamp = date_to_timestamp(random_date)
    utc_date = datetime.datetime.utcfromtimestamp(time_stamp)
    return utc_date
