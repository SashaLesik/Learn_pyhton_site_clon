from datetime import datetime, timedelta


month_mapping = {'январь': 1,
                 'февраль': 2,
                 'март': 3,
                 'апрель': 4,
                 'май': 5,
                 'июнь': 6,
                 'июль': 7,
                 'август': 8,
                 'сентябрь': 9,
                 'октябрь': 10,
                 'ноябрь': 11,
                 'декабрь': 12,
                 'января': 1,
                 'февраля': 2,
                 'марта': 3,
                 'апреля': 4,
                 'мая': 5,
                 'июня': 6,
                 'июля': 7,
                 'августа': 8,
                 'сентября': 9,
                 'октября': 10,
                 'ноября': 11,
                 'декабря': 12}

def detect_month_num(dt_element: list[str]) -> int:
    matching_months = set(dt_element).intersection(set(month_mapping.keys()))
    month = matching_months.pop()
    return month_mapping[month]


def detect_year(dt_element: list[str]) -> int:
    for el in dt_element:
        if el.isdigit() and len(el) == 4:
            return int(el)
    raise ValueError(f'year not present {dt_element}')


def parse_register_date(date_time: str | int) -> datetime:
    #  Дата регистрации пользователя
    dt_element = date_time.split(' ')
    month = detect_month_num(dt_element)
    year = detect_year(dt_element)
    return datetime(year, month, day=1)


def parse_last_online_date(date_time: str) -> datetime:
    # Дата последнего посещения сайта пользователем
    date_time = date_time.split(' ')
    if len(date_time) > 4:
        day = int(date_time[1])
        month = detect_month_num(date_time)
        year = int(date_time[3])
        return datetime(year, month, day)
    elif len(date_time) == 3:
        hour, minute = date_time[2].split(':')
        date_of_last_visit = datetime.now().replace(hour=int(hour), minute=int(minute))
        return date_of_last_visit
    elif len(date_time) == 4:
        hour, minute = date_time[3].split(':')
        day_earlier = datetime.now() - timedelta(days=1)
        date_of_last_visit = day_earlier.replace(hour=int(hour), minute=int(minute))
        return date_of_last_visit
    else:
        raise Exception


def parse_published_date(date_time) -> datetime:
    # Дата публикации объявления
    date_time = date_time.split(' ')
    if date_time[0].isdigit():
        day = int(date_time[0])
        month = detect_month_num(date_time)
        year = int(date_time[2])
        published_date = datetime(year, month, day)
        return published_date
    elif date_time[0] == 'Сегодня':
        hour, minute = date_time[2].split(':')
        published_date = datetime.now().replace(hour=int(hour), minute=int(minute))
        return published_date