import pytest
from capital.capital_case import capital_case


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_other_than_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)