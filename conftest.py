import datetime

import pytest


@pytest.fixture
def datetime_kwargs():
    return {
        'year': 2020,
        'month': 6,
        'day': 15,
        'hour': 12,
        'minute': 30,
        'second': 30,
        'microsecond': 500000,
    }


@pytest.fixture
def dummy_datetime(datetime_kwargs):
    return datetime.datetime(**datetime_kwargs)
