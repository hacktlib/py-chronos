import calendar
import datetime
from typing import Optional


def future_utc_timestamp(**delta_kwargs) -> int:
    return utc_timestamp(future_utc_datetime(**delta_kwargs))


def future_utc_datetime(**delta_kwargs) -> datetime.datetime:
    return utc_now() + datetime.timedelta(**delta_kwargs)


def past_utc_timestamp(**delta_kwargs) -> int:
    return utc_timestamp(past_utc_datetime(**delta_kwargs))


def past_utc_datetime(**delta_kwargs) -> datetime.datetime:
    return utc_now() - datetime.timedelta(**delta_kwargs)


def utc_timestamp(datetime_utc_now: Optional[datetime.datetime] = None) -> int:
    if datetime_utc_now is None:
        datetime_utc_now = utc_now()

    return calendar.timegm(datetime_utc_now.utctimetuple())


def utc_now() -> datetime.datetime:
    return datetime.datetime.utcnow()
