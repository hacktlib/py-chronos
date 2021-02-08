import datetime
from typing import Dict, List

from chronos.types import (
    DatetimeAttr,
    DatetimeAttrOrder,
)


def reset_attributes(
    dt: datetime.datetime,
    attr_names: List[DatetimeAttr],
) -> Dict[DatetimeAttr, int]:
    datetime_attr = DatetimeAttrOrder()

    return {
        attr: 0 if attr in attr_names else getattr(dt, attr)
        for attr in datetime_attr.attributes
    }
