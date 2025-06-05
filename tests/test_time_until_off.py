import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from time_until_off import parse_end_time, time_until


def test_time_until_same_day():
    now = dt.datetime(2023, 1, 1, 17, 15)
    delta = time_until("18:30", now)
    assert delta == dt.timedelta(hours=1, minutes=15)


def test_time_until_next_day():
    now = dt.datetime(2023, 1, 1, 17, 15)
    delta = time_until("16:00", now)
    assert delta == dt.timedelta(hours=22, minutes=45)
