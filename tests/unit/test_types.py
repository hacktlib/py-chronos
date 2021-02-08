import pytest

import chronos.types


def test_datetime_attr_order():
    datetime_attr_order = chronos.types.DatetimeAttrOrder()

    assert datetime_attr_order['year'] == 6
    assert datetime_attr_order['month'] == 5
    assert datetime_attr_order['day'] == 4
    assert datetime_attr_order['hour'] == 3
    assert datetime_attr_order['minute'] == 2
    assert datetime_attr_order['second'] == 1
    assert datetime_attr_order['microsecond'] == 0


def test_datetime_attr_order_locks():
    datetime_attr_order = chronos.types.DatetimeAttrOrder()

    # Should prevent setting new items
    with pytest.raises(KeyError):
        datetime_attr_order['foo'] = 'bar'

    # Should avoid deleting items
    with pytest.raises(KeyError):
        del datetime_attr_order['year']

    # Should not take any arguments
    with pytest.raises(TypeError):
        chronos.types.DatetimeAttrOrder(hello='world')


def test_datetime_delta_attr():
    delta_attr = chronos.types.DatetimeDeltaAttr()

    assert delta_attr['year'] == 'years'
    assert delta_attr['month'] == 'months'
    assert delta_attr['day'] == 'days'
    assert delta_attr['hour'] == 'hours'
    assert delta_attr['minute'] == 'minutes'
    assert delta_attr['second'] == 'seconds'
    assert delta_attr['microsecond'] == 'microseconds'


def test_datetime_delta_attr_locks():
    delta_attr = chronos.types.DatetimeDeltaAttr()

    # Should prevent setting new items
    with pytest.raises(KeyError):
        delta_attr['foo'] = 'bar'

    # Should avoid deleting items
    with pytest.raises(KeyError):
        del delta_attr['year']

    # Should not take any arguments
    with pytest.raises(TypeError):
        chronos.types.DatetimeDeltaAttr(hello='world')


def test_datetime_attr():
    assert chronos.types.DatetimeAttr('year') == 'year'
    assert chronos.types.DatetimeAttr('month') == 'month'
    assert chronos.types.DatetimeAttr('day') == 'day'
    assert chronos.types.DatetimeAttr('hour') == 'hour'
    assert chronos.types.DatetimeAttr('minute') == 'minute'
    assert chronos.types.DatetimeAttr('second') == 'second'
    assert chronos.types.DatetimeAttr('microsecond') == 'microsecond'


def test_datetime_attr_invalid():
    with pytest.raises(ValueError):
        chronos.types.DatetimeAttr('foobar')
