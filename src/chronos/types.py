import collections


class DatetimeAttr(collections.UserString):

    def __init__(self, data: str) -> None:
        dt_attr = DatetimeAttrOrder()

        if data not in dt_attr.attributes:
            raise ValueError(f'Invalid datetime attribute {data}')

        super().__init__(data)


class DatetimeDeltaAttr(collections.abc.MutableMapping):

    def __init__(self):
        dt_attr_order = DatetimeAttrOrder()

        self.delta_attributes = {
            attr: f'{attr}s'
            for attr in dt_attr_order.attributes
        }

    def __getitem__(self, attr):
        return self.delta_attributes[attr]

    def __delitem__(self, attr):
        raise KeyError('Cannot delete item from {self.__class__.__name__}')

    def __iter__(self):
        return iter(self.delta_attributes)

    def __len__(self):
        return len(self.delta_attributes)

    def __setitem__(self, attr, val):
        raise KeyError('Cannot set item to {self.__class__.__name__}')


class DatetimeAttrOrder(collections.abc.MutableMapping):

    def __init__(self):
        self.attributes = [
            'microsecond',
            'second',
            'minute',
            'hour',
            'day',
            'month',
            'year',
        ]

        self.attr_order = {attr: i for i, attr in enumerate(self.attributes)}

    def __getitem__(self, attr):
        return self.attr_order[attr]

    def __delitem__(self, attr):
        raise KeyError('Cannot delete item from {self.__class__.__name__}')

    def __iter__(self):
        return iter(self.attr_order)

    def __len__(self):
        return len(self.attr_order)

    def __setitem__(self, attr, val):
        raise KeyError('Cannot set item to {self.__class__.__name__}')
