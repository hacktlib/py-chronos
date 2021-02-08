import datetime
from unittest import mock

import chronos


@mock.patch('chronos.datetime.datetime')
def test_utc_now_mocked(datetime_mock):
    datetime_utc_now = mock.Mock()
    datetime_mock.utcnow.return_value = datetime_utc_now

    response = chronos.utc_now()

    assert response == datetime_utc_now

    datetime_mock.utcnow.assert_called_with()


def test_utc_now_real():
    response = chronos.utc_now()

    assert isinstance(response, datetime.datetime)


@mock.patch('chronos.utc_now')
@mock.patch('chronos.calendar.timegm')
@mock.patch('chronos.datetime.datetime')
def test_utc_timestamp_mocked(datetime_mock, calendar_timegm, utc_now):
    datetime_tuple = mock.Mock()
    datetime_utc_now = mock.Mock()
    datetime_utc_now.utctimetuple.return_value = datetime_tuple

    expected_response = mock.Mock()
    calendar_timegm.return_value = expected_response

    response = chronos.utc_timestamp(datetime_utc_now=datetime_utc_now)

    assert response == expected_response
    datetime_utc_now.utctimetuple.assert_called_with()
    calendar_timegm.assert_called_with(datetime_tuple)
    utc_now.assert_not_called()


def test_utc_timestamp_real():
    response = chronos.utc_timestamp()

    assert type(response) is int


@mock.patch('chronos.datetime.datetime')
def test_future_utc_datetime_mocked(datetime_mock, dummy_datetime):
    datetime_mock.utcnow.return_value = dummy_datetime

    days_delta = 1
    seconds_delta = 10

    response = chronos.future_utc_datetime(
        days=days_delta,
        seconds=seconds_delta,
    )

    assert response.day == dummy_datetime.day + days_delta
    assert response.second == dummy_datetime.second + seconds_delta


def test_future_utc_datetime_real():
    days_delta = 5

    future = chronos.future_utc_datetime(days=days_delta)

    assert isinstance(future, datetime.datetime)


def test_future_utc_timestamp():
    now = chronos.utc_timestamp()
    days_delta = 5
    days_in_seconds = days_delta * 24 * 60 * 60

    response = chronos.future_utc_timestamp(days=days_delta)

    assert type(response) is int
    assert response >= (now + days_in_seconds)


@mock.patch('chronos.datetime.datetime')
def test_past_utc_datetime_mocked(datetime_mock, dummy_datetime):
    datetime_mock.utcnow.return_value = dummy_datetime

    days_delta = 1
    seconds_delta = 10

    response = chronos.past_utc_datetime(
        days=days_delta,
        seconds=seconds_delta,
    )

    assert response.day == dummy_datetime.day - days_delta
    assert response.second == dummy_datetime.second - seconds_delta


def test_past_utc_datetime_real():
    days_delta = 5

    past = chronos.past_utc_datetime(days=days_delta)

    assert isinstance(past, datetime.datetime)


def test_past_utc_timestamp():
    now = chronos.utc_timestamp()
    days_delta = 5
    days_in_seconds = days_delta * 24 * 60 * 60

    response = chronos.past_utc_timestamp(days=days_delta)

    assert type(response) is int
    assert response >= (now - days_in_seconds)


def test_round_datetime_down(dummy_datetime):
    rounded = chronos.round_datetime_down(
        dt=dummy_datetime,
        round_attr=chronos.types.DatetimeAttr('hour'),
    )

    assert rounded.year == dummy_datetime.year
    assert rounded.month == dummy_datetime.month
    assert rounded.day == dummy_datetime.day
    assert rounded.hour == dummy_datetime.hour
    assert rounded.minute == 0
    assert rounded.second == 0
    assert rounded.microsecond == 0

    rounded = chronos.round_datetime_down(
        dt=dummy_datetime,
        round_attr=chronos.types.DatetimeAttr('minute'),
    )

    assert rounded.year == dummy_datetime.year
    assert rounded.month == dummy_datetime.month
    assert rounded.day == dummy_datetime.day
    assert rounded.hour == dummy_datetime.hour
    assert rounded.minute == dummy_datetime.minute
    assert rounded.second == 0
    assert rounded.microsecond == 0
