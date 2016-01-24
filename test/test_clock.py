from unittest import TestCase

import arrow
from hamcrest import assert_that, is_

from bank.clock import Clock


class TestClock(Clock):
    def today(self):
        return arrow.get("2015-07-13")


class ClockTest(TestCase):
    def test_clock_converts_today_to_string(self):
        clock = TestClock()
        assert_that(clock.date_as_string(), is_("13-07-2015"))
