import pytest
from datetime import date
import problem_set9.seasons as seasons


def test_get_birth_date():
    assert seasons.birth_date("1999-01-01") == date(1999, 1, 1)
    assert seasons.birth_date("0001-01-01") == date(1, 1, 1)
    assert seasons.birth_date("2021-1-1") == date(2021, 1, 1)

    with pytest.raises(ValueError):
        seasons.birth_date("2/3/2023")
        seasons.birth_date("2/3/2023")
        seasons.birth_date("2020-14-14")
        seasons.birth_date("14/14/2020")
        seasons.birth_date("hello")


def test_get_difference():
    assert seasons.get_difference(date(2023,1,19), date(2022, 1, 19)) == 525600


    with pytest.raises(TypeError):
        seasons.get_difference(date(2023,1,19), "hello")
        seasons.get_difference(date(2023,1,19), "2022-02-01")
