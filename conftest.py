import datetime

import pytest


@pytest.fixture
def dummy_utc_now_datetime():
    datetime_args = {
        'year': 2020,
        'month': 6,
        'day': 15,
        'hour': 12,
        'minute': 30,
        'second': 30,
    }

    return datetime.datetime(**datetime_args)
