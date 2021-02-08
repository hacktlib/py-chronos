import calendar
import datetime
from typing import Optional

from chronos import types, datetime_filter


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


def round_datetime_down(
    dt: datetime.datetime,
    round_attr: types.DatetimeAttr,
) -> datetime.datetime:
    order = types.DatetimeAttrOrder()
    threshold = order[round_attr]

    return datetime.datetime(
        **datetime_filter.reset_attributes(
            dt=dt,
            attr_names=[
                attribute_name
                for attribute_name, position in order.items()
                if position < threshold
            ],
        )
    )
