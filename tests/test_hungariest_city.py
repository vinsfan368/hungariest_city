from hungariest_city import get_hungariest
from unittest import TestCase


class TestGetHungariest(TestCase):
    def test_get_hungariest(self):
        result = get_hungariest()
        assert isinstance(result, str), result
