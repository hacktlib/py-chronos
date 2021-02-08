from chronos import datetime_filter


def test_reset_attributes(dummy_datetime):
    rounded_dt = datetime_filter.reset_attributes(
        dt=dummy_datetime,
        attr_names=['minute', 'second', 'microsecond']
    )

    assert rounded_dt['year'] == dummy_datetime.year
    assert rounded_dt['month'] == dummy_datetime.month
    assert rounded_dt['day'] == dummy_datetime.day
    assert rounded_dt['hour'] == dummy_datetime.hour
    assert rounded_dt['minute'] == 0
    assert rounded_dt['second'] == 0
    assert rounded_dt['microsecond'] == 0

    rounded_dt = datetime_filter.reset_attributes(
        dt=dummy_datetime,
        attr_names=['second', 'microsecond']
    )

    assert rounded_dt['year'] == dummy_datetime.year
    assert rounded_dt['month'] == dummy_datetime.month
    assert rounded_dt['day'] == dummy_datetime.day
    assert rounded_dt['hour'] == dummy_datetime.hour
    assert rounded_dt['minute'] == dummy_datetime.minute
    assert rounded_dt['second'] == 0
    assert rounded_dt['microsecond'] == 0
